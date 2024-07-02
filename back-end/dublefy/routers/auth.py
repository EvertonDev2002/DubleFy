from fastapi import APIRouter, Depends

from dublefy.utils.spotify_client import SpotifyClient

rt_auth = APIRouter()


@rt_auth.get('/auth', summary='Pede autorização do Spotify')
async def auth(spotify_client: SpotifyClient = Depends(SpotifyClient)):
    scope = (
        'user-library-modify '
        'playlist-read-private '
        'user-library-read '
        'playlist-modify-public '
        'playlist-read-collaborative '
        'playlist-modify-private '
    )

    return spotify_client.authenticate(scope)
