
from maneger.configuracoes.manegerConfiguracoes import resetar_banco
from fastapi import APIRouter

router = APIRouter()

@router.delete("/resetar_sistema")
def resetar_banco_de_dados():
    resetar_banco()
    return {"msg": "Banco resetado com sucesso"}