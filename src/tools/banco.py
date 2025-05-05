"""
Ferramenta para consulta de cambio
"""

from typing import Dict, Any
from ..utils.api import make_request
from ..utils.formatters import format_data

async def get_lista_banco() -> Dict[str, Any]:
    """
    Obtém informações de um banco brasileiro."""
         
    return await make_request("lista_banco")

async def get_banco_info(codigo: str) -> Dict[str, Any]:
    """
    Obtém informações de um banco brasileiro.

    Args:
        codigo (str): Código do banco para consulta.

    Returns:
        Dict[str, Any]: Informações do banco, incluindo ISPB, nome, código e nome completo.
    """
    return await make_request("banco", codigo)
