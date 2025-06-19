"""
Ferramenta para consulta de CEP
"""

from typing import List, Dict, Any
from ..utils.api import make_request
from ..utils.formatters import format_cep
from .schemas import ConsultarCepInput
from pydantic import ValidationError
from ..exceptions import (
    BrasilAPINotFoundError,
    BrasilAPIInvalidRequestError,
    BrasilAPIServiceUnavailableError,
    BrasilAPIUnknownError,
)

async def get_cep_info(cep: str) -> List[Dict[str, Any]]:
    """
    Função para obter informações sobre um CEP brasileiro.

    Args:
        cep (str): O CEP a ser consultado, no formato 'XXXXX-XXX' ou 'XXXXXXXX'.

    Returns:
        List[Dict[str, Any]]: Uma lista de dicionários contendo informações relacionadas ao CEP.

    Raises:
        ValidationError: Se o CEP fornecido não estiver no formato correto.
        BrasilAPINotFoundError: Se o CEP não for encontrado na Brasil API (HTTP 404).
        BrasilAPIInvalidRequestError: Se a requisição para a Brasil API for inválida (HTTP 400).
        BrasilAPIServiceUnavailableError: Se o serviço da Brasil API estiver indisponível (HTTP 5xx) ou houver erro de rede.
        BrasilAPIUnknownError: Para outros erros inesperados.
    """
    # Validação com Pydantic
    ConsultarCepInput(cep=cep)
    formatted_cep = format_cep(cep)
    return await make_request("cep", formatted_cep)