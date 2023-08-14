import dtos
from util import Utilidades
from fastapi import status, HTTPException, APIRouter, Depends
from dependencias import obter_repo_cardapio, obter_repo_produto
from repositorio_produto import RepositorioProduto
from repositorio_cardapio import RepositorioCardapio

cardapios = APIRouter()

@cardapios.get('/cardapio')
async def listar_cardapios(repCardapio: RepositorioCardapio = Depends(obter_repo_cardapio)):      
        return repCardapio.listar_cardapio()

@cardapios.get('/cardapio/{codigo}')
async def consultar_cardapio(codigo: str,
    repCardapio: RepositorioCardapio = Depends(obter_repo_cardapio)):    
    
    retorno = repCardapio.consultar_cardapio(codigo)
    
    if not retorno:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Código de cardápio não existe')
    
    return retorno


@cardapios.post('/cardapio/', status_code=status.HTTP_201_CREATED)
async def criar_cardapio(nome: str, descricao: str, util: Utilidades = Depends(Utilidades),
    repCardapio: RepositorioCardapio = Depends(obter_repo_cardapio)):

    codigo = util.criar_codigo(nome)
    retorno = repCardapio.criar_cardapio(codigo, nome, descricao)

    if not retorno:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Erro ao criar o cardápio')

    return repCardapio.consultar_cardapio(codigo)


@cardapios.put('/cardapio/{codigo}')
async def alterar_cardapio(codigo: str, nome: str, descricao: str,
    repCardapio: RepositorioCardapio = Depends(obter_repo_cardapio)):

    retorno = repCardapio.consultar_cardapio(codigo)
    
    if not retorno:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Código de cardápio inexistente')
    
    retorno = repCardapio.alterar_cardapio(codigo, nome, descricao)

    if not retorno:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Cardápio não alterado')
    
    return repCardapio.consultar_cardapio(codigo)


@cardapios.delete('/cardapio/{codigo}')
async def deletar_cardapio(codigo: str,
    repCardapio: RepositorioCardapio = Depends(obter_repo_cardapio)):

    retorno = repCardapio.consultar_cardapio(codigo)
    
    if not retorno:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Código de cardápio inexistente')

    deletado = repCardapio.deletar_cardapio(codigo)
    
    if not deletado:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Erro ao deletar cardápio')
    
    return retorno


@cardapios.patch('/cardapio/{id}')
async def alterar_descricao_cardapio(codigo: str, descricao: str,
    repCardapio: RepositorioCardapio = Depends(obter_repo_cardapio)):

    retorno = repCardapio.consultar_cardapio(codigo)
    
    if not retorno:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Código de cardápio inexistente')

    retorno = repCardapio.alterar_descricao_cardapio(codigo, descricao)

    if not retorno:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Erro ao alterar a descrição do cardápio')
    
    return retorno