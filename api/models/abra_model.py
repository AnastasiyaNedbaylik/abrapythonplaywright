from __future__ import annotations
from typing import Optional

from pydantic import BaseModel


class LoginRequestModel(BaseModel):
    email: Optional[str | int | bool] = None
    password: Optional[str | int | bool] = None


class LoginResponseModel(BaseModel):
    ok: bool
    result: bool
#    detail: str
 #   error: str
#    error_code: int
