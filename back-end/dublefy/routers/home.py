from fastapi import APIRouter

from dublefy.schemas.message import Message

rt_home = APIRouter()


@rt_home.get('/', response_model=Message)
def home():
    return {
        'message': 'Adicione /docs na URL para ter mais detalhes sobre a API.'
    }
