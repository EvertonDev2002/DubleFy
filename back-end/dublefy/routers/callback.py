from http import HTTPStatus
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException

from dublefy.utils.spotify_client import SpotifyClient

rt_callback = APIRouter()


@rt_callback.get(
    '/callback',
    summary='Callback para receber a autorização do Spotify',
)
async def callback(
    code: Optional[str] = None,
    spotify_client: SpotifyClient = Depends(SpotifyClient),
):
    if not code:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Código de autorização não fornecido!',
        )

    access_token = await spotify_client.get_access_token(code)

    if not access_token:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Falha ao obter o token de acesso!',
        )
    return access_token
