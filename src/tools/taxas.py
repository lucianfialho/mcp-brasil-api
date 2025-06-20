from typing import Dict, Any
from ..utils.api import make_request
from ..exceptions import (
    BrasilAPINotFoundError,
    BrasilAPIInvalidRequestError,
    BrasilAPIServiceUnavailableError,
    BrasilAPIUnknownError,
)

async def get_taxa_info(sigla: str) -> Dict[str, Any]:
    """
    Obtém informações sobre uma taxa de juros ou índice oficial do Brasil.

    Args:
        sigla (str): A sigla da taxa (ex: "SELIC", "CDI", "IPCA").

    Returns:
        Dict[str, Any]: Dicionário contendo o nome e valor da taxa.

    Raises:
        BrasilAPINotFoundError: Se a taxa não for encontrada (HTTP 404).
        BrasilAPIInvalidRequestError: Se a requisição for inválida (HTTP 400).
        BrasilAPIServiceUnavailableError: Se a Brasil API estiver indisponível (HTTP 5xx) ou houver erro de rede.
        BrasilAPIUnknownError: Para outros erros inesperados.
    """
    return await make_request("taxas", sigla)
