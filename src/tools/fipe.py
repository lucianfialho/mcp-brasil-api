from typing import Dict, Any, List, Optional
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

async def get_marcas_fipe(tipo_veiculo: str, tabela_referencia: Optional[int] = None) -> List[Dict[str, Any]]:
    """
    Obtém a lista de marcas de veículos FIPE para um tipo de veículo específico.

    Args:
        tipo_veiculo (str): O tipo de veículo (e.g., 'carros', 'motos', 'caminhoes').
        tabela_referencia (Optional[int]): Opcional. Código da tabela FIPE de referência.

    Returns:
        List[Dict[str, Any]]: Uma lista de dicionários, cada um representando uma marca FIPE.

    Raises:
        BrasilAPINotFoundError: Se o tipo de veículo ou tabela não for encontrado.
        BrasilAPIInvalidRequestError: Se a requisição for inválida.
        BrasilAPIServiceUnavailableError: Se a Brasil API estiver indisponível.
        BrasilAPIUnknownError: Para outros erros inesperados.
    """
    query_params = {"tabela_referencia": tabela_referencia} if tabela_referencia is not None else None
    return await make_request("marcas_fipe", tipo_veiculo, query_params=query_params)
