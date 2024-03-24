from flask import redirect, url_for, request, current_app as app
from utils.spotify_client import SpotifyClient


def login():
    scope = 'user-library-modify ' \
            'playlist-read-private ' \
            'user-library-read ' \
            'playlist-modify-public ' \
            'playlist-read-collaborative ' \
            'playlist-modify-private '

    spotify_client = SpotifyClient(
        app.config['CLIENT_ID'],
        app.config['CLIENT_SECRET'],
        app.config['REDIRECT_URI']
    )
    return spotify_client.authenticate(scope)


def callback():
    code = request.args.get('code')
    spotify_client = SpotifyClient(
        app.config['CLIENT_ID'],
        app.config['CLIENT_SECRET'],
        app.config['REDIRECT_URI']
    )
    if spotify_client.get_access_token(code):
        return redirect(url_for("blueprints.tracks"))
    else:
        return 'Falha ao obter o token de acesso.'


def tracks():
    spotify_client = SpotifyClient(
        app.config['CLIENT_ID'],
        app.config['CLIENT_SECRET'],
        app.config['REDIRECT_URI']
    )

    favorite_tracks = spotify_client.get_favorite_tracks()

    if favorite_tracks is not None:
        if spotify_client.remove_duplicate_tracks(favorite_tracks):
            return "Músicas removidas com sucesso!"
        else:
            return "Falha ao remover as músicas."
    else:
        return 'Falha ao obter as faixas favoritas.'
