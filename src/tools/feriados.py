"""
    Ferramenta para consulta de feriados nacionais
"""

from typing import Dict, Any
from ..utils.api import make_request
from ..utils.validators import is_valid_year
from ..exceptions import (
    BrasilAPINotFoundError,
    BrasilAPIInvalidRequestError,
    BrasilAPIServiceUnavailableError,
    BrasilAPIUnknownError,
)

async def get_feriados_info(year: str) -> Dict[str, Any]:
    """
    Obtém informações sobre os feriados nacionais brasileiros para um ano específico.
    
    Args:
        year (str): Ano para o qual se deseja consultar os feriados (ex: '2023').
        
    Returns:
        Dict[str, Any]: Um dicionário contendo informações sobre os feriados nacionais
        do Brasil para o ano especificado.
        
    Raises:
        ValueError: Se o ano fornecido não estiver no formato correto ou não for válido.
        BrasilAPINotFoundError: Se o ano não for encontrado na Brasil API (HTTP 404).
        BrasilAPIInvalidRequestError: Se a requisição para a Brasil API for inválida (HTTP 400).
        BrasilAPIServiceUnavailableError: Se a Brasil API estiver indisponível (HTTP 5xx) ou houver erro de rede.
        BrasilAPIUnknownError: Para outros erros inesperados.
    """
    # Valida o ano
    if not is_valid_year(year):
        raise ValueError("Ano inválido. O ano deve estar no formato YYYY.")

    return await make_request("feriados", year)
