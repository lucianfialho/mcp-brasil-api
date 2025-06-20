<<<<<<< HEAD
from pydantic import BaseModel, constr, Field
from typing import Literal, Optional
=======
from pydantic import BaseModel, constr
from typing import Optional
>>>>>>> 149fe5b (feat(fipe): adiciona modelo ListarVeiculosFIPEInput para entrada da ferramenta listar_veiculos_fipe)

class ConsultarCepInput(BaseModel):
    cep: constr(min_length=8, max_length=8, pattern=r'^\d{8}$')

<<<<<<< HEAD
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
=======
class ListarVeiculosFIPEInput(BaseModel):
    tipo_veiculo: constr(strip_whitespace=True, min_length=3)
    marca: int
    tabela_referencia: Optional[int] = None
>>>>>>> 149fe5b (feat(fipe): adiciona modelo ListarVeiculosFIPEInput para entrada da ferramenta listar_veiculos_fipe)
