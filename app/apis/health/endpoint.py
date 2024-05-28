from fastapi import APIRouter, Depends, status


router = APIRouter()


@router.get("", status_code=status.HTTP_200_OK, description="Health check")
async def health_check() -> str:

    return "ok"
