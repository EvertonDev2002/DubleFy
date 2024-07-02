from pydantic import BaseModel


class TokenAccessCallback(BaseModel):
    token_access: str


class CodeCallback(BaseModel):
    code: str
