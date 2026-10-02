from fastapi import FastAPI

import models
from database import Base, engine
from routers import livros

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="appeu - Biblioteca",
    description="API de gestão de biblioteca (livros).",
    version="1.0.0",
)

app.include_router(livros.router)


@app.get("/")
def raiz():
    return {"status": "online", "mensagem": "API da biblioteca funcionando"}