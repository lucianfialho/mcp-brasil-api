"""
    Funções para comunicação com a API Brasil API
"""

import httpx
from typing import Dict, Any

from ..config import API_BASE_URL, API_PATHS, USER_AGENT
from ..exceptions import (
    BrasilAPINotFoundError,
    BrasilAPIInvalidRequestError,
    BrasilAPIServiceUnavailableError,
    BrasilAPIUnknownError,
)

async def make_request(endpoint: str, *params: str) -> Dict[str, Any]:
    """
    Função genérica para fazer requisições para a Brasil API.
    
    Args:
        endpoint: Nome do endpoint (ex: "cep", "cnpj")
        param: Parâmetro de caminho para o endpoint (ex: número do CEP ou CNPJ)
        
    Returns:
        Dict contendo a resposta da API
    
    Raises:
        BrasilAPINotFoundError: Se o recurso não for encontrado (404)
        BrasilAPIInvalidRequestError: Se a requisição for inválida (400)
        BrasilAPIServiceUnavailableError: Se a API estiver indisponível (5xx ou erro de rede)
        BrasilAPIUnknownError: Para outros erros inesperados
    """
    path = API_PATHS.get(endpoint)
    if not path:
        raise BrasilAPIInvalidRequestError(f"Endpoint desconhecido: {endpoint}")
    
    # Junta os path params com barra, garantindo que estejam limpos e não vazios
    full_path = "/".join(str(param).strip().strip("/") for param in params if param)
    url = f"{API_BASE_URL}{path}{full_path}"

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(
                url,
                headers={"User-Agent": USER_AGENT},
            )
            
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            status = e.response.status_code
            if status == 404:
                raise BrasilAPINotFoundError(f"Recurso não encontrado na Brasil API: {e.request.url}") from e
            elif status == 400:
                try:
                    detail = e.response.json().get("message", "Requisição inválida para a Brasil API")
                except Exception:
                    detail = "Requisição inválida para a Brasil API"
                raise BrasilAPIInvalidRequestError(f"Erro na requisição para a Brasil API: {detail}") from e
            elif 500 <= status < 600:
                raise BrasilAPIServiceUnavailableError(f"Serviço da Brasil API indisponível: {status}") from e
            else:
                raise BrasilAPIUnknownError(f"Erro inesperado da Brasil API: {status}") from e
        except httpx.RequestError as e:
            raise BrasilAPIServiceUnavailableError(f"Erro de rede ou conexão ao chamar a Brasil API: {e}") from e
        except Exception as e:
            raise BrasilAPIUnknownError(f"Um erro inesperado ocorreu: {e}") from e

