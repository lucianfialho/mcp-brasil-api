from pydantic import BaseModel, constr, Field
from typing import Literal, Optional

class ConsultarCepInput(BaseModel):
    cep: constr(min_length=8, max_length=8, pattern=r'^\d{8}$')

class ConsultarTaxaInput(BaseModel):
    sigla: Literal["SELIC", "CDI", "IPCA", "IGPM", "POUPANCA", "DOLAR"] | str = Field(
        ...,
        description="Sigla da taxa ou índice oficial (ex: 'SELIC', 'CDI', 'IPCA').",
        min_length=1,
        max_length=20
    )

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
    """
    Modelo de entrada para listar veículos FIPE por marca e tipo.
    """
    tipo_veiculo: Literal["caminhoes", "carros", "motos"] = Field(
        ...,
        description="Tipo de veículo para listar os modelos (ex: 'carros', 'motos', 'caminhoes')."
    )
    codigo_marca: int = Field(
        ...,
        description="Código da marca FIPE. Pode ser obtido com 'listar_marcas_fipe'."
    )
    tabela_referencia: Optional[int] = Field(
        None,
        description="Código da tabela FIPE de referência (opcional). Se omitido, usará a tabela atual. Pode ser obtido com 'listar_tabelas_fipe'."
    )
