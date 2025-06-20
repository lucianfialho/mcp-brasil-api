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

async def get_veiculos_fipe(tipo_veiculo: str, codigo_marca: int, tabela_referencia: Optional[int] = None) -> List[Dict[str, Any]]:
    """
    Obtém a lista de veículos FIPE para uma marca e tipo de veículo específicos.

    Args:
        tipo_veiculo (str): O tipo de veículo (ex: 'carros', 'motos', 'caminhoes').
        codigo_marca (int): Código da marca FIPE.
        tabela_referencia (Optional[int]): Código da tabela FIPE de referência (opcional).

    Returns:
        List[Dict[str, Any]]: Uma lista de dicionários, cada um representando um veículo FIPE.

    Raises:
        BrasilAPINotFoundError: Se a marca, tipo de veículo ou tabela não for encontrada.
        BrasilAPIInvalidRequestError: Se a requisição for inválida.
        BrasilAPIServiceUnavailableError: Se a Brasil API estiver indisponível.
        BrasilAPIUnknownError: Para outros erros inesperados.
    """
    query_params = {"tabela_referencia": tabela_referencia} if tabela_referencia is not None else None
    return await make_request("veiculos_fipe", tipo_veiculo, str(codigo_marca), query_params=query_params)
