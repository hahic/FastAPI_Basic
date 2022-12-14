from pydantic import BaseModel, Field


class CreateTokenResponse(BaseModel):
    token: str = Field(..., description="Token")


class RefreshTokenResponse(BaseModel):
    token: str = Field(..., description="Token")
    refresh_token: str = Field(..., description="Refresh token")
