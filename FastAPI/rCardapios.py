import db
import dtos
from util import Utilidades
from fastapi import status, HTTPException, APIRouter, Depends

cardapios = APIRouter()

@cardapios.get('/cardapio')
async def listar_cardapios():
      
        return db.cardapios.items()

@cardapios.get('/cardapio/{codigo}')
async def consultar_cardapio(codigo: str):
    if codigo in db.cardapios:
        return db.cardapios[codigo]
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Cardápio não encontrado')


@cardapios.post('/cardapio/', status_code=status.HTTP_201_CREATED)
async def cadastrar_cardapio(cardapio: dtos.CardapioIn, util: Utilidades = Depends(Utilidades)) -> dtos.Cardapio:
    codigo = util.criar_codigo(cardapio.nome)
    db.cardapios[codigo] = cardapio.model_dump()
    db.cardapios[codigo]['codigo'] = codigo
    return db.cardapios[codigo]


@cardapios.put('/cardapio/{codigo}')
async def alterar_cardapio(codigo: str, cardapio: dtos.CardapioIn):
    if codigo in db.cardapios:
        db.cardapios[codigo] = db.cardapios.model_dump()
        return db.cardapios[codigo]
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Cardápio não cadastrado')


@cardapios.delete('/cardapio/{codigo}')
async def remover_produto(codigo: str):
    if codigo in db.cardapios:
        return db.cardapios.pop(codigo)
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Cardápio inexistente')
    

@cardapios.patch('/cardapio/{id}')
async def alterar_descricao_cardapio(codigo: int, descricao: dtos.Descricao):
    if codigo in db.cardapios:
        db.cardapios[codigo]['descricao'] = descricao.preco
        return db.cardapios[codigo]
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Cardápio não cadastrado')