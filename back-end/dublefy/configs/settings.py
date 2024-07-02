from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env', env_file_encoding='utf-8'
    )

    CLIENT_ID: str
    TOKEN_URL: str
    TRACKS_URL: str
    REDIRECT_URI: str
    CLIENT_SECRET: str
    AUTHORIZE_URL: str
    TRACKS_URL_DELETE: str
