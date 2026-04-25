from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/api/v1/demo", tags=["demo"])

DEMO_COMPANIES = [
    {
        "id": 1,
        "name": "Example Retail Ltd",
        "domain": "example-retail.test",
        "risk_level": "medium",
        "risk_score": 54,
        "source": "demo",
    },
    {
        "id": 2,
        "name": "Sample Finance Group",
        "domain": "sample-finance.test",
        "risk_level": "high",
        "risk_score": 78,
        "source": "demo",
    },
]

DEMO_REQUESTS: dict[int, dict[str, object]] = {}


@router.get("/companies")
def list_detected_companies() -> list[dict[str, object]]:
    return DEMO_COMPANIES


@router.get("/companies/{company_id}")
def get_detected_company(company_id: int) -> dict[str, object]:
    for company in DEMO_COMPANIES:
        if company["id"] == company_id:
            return company
    raise HTTPException(status_code=404, detail="Company not found")


@router.get("/companies/{company_id}/risk")
def get_company_risk(company_id: int) -> dict[str, object]:
    company = get_detected_company(company_id)
    return {
        "company_id": company["id"],
        "risk_level": company["risk_level"],
        "risk_score": company["risk_score"],
        "explanation": "Demo score based on placeholder privacy-risk signals.",
    }


@router.post("/companies/{company_id}/privacy-requests", status_code=201)
def create_privacy_request(company_id: int) -> dict[str, object]:
    company = get_detected_company(company_id)
    request_id = len(DEMO_REQUESTS) + 1
    request = {
        "id": request_id,
        "company_id": company["id"],
        "company_name": company["name"],
        "request_type": "access",
        "status": "draft",
        "template_reference": "gdpr-access-request-v1",
    }
    DEMO_REQUESTS[request_id] = request
    return request


@router.get("/privacy-requests/{request_id}")
def get_privacy_request_status(request_id: int) -> dict[str, object]:
    request = DEMO_REQUESTS.get(request_id)
    if request is None:
        raise HTTPException(status_code=404, detail="Privacy request not found")
    return request
