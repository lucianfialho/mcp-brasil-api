from pydantic import BaseModel, constr, Field
from typing import Literal, Optional

class ConsultarCepInput(BaseModel):
    cep: constr(min_length=8, max_length=8, pattern=r'^\d{8}$')

class ConsultarTaxaInput(BaseModel):
    sigla: constr(min_length=1, max_length=20)

class ListarMarcasFIPEInput(BaseModel):
    tipo_veiculo: Literal["caminhoes", "carros", "motos"] = Field(
        ...,
        description="Tipo de veículo para listar as marcas (ex: 'carros', 'motos', 'caminhoes')."
    )
    tabela_referencia: Optional[int] = Field(
        None,
        description="Código da tabela FIPE de referência (opcional). Se omitido, usará a tabela atual. Pode ser obtido com 'listar_tabelas_fipe'."
    )

class ListarVeiculosFIPEInput(BaseModel):
    tipo_veiculo: Literal["caminhoes", "carros", "motos"] = Field(
        ...,
        description="Tipo de veículo para listar os modelos (ex: 'carros', 'motos', 'caminhoes')."
    )
    marca: int = Field(
        ...,
        description="Código da marca do veículo (obtido com 'listar_marcas_fipe')."
    )
    tabela_referencia: Optional[int] = Field(
        None,
        description="Código da tabela FIPE de referência (opcional). Se omitido, usará a tabela atual."
    )
