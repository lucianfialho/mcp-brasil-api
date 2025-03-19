from typing import List

import httpx
from mcp.server.fastmcp import FastMCP

import os
import dotenv

dotenv.load_dotenv()

API_BASE_URL = os.getenv("API_BASE_URL")
API_BASE_PATH = "/cep/v2/"
USER_AGENT = "brasil-api/1.0"

mcp = FastMCP("brasil_api_cep")

async def make_request(cep: str) -> List:
    
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{API_BASE_URL}{API_BASE_PATH}{cep}",
            headers={"User-Agent": USER_AGENT},
        )
        if response.status_code == 200:
            try:
                return response.json()
            except ValueError:
                return {"error": "Invalid JSON response"}
        else:
            return {"error": f"Request failed with status {response.status_code}"}

@mcp.tool()
async def get_cep_info(cep: str) -> List:
    """ Get information for a given Brazilian postal code (CEP).

        cep (str): Brazilian postal code (CEP) in the format 'XXXXX-XXX' or 'XXXXXXXX' .

    Returns:
        List: A list containing information related to the given CEP.

    Raises:
        ValueError: If the provided CEP is not in the correct format.
    """
    return await make_request(cep)
