from pydantic import BaseModel, constr

class ConsultarCepInput(BaseModel):
    cep: constr(min_length=8, max_length=8, pattern=r'^\d{8}$')
