"""
Ferramenta para consulta de câmbio
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

async def get_lista_cambio() -> Dict[str, Any]:
    """
    Obtém informações de Câmbio.
       
    Returns:
        Um dicionário contendo informações relacionadas a moedas de câmbio.
    Raises:
        BrasilAPIServiceUnavailableError: Se a Brasil API estiver indisponível (HTTP 5xx) ou houver erro de rede.
        BrasilAPIUnknownError: Para outros erros inesperados.
    """
    return await make_request("lista_cambio", "")

async def get_cambio_info(moeda: str, data: str) -> Dict[str, Any]:
    """
    Obtém informações de Câmbio comparado ao real.

    Args:
        moeda (str): A Moeda será obtida através do valor do símbolo na pesquisa get_lista_cambio.
                   Exemplo: "USD", "EUR", etc.
        data (str): A data será obtida através do input do cliente.

    Returns:
        Dict[str, Any]: Dicionário contendo a cotação da moeda na data especificada.
    Raises:
        BrasilAPINotFoundError: Se a moeda não for encontrada (HTTP 404).
        BrasilAPIInvalidRequestError: Se a requisição for inválida (HTTP 400).
        BrasilAPIServiceUnavailableError: Se a Brasil API estiver indisponível (HTTP 5xx) ou houver erro de rede.
        BrasilAPIUnknownError: Para outros erros inesperados.
    """
    formatted_data = format_data(data)
    return await make_request("cambio", moeda, formatted_data)
