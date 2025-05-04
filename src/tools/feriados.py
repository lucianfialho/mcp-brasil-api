"""
    Ferramenta para consulta de feriados nacionais
"""

from typing import Dict, Any
from ..utils.api import make_request
from ..utils.validators import is_valid_year

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
    """
    # Valida o ano
    if not is_valid_year(year):
        raise ValueError("Ano inválido. O ano deve estar no formato YYYY.")

    return await make_request("feriados", year)
