from typing import Dict, Any, List
from ..utils.api import make_request
from ..exceptions import (
    BrasilAPINotFoundError,
    BrasilAPIInvalidRequestError,
    BrasilAPIServiceUnavailableError,
    BrasilAPIUnknownError,
)

async def get_tabelas_fipe() -> List[Dict[str, Any]]:
    """
    Obtém a lista de todas as tabelas de referência FIPE existentes.

    Returns:
        List[Dict[str, Any]]: Uma lista de dicionários, onde cada dicionário representa uma tabela FIPE com 'codigo' e 'mes'.

    Raises:
        BrasilAPIServiceUnavailableError: Se a Brasil API estiver indisponível (HTTP 5xx) ou houver erro de rede.
        BrasilAPIUnknownError: Para outros erros inesperados.
    """
    return await make_request("tabelas_fipe")
