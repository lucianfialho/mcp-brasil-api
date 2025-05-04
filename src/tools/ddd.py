"""
Ferramenta para consulta de DDD
"""

from typing import Dict, Any, List
from ..utils.api import make_request
from ..utils.validators import is_valid_ddd

async def get_ddd_info(ddd: str) -> Dict[str, Any]:
    """
    Obtém informações para um DDD brasileiro.
    
    Args:
        ddd (str): Código DDD brasileiro (ex: '11', '21', etc.)
        
    Returns:
        Dict[str, Any]: Um dicionário contendo informações relacionadas ao DDD fornecido,
        incluindo estado e cidades atendidas.
        
    Raises:
        ValueError: Se o DDD fornecido não estiver no formato correto ou não for válido.
    """
    # Validação do DDD
    if not is_valid_ddd(ddd):
        raise ValueError("DDD inválido. O DDD deve conter apenas números e ter entre 2 e 3 dígitos.")
        
    # Remove espaços e outros caracteres não numéricos
    ddd_cleaned = ''.join(filter(str.isdigit, ddd))
    
    return await make_request("ddd", ddd_cleaned)