from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import models
import schemas
from database import get_db

router = APIRouter(prefix="/livros", tags=["Livros"])


@router.post("/", response_model=schemas.LivroResponseSchema, status_code=201)
def cadastrar_livro(livro: schemas.LivroCreateSchema, db: Session = Depends(get_db)):
    novo_livro = models.Livro(**livro.model_dump())
    db.add(novo_livro)
    db.commit()
    db.refresh(novo_livro)
    return novo_livro


@router.get("/", response_model=list[schemas.LivroResponseSchema])
def listar_livros(autor: str | None = None, db: Session = Depends(get_db)):
    consulta = db.query(models.Livro)
    if autor:
        consulta = consulta.filter(models.Livro.autor.ilike(f"%{autor}%"))
    return consulta.all()