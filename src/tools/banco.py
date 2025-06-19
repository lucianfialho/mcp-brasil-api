"""
Ferramenta para consulta de cambio
"""

from typing import Dict, Any
from ..utils.api import make_request
from ..utils.formatters import format_data
from ..exceptions import (
    BrasilAPINotFoundError,
    BrasilAPIInvalidRequestError,
    BrasilAPIServiceUnavailableError,
    BrasilAPIUnknownError,
)

async def get_lista_banco() -> Dict[str, Any]:
    """
    Obtém informações de bancos brasileiros.

    Returns:
        Dicionário com a lista de bancos.

    Raises:
        BrasilAPIServiceUnavailableError: Se a Brasil API estiver indisponível (HTTP 5xx) ou houver erro de rede.
        BrasilAPIUnknownError: Para outros erros inesperados.
    """
    return await make_request("lista_banco")

async def get_banco_info(codigo: str) -> Dict[str, Any]:
    """
    Obtém informações de um banco brasileiro.

    Args:
        codigo (str): Código do banco para consulta.

    Returns:
        Dict[str, Any]: Informações do banco, incluindo ISPB, nome, código e nome completo.

    Raises:
        BrasilAPINotFoundError: Se o banco não for encontrado na Brasil API (HTTP 404).
        BrasilAPIInvalidRequestError: Se a requisição para a Brasil API for inválida (HTTP 400).
        BrasilAPIServiceUnavailableError: Se a Brasil API estiver indisponível (HTTP 5xx) ou houver erro de rede.
        BrasilAPIUnknownError: Para outros erros inesperados.
    """
    return await make_request("banco", codigo)
