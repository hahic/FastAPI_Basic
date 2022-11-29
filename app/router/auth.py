from fastapi import APIRouter, Response

from model.auth import request, response
from service.auth import JwtService

auth_router = APIRouter()


@auth_router.post("/verify")
async def verify_token(request: request.VerifyTokenRequest):
    await JwtService().verify_token(token=request.token)
    return Response(status_code=200)


@auth_router.post("/create", response_model=response.CreateTokenResponse)
async def create_token(request: request.CreateTokenRequest):
    token = await JwtService().create_token(**request.dict())
    return {"token": token}


@auth_router.post("/refresh", response_model=response.RefreshTokenResponse)
async def refresh_token(request: request.RefreshTokenRequest):
    token = await JwtService().refresh_token(**request.dict())
    return {"token": token.token, "refresh_token": token.refresh_token}