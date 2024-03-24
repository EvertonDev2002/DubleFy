from flask import redirect, current_app as app
from requests import post, get, delete
from urllib.parse import urlencode
from datetime import datetime


class SpotifyClient:
    def __init__(self, client_id: str, client_secret: str, redirect_uri: str):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri

    def authenticate(self, scope: str):
        auth_params = {
            'response_type': 'code',
            'client_id': self.client_id,
            'scope': scope,
            'redirect_uri': self.redirect_uri,
        }
        auth_url = f"{app.config['AUTHORIZE_URL']}?{urlencode(auth_params)}"
        return redirect(auth_url)

    def get_access_token(self, code: str | None):
        token_params = {
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': self.redirect_uri,
            'client_id': self.client_id,
            'client_secret': self.client_secret,
        }
        response = post(app.config['TOKEN_URL'], data=token_params)
        if response.status_code == 200:
            token_info = response.json()
            app.config.set(  # type: ignore
                'ACCESS_TOKEN',
                token_info['access_token']
            )
            return True
        return False

    def get_favorite_tracks(self):

        if not app.config['ACCESS_TOKEN']:
            return None

        limit = 50
        offset = 0
        all_tracks = []

        while True:
            params = {'limit': limit, 'offset': offset}
            headers = {'Authorization': f"Bearer {app.config['ACCESS_TOKEN']}"}
            tracks_response = get(
                app.config['TRACKS_URL'],
                params=params,
                headers=headers
            )

            if tracks_response.status_code == 200:
                tracks_data = tracks_response.json()
                tracks = tracks_data.get('items', [])
                all_tracks.extend(tracks)

                if len(tracks) < limit:
                    break
                else:
                    offset += limit
            else:
                return None

        favorite_tracks = []
        for data in all_tracks:
            track = {
                'id': data['track']['id'],
                'name': data['track']['name'],
                'artist': data['track']['artists'][0]['name'],
                'added_at': datetime.strptime(
                    data['added_at'],
                    '%Y-%m-%dT%H:%M:%SZ'
                )
            }
            favorite_tracks.append(track)

        return favorite_tracks

    def remove_duplicate_tracks(self, favorite_tracks: list):  # type: ignore
        if not app.config['ACCESS_TOKEN'] or not favorite_tracks:
            return False

        duplicate_tracks = []
        unique_track_names = set()

        for track in favorite_tracks:
            if track['name'] not in unique_track_names:
                unique_track_names.add(track['name'])
            else:
                duplicate_tracks.append(track['id'])

        if duplicate_tracks:
            headers = {
                'Authorization': f"Bearer {app.config['ACCESS_TOKEN']}"
            }

            for i in range(0, len(duplicate_tracks), 50):
                batch_ids = duplicate_tracks[i:i+50]
                data = {'ids': batch_ids}
                print(f"Antes: {data}")

                response = delete(
                    app.config['TRACKS_URL_DELETE'],
                    json=data,
                    headers=headers
                )

                if response.status_code != 200:
                    return False
            return True
