from pydantic import BaseModel, Field


class VerifyTokenRequest(BaseModel):
    token: str = Field(..., description="Token")
    

class CreateTokenRequest(BaseModel):
    role: str = 'dev'
    

class RefreshTokenRequest(BaseModel):
    token: str = Field(..., description="Token")
    refresh_token: str = Field(..., description="Refresh token")


