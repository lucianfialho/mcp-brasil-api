"""
Ferramenta para consulta de cambio
"""

from typing import Dict, Any
from ..utils.api import make_request
from ..utils.formatters import format_data

async def get_lista_cambio() -> Dict[str, Any]:
    """
    Obtém informações de Cambio.
       
    Returns:
        Um dicionário contendo informações relacionadas a moedas de cambio.
    """
         
    return await make_request("lista_cambio","")

async def get_cambio_info(moeda:str,data:str) -> Dict[str, Any]:
    """
    Obtém informações de Cambio comparado ao real.

    Args:
        moeda (str): A Moeda será obtida através do valor do simbolo na pesquisa get_lista_cambio . Exemplo: "USD", "EUR", etc.
        data (str): A data será obtida através do input do cliente.

    Returns:
        List[Dict[str, Any]]: lista de valores de paridade de moedas com o real brasileiro.
    """

    formatted_data = format_data(data)
         
    return await make_request("cambio",moeda,formatted_data)