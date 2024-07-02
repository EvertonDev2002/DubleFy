from pydantic import BaseModel, HttpUrl


class auth(BaseModel):
    authorize_url: HttpUrl
