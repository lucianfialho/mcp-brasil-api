"""
Ferramenta para consulta de CNPJ
"""

from typing import Dict, Any
from ..utils.api import make_request
from ..utils.formatters import format_document
from ..utils.validators import is_valid_cnpj

async def get_cnpj_info(cnpj: str) -> Dict[str, Any]:
    """
    Obtém informações para um CNPJ brasileiro.
    
    Args:
        cnpj: CNPJ no formato 'XX.XXX.XXX/XXXX-XX' ou 'XXXXXXXXXXXXXX'
        
    Returns:
        Dicionário contendo informações relacionadas ao CNPJ fornecido
    """
    # Formatar o CNPJ removendo caracteres especiais
    formatted_cnpj = format_document(cnpj)
    
    # Validação do CNPJ
    if not is_valid_cnpj(formatted_cnpj):
        return {"error": "CNPJ inválido. Deve conter 14 dígitos válidos."}
        
    return await make_request("cnpj", formatted_cnpj)