"""
    Funções para comunicação com a API Brasil API
"""

import httpx
from typing import List, Dict, Any

from ..config import API_BASE_URL, API_PATHS, USER_AGENT

async def make_request(endpoint: str, params: Dict[str, Any] = None) -> List:
    """
    Função para fazer uma requisição HTTP GET para a API Brasil API.

    Args:
        endpoint (str): O endpoint da API a ser consultado.
        params (Dict[str, Any], optional): Parâmetros adicionais para a requisição. Defaults to None.

    Returns:
        List: A lista de dados retornada pela API.
    """
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{API_BASE_URL}{API_PATHS[endpoint]}",
            headers={"User-Agent": USER_AGENT},
            params=params
        )
        if response.status_code == 200:
            try:
                return response.json()
            except ValueError:
                return {"error": "Invalid JSON response"}
        else:
            return {"error": f"Request failed with status {response.status_code}"}
