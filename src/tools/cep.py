"""
Ferramenta para consulta de CEP
"""

from typing import List, Dict, Any
from ..utils.api import make_request
from ..utils.formatters import format_cep
from .schemas import ConsultarCepInput
from pydantic import ValidationError

async def get_cep_info(cep: str) -> List[Dict[str, Any]]:
    """
    Função para obter informações sobre um CEP brasileiro.

    Args:
        cep (str): O CEP a ser consultado, no formato 'XXXXX-XXX' ou 'XXXXXXXX'.

    Returns:
        List[Dict[str, Any]]: Uma lista de dicionários contendo informações relacionadas ao CEP.

    Raises:
        ValidationError: Se o CEP fornecido não estiver no formato correto.
    """
    # Validação com Pydantic
    ConsultarCepInput(cep=cep)
    formatted_cep = format_cep(cep)
    return await make_request("cep", formatted_cep)