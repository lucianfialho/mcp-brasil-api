from typing import List

import httpx
from mcp.server.fastmcp import FastMCP

import os
import dotenv

dotenv.load_dotenv()

API_BASE_URL = "https://brasilapi.com.br/api"
API_BASE_PATH = "/cnpj/v1/"
USER_AGENT = "brasil-api/1.0"

mcp = FastMCP("brasil_api_cnpj")

async def make_request(cnpj: str) -> List:
    
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{API_BASE_URL}{API_BASE_PATH}{cnpj}",
            headers={"User-Agent": USER_AGENT},
        )
        if response.status_code == 200:
            try:
                return response.json()
            except ValueError:
                return {"error": "Invalid JSON response"}
        else:
            return {"error": f"Request failed with status {response.status_code}"}

def format_cnpj(cnpj: str) -> str:
    cnpj = cnpj.replace(".", "").replace("/", "").replace("-", "")
    return cnpj

@mcp.tool()
async def get_cnpj_info(cnpj: str) -> List:
    """Get information for a given Brazilian company registration number (CNPJ) provided in the correct format.

    Args:
        cnpj (str): The Cadastro Nacional da Pessoa Jurídica. Please provide the CNPJ in the format "XXXXXXXXXXXXXX" (without punctuation).

    Returns:
        List: A list containing the information related to the provided CNPJ.
    """

    return await make_request(cnpj)
