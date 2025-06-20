from pydantic import BaseModel, constr
from typing import Optional

class ConsultarCepInput(BaseModel):
    cep: constr(min_length=8, max_length=8, pattern=r'^\d{8}$')

class ListarVeiculosFIPEInput(BaseModel):
    tipo_veiculo: constr(strip_whitespace=True, min_length=3)
    marca: int
    tabela_referencia: Optional[int] = None
