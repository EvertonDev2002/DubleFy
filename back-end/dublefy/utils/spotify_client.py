from http import HTTPStatus

from fastapi.responses import RedirectResponse
from httpx import AsyncClient

from dublefy.configs.settings import Settings
from dublefy.schemas.track_schema import Track


class SpotifyClient:
    def __init__(self):
        self.urls = Settings()

    def authenticate(self, scope: str):
        params = {
            'client_id': self.urls.CLIENT_ID,
            'response_type': 'code',
            'redirect_uri': self.urls.REDIRECT_URI,
            'scope': scope,
        }
        auth_url = (
            f'{self.urls.AUTHORIZE_URL}?client_id={params["client_id"]}'
            f'&response_type={params["response_type"]}'
            f'&redirect_uri={params["redirect_uri"]}&scope={params["scope"]}'
        )
        return RedirectResponse(auth_url)

    async def get_access_token(self, code: str) -> str | bool:
        async with AsyncClient() as client:
            token_params = {
                'grant_type': 'authorization_code',
                'code': code,
                'redirect_uri': self.urls.REDIRECT_URI,
                'client_id': self.urls.CLIENT_ID,
                'client_secret': self.urls.CLIENT_SECRET,
            }
            response = await client.post(
                self.urls.TOKEN_URL, data=token_params
            )

        if response.status_code != HTTPStatus.OK:
            return False
        token_info = response.json()
        return token_info['access_token']

    async def get_favorite_tracks(
        self, access_token: str, limit: int = 50, offset: int = 0
    ) -> list[Track]:
        if not access_token:
            return []

        all_tracks = []

        async with AsyncClient() as client:
            while True:
                params = {'limit': limit, 'offset': offset}
                headers = {'Authorization': f'Bearer {access_token}'}
                response = await client.get(
                    self.urls.TRACKS_URL, params=params, headers=headers
                )

                if response.status_code == HTTPStatus.OK:
                    tracks_data = response.json()
                    tracks = tracks_data.get('items', [])
                    all_tracks.extend(tracks)

                    if len(tracks) < limit:
                        break
                    offset += limit
                else:
                    break

        favorite_tracks = []
        for data in all_tracks:
            track = Track(
                id=data['track']['id'],
                name=data['track']['name'],
                artist=data['track']['artists'][0]['name'],
                added_at=data['added_at'],  # Mantendo a data como string
            )
            favorite_tracks.append(track)

        return favorite_tracks

    @staticmethod
    async def find_duplicates(
        favorite_tracks: list[Track],
    ) -> list[Track]:
        if not favorite_tracks:
            return []

        seen_names = set()
        duplicate_tracks: list[Track] = []

        for track in favorite_tracks:
            track_name = track.name

            if track_name in seen_names:
                _track = Track(
                    id=track.id,
                    name=track.name,
                    artist=track.artist,
                    added_at=track.added_at,
                )
                duplicate_tracks.append(_track)
            else:
                seen_names.add(track_name)

        return duplicate_tracks

    async def remove_duplicate_tracks(
        self, duplicate_tracks: list[str], access_token: str
    ) -> bool:
        if not access_token or not duplicate_tracks:
            return False

        headers = {'Authorization': f'Bearer {access_token}'}

        async with AsyncClient() as client:
            for i in range(0, len(duplicate_tracks), 40):
                batch_ids = duplicate_tracks[i : i + 40]
                data = {'ids': batch_ids}

                response = await client.delete(
                    self.urls.TRACKS_URL_DELETE,
                    json=data,
                    headers=headers,
                )

                if response.status_code != HTTPStatus.OK:
                    return False

        return True
