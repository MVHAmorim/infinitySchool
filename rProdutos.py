import db
import dtos
from typing import Optional
from util import Utilidades
from fastapi import status, APIRouter, HTTPException, Depends

produtos = APIRouter()

@produtos.get('/produto')
async def listar_produtos(cardapio: Optional[str] = -1, preco_min: Optional[int] = -1, preco_max: Optional[int] = 999, restricao: Optional[str] = None):
      
        return {id: Produto for id, Produto in db.produtos.items() 
                if Produto['preco'] >= preco_min 
                and Produto['preco'] <= preco_max
                and (Produto['restricao'] == restricao or restricao is None)
                and (Produto['cardapio'] == cardapio or cardapio is None)}
    

@produtos.get('/produto/{id}')
async def consultar_produto(id: int):
    if id in db.produtos:
        return db.produtos[id]
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Produto não encontrado')


@produtos.post('/produto/', status_code=status.HTTP_201_CREATED )
async def cadastrar_produto(produto: dtos.ProdutoIn, util: Utilidades = Depends(Utilidades)) -> dtos.Produto:
    codigo = util.criar_codigo(produto.nome)
    db.produtos[codigo] = produto.model_dump()
    db.produtos[codigo]['codigo'] = codigo
    return db.produtos[codigo]


@produtos.put('/produto/{id}')
async def alterar_produto(id: int, aluno: dtos.ProdutoIn):
    if id in db.produtos:
        db.produtos[id] = aluno.model_dump()
        return db.produtos[id]
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Produto não cadastrado')


@produtos.delete('/produto/{id}')
async def remover_produto(id: int):
    if id in db.produtos:
        return db.produtos.pop(id)
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Produto inexistente')


@produtos.patch('/produto/{id}')
async def alterar_preco_produto(id: int, preco: dtos.Descricao):
    if id in db.produtos:
        db.produtos[id]['preco'] = preco.preco
        return db.produtos[id]
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Produto não cadastrado')
