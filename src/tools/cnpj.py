"""
Ferramenta para consulta de CNPJ
"""

from typing import Dict, Any
from ..utils.api import make_request
from ..utils.formatters import format_document
from ..utils.validators import is_valid_cnpj
from ..exceptions import (
    BrasilAPINotFoundError,
    BrasilAPIInvalidRequestError,
    BrasilAPIServiceUnavailableError,
    BrasilAPIUnknownError,
)

async def get_cnpj_info(cnpj: str) -> Dict[str, Any]:
    """
    Obtém informações para um CNPJ brasileiro.
    
    Args:
        cnpj: CNPJ no formato 'XX.XXX.XXX/XXXX-XX' ou 'XXXXXXXXXXXXXX'
        
    Returns:
        Dicionário contendo informações relacionadas ao CNPJ fornecido
    
    Raises:
        BrasilAPINotFoundError: Se o CNPJ não for encontrado na Brasil API (HTTP 404).
        BrasilAPIInvalidRequestError: Se a requisição para a Brasil API for inválida (HTTP 400).
        BrasilAPIServiceUnavailableError: Se a Brasil API estiver indisponível (HTTP 5xx) ou houver erro de rede.
        BrasilAPIUnknownError: Para outros erros inesperados.
    """
    # Formatar o CNPJ removendo caracteres especiais
    formatted_cnpj = format_document(cnpj)
    
    # Validação do CNPJ
    if not is_valid_cnpj(formatted_cnpj):
        return {"error": "CNPJ inválido. Deve conter 14 dígitos válidos."}
        
    return await make_request("cnpj", formatted_cnpj)