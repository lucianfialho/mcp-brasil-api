from pydantic import BaseModel, constr, Field
from typing import Literal

class ConsultarCepInput(BaseModel):
    cep: constr(min_length=8, max_length=8, pattern=r'^\d{8}$')

class ConsultarTaxaInput(BaseModel):
    sigla: Literal["SELIC", "CDI", "IPCA", "IGPM", "POUPANCA", "DOLAR"] | str = Field(
        ...,
        description="Sigla da taxa ou índice oficial (ex: 'SELIC', 'CDI', 'IPCA').",
        min_length=1,
        max_length=20
    )
