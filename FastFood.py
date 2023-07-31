from fastapi import FastAPI
import uvicorn
import rProdutos
import rCardapios

app = FastAPI()

app.include_router(rProdutos.produtos)
app.include_router(rCardapios.cardapios)


# if __name__ == '__main__':
#     uvicorn.run("FastFood:app", port=8000, host='0.0.0.0', reload = True)
    #python -m uvicorn FastFood:app --reload --> para executar a API via terminal

#s: str
#s.isalmun()