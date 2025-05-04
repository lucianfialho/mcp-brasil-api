from mcp.server.fastmcp import FastMCP

mcp = FastMCP("brasil_api")

from src.tools.cep import get_cep_info
from src.tools.cnpj import get_cnpj_info
from src.tools.ddd import get_ddd_info
from src.tools.feriados import get_feriados_info
from src.tools.cambio import get_lista_cambio 

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
    return await get_cep_info(cep)

@mcp.tool()
async def consultar_cnpj(cnpj: str):
    """
    Obtém informações para um CNPJ brasileiro.
    
    Args:
        cnpj (str): Cadastro Nacional da Pessoa Jurídica (CNPJ) no formato 'XX.XXX.XXX/XXXX-XX' ou 'XXXXXXXXXXXXXX'.
    Returns:
        dict: Um dicionário contendo informações relacionadas ao CNPJ fornecido.
    """
    return await get_cnpj_info(cnpj)

@mcp.tool()
async def consultar_ddd(ddd: str):
    """
    Obtém informações para um DDD brasileiro.
    
    Args:
        ddd (str): Código DDD brasileiro (ex: '11', '21', etc.).
        
    Returns:
        dict: Um dicionário contendo informações relacionadas ao DDD fornecido,
              incluindo estado e cidades atendidas.
        
    Raises:
        ValueError: Se o DDD fornecido não estiver no formato correto ou não for válido.
    """
    return await get_ddd_info(ddd)

@mcp.tool()
async def consultar_feriados(ano: str):
    """
    Obtém informações sobre os feriados nacionais brasileiros para um ano específico.
    
    Args:
        ano (str): Ano para o qual se deseja consultar os feriados (ex: '2023').
        
    Returns:
        dict: Um dicionário contendo informações sobre os feriados nacionais
              do Brasil para o ano especificado.
        
    Raises:
        ValueError: Se o ano fornecido não estiver no formato correto ou não for válido.
    """
    return await get_feriados_info(ano)

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