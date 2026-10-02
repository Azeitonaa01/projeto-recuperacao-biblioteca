from pydantic import BaseModel, ConfigDict


class LivroCreateSchema(BaseModel):
    titulo: str
    autor: str
    ano_publicacao: int
    preco: float
    disponivel: bool = True


class LivroResponseSchema(LivroCreateSchema):
    id: int

    model_config = ConfigDict(from_attributes=True)