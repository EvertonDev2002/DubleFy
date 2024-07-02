from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException, Query

from dublefy.schemas.message import Message
from dublefy.schemas.track_schema import TracksResponse
from dublefy.utils.spotify_client import SpotifyClient

rt_tracks = APIRouter()


@rt_tracks.get('/tracks/{access_token}', response_model=TracksResponse)
async def tracks(
    access_token: str, spotify_client: SpotifyClient = Depends(SpotifyClient)
):
    favorite_tracks = await spotify_client.get_favorite_tracks(access_token)

    duplicates = await spotify_client.find_duplicates(favorite_tracks)

    if not favorite_tracks:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Falha ao obter músicas curtidas',
        )

    if not duplicates:
        return {'detail': 'Não há duplicatas'}
    return {'tracks': duplicates}


@rt_tracks.delete('/delete_tracks/', response_model=Message)
def delete_tracks(
    ids: list[int] = Query(...),
    access_token: str = Query(...),
    spotify_client: SpotifyClient = Depends(SpotifyClient),
):
    if not spotify_client.remove_duplicate_tracks(ids, access_token):
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Falha ao remover duplicatas!',
        )
    return {'message': 'Duplicatas removidas com sucesso!'}
