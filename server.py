from mcp.server.fastmcp import FastMCP

# Use "mcp" como nome para a instância FastMCP
mcp = FastMCP("brasil_api")

from src.tools.cep import get_cep_info  # Ensure this module and function exist
from src.tools.cnpj import get_cnpj_info  # Ensure this module and function exist
from src.tools.cambio import get_lista_cambio  # Ensure this module and function exist

@mcp.tool()
async def consultar_cep(cep: str):
    """
    Obtém informações para um CEP brasileiro.
    
    Args:
        cep (str): Código postal brasileiro (CEP) no formato 'XXXXX-XXX' ou 'XXXXXXXX'.
        
    Returns:
        dict: Um dicionário contendo informações relacionadas ao CEP fornecido.
        
    Raises:
        ValueError: Se o CEP fornecido não estiver no formato correto.
    """
    return await get_cep_info(cep)  # Ensure get_cep_info is an async function

@mcp.tool()
async def consultar_cnpj(cnpj: str):
    """
    Obtém informações para um CNPJ brasileiro.
    
    Args:
        cnpj (str): Cadastro Nacional da Pessoa Jurídica (CNPJ) no formato 'XX.XXX.XXX/XXXX-XX' ou 'XXXXXXXXXXXXXX'.
    Returns:
        dict: Um dicionário contendo informações relacionadas ao CNPJ fornecido.
    """
    return await get_cnpj_info(cnpj)  # Ensure get_cnpj_info is an async function

@mcp.tool()
async def consultar_cambio():
    """
    Obtém informações de uma lista de moedas de cambio.
    
    Returns:
        dict: Um dicionário contendo informações relacionadas a moedas de cambio.
    """
    return await get_lista_cambio()  # Ensure get_cnpj_info is an async function


if __name__ == "__main__":
    mcp.run()