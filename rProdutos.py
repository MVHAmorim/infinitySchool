import db
import dtos
from typing import Optional
from util import Utilidades
from fastapi import status, APIRouter, HTTPException, Depends
from dependencias import obter_repo_cardapio, obter_repo_produto
from repositorio_produto import RepositorioProduto
from repositorio_cardapio import RepositorioCardapio

produtos = APIRouter()

@produtos.get('/produto')
async def listar_produtos(cardapio: Optional[str] = -1, preco_min: Optional[int] = -1, preco_max: Optional[int] = 999, restricao: Optional[str] = None):
      
        return {id: Produto for id, Produto in db.produtos.items() 
                if Produto['preco'] >= preco_min 
                and Produto['preco'] <= preco_max
                and (Produto['restricao'] == restricao or restricao is None)
                and (Produto['cardapio'] == cardapio or cardapio is None)}
    

@produtos.get('/produto/{id}')
async def consultar_produto(codigo: str,
    repProduto: RepositorioProduto = Depends(obter_repo_produto)):

    retorno = repProduto.consultar_produto(codigo)

    if not retorno:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Produto não encontrado')

    return retorno


@produtos.post('/produto/', status_code=status.HTTP_201_CREATED )
async def cadastrar_produto(nome: str, descricao: str, preco: float, 
    restricao: str, cardapio: str, util: Utilidades = Depends(Utilidades),
    repProduto: RepositorioProduto = Depends(obter_repo_produto)):

    codigo = util.criar_codigo(nome)
    retorno = repProduto.criar_produto(codigo, nome, descricao, preco, restricao, cardapio)

    if not retorno:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Erro ao cadastrar produto')

    return retorno


@produtos.put('/produto/{id}')
async def alterar_produto(codigo: str, nome: str, descricao: str, preco: float, restricao: str,
    cardapio: str, repProduto: RepositorioProduto = Depends(obter_repo_produto)):

    consulta = repProduto.consultar_produto(codigo)

    if not consulta:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Produto não encontrado')

    retorno = repProduto.alterar_produto(codigo, nome, descricao, preco, restricao, cardapio)

    if not retorno:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Erro ao alterar produto')

    return repProduto.consultar_produto(codigo)


@produtos.delete('/produto/{id}')
async def deletar_produto(codigo: str,
    repProduto: RepositorioProduto = Depends(obter_repo_produto)):

    consulta = repProduto.consultar_produto(codigo)

    if not consulta:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Produto não encontrado')

    retorno = repProduto.deletar_produto(codigo)

    if not retorno:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Erro ao deletar produto')

    return consulta


@produtos.patch('/produto/{id}')
async def alterar_preco_produto(id: int, preco: dtos.Descricao):
    if id in db.produtos:
        db.produtos[id]['preco'] = preco.preco
        return db.produtos[id]
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Produto não cadastrado')
