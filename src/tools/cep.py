"""
Ferramenta para consulta de CEP
"""

from typing import List, Dict, Any
from ..utils.api import make_request
from ..utils.validators import is_valid_cep
from ..utils.formatters import format_cep

async def get_cep_info(cep: str) -> List[Dict[str, Any]]:
    """
    Função para obter informações sobre um CEP brasileiro.

    Args:
        cep (str): O CEP a ser consultado, no formato 'XXXXX-XXX' ou 'XXXXXXXX'.

    Returns:
        List[Dict[str, Any]]: Uma lista de dicionários contendo informações relacionadas ao CEP.

    Raises:
        ValueError: Se o CEP fornecido não estiver no formato correto.
    """
    
    formatted_cep = format_cep(cep)

    if not is_valid_cep(formatted_cep):
        raise ValueError("CEP inválido. O CEP deve ter 8 dígitos numéricos.")
    
    
    return await make_request("cep", formatted_cep)