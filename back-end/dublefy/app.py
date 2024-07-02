from fastapi import FastAPI

from dublefy.routers import auth, callback, home, tracks

app = FastAPI()


# Home
app.include_router(home.rt_home)
# Autenticação do Spotify
app.include_router(auth.rt_auth)
# Callback para o retorno do Spotify
app.include_router(callback.rt_callback)
# Manipulação das faixas
app.include_router(tracks.rt_tracks)
