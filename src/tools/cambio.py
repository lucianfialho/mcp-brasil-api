"""
Ferramenta para consulta de cambio
"""

from typing import Dict, Any
from ..utils.api import make_request

async def get_lista_cambio() -> Dict[str, Any]:
    """
    Obtém informações de Cambio.
       
    Returns:
        Um dicionário contendo informações relacionadas a moedas de cambio.
    """
         
    return await make_request("lista_cambio","")