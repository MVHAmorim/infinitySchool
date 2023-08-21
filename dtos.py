from pydantic import BaseModel, Field, validator
import util

class CardapioIn(BaseModel):
    nome: str = Field(min_length=2, max_length=50)
    descricao: str = Field(max_length=255)

class Cardapio(BaseModel):
    codigo: str = Field(min_length=2, max_length=50)
    nome: str = Field(min_length=2, max_length=50)
    descricao: str = Field(max_length=255)

    @validator('codigo')
    def validar_codigo(codigo: str) -> str:
        return util.Utilidades.validar_codigo(codigo)
    
class ProdutoIn(BaseModel):
    nome: str = Field(min_length=2, max_length=50)
    descricao: str = Field(max_length=255)
    preco: float = Field(ge=0)
    restricao: str = Field(min_length=2, max_length=20)
    cardapio: str = Field(min_length=2, max_length=50)

    @validator('cardapio')
    def validar_codigo(cardapio: str) -> str:
        return util.Utilidades.validar_codigo(cardapio)

class Produto(BaseModel):
    codigo: str = Field(min_length=2, max_length=50)
    nome: str = Field(min_length=2, max_length=50)
    descricao: str = Field(max_length=255)
    preco: float = Field(ge=0)
    restricao: str = Field(min_length=2, max_length=20)
    cardapio: str = Field(min_length=2, max_length=50)

class Usuario(BaseModel):
    nome_usuario: str = Field(min_length=6, max_length=20)
    nome_completo: str = Field(min_length=6, max_length=20)
    cargo: str = Field(min_length=2, max_length=20)

class Cadastro(baseModel):
    nome_completo: str = Field(min_length=6, max_length=20)
    cargo: str = Field(min_length=2, max_length=20)
    senha: SecretStr = Field(min_length=6, max_length=20) 

class BearerToken(BaseModel):
    access_token: str
    token_type: Literal['bearer'] = Field(default='bearer')


class Usuario(BaseModel):
    codigo: str = Field(min_length=2, max_length=50)
    nome: str = Field(min_length=2, max_length=50)
    descricao: str = Field(max_length=255)
    preco: float = Field(ge=0)
    restricao: str = Field(min_length=2, max_length=20)
    cardapio: str = Field(min_length=2, max_length=50)


class Preco(BaseModel):
    preco: float = Field(ge=0)

class Descricao(BaseModel):
    descricao: str = Field(max_length=255)
