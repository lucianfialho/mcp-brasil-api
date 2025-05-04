"""
    Funções para comunicação com a API Brasil API
"""

import httpx
from typing import Dict, Any

from ..config import API_BASE_URL, API_PATHS, USER_AGENT

async def make_request(endpoint: str, param: str) -> Dict[str, Any]:
    """
    Função genérica para fazer requisições para a Brasil API.
    
    Args:
        endpoint: Nome do endpoint (ex: "cep", "cnpj")
        param: Parâmetro de caminho para o endpoint (ex: número do CEP ou CNPJ)
        
    Returns:
        Dict contendo a resposta da API ou mensagem de erro
    """
    path = API_PATHS.get(endpoint)
    if not path:
        return {"error": f"Endpoint desconhecido: {endpoint}"}
    
    # Constrói a URL completa com o param como path parameter
    url = f"{API_BASE_URL}{path}{param}"
    print(f"URL: {url}")
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(
                url,
                headers={"User-Agent": USER_AGENT},
            )
            
            if response.status_code == 200:
                try:
                    return response.json()
                except ValueError:
                    return {"error": "Resposta JSON inválida"}
            else:
                return {"error": f"Requisição falhou com status {response.status_code}"}
        except httpx.RequestError as e:
            return {"error": f"Erro na requisição: {str(e)}"}