import log_config
import sys
import math

from fastapi import FastAPI
from pydantic import BaseModel

from logging.config import dictConfig
from prometheus_fastapi_instrumentator import Instrumentator


dictConfig(log_config.sample_logger)

app = FastAPI()

Instrumentator().instrument(app).expose(app)

def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])


@app.get("/")
async def root():
    return {"message": "Aplicacao para teste de deployment e DevOps - Response - Clientes"}

class Cliente(BaseModel):
    id: int
    nome: str
    email: str
    endereco: str

base_dados = [
    Cliente(id=1,nome="Jose Silva", email="jose.silva@email.com",endereco="Rua dos bobos, n 0"),
    Cliente(id=2,nome="Maria Joaquina", email="maria.joaquina@email.com",endereco="Alameda dos anjos, n 1970")
]

@app.get("/clientes")
def get_todos_clientes():
    return base_dados

@app.get("/clientes/{id_usuario}")
def get_cliente_id(id_usuario: int):
    for cliente in base_dados:
        if(cliente.id == id_usuario):
            return cliente
    return{"Mensagem": "Usuario não encontrado, por favor confira os id's existentes"}

@app.post("/clientes")
def post_client(cliente: Cliente):
    base_dados.append(cliente)
    return cliente

class Data(BaseModel):
    user: str

@app.post("/payloadprint")
def payload_print(data: Data):
    raw = str(data)
    bytessize = sys.getsizeof(raw)
    converted = convert_size(bytessize)
    return("Payload recebido com sucesso, tamanho: " + converted)