from mcp.server.fastmcp import FastMCP
from pydantic import ValidationError
from fastapi.responses import JSONResponse
from fastapi import Request

mcp = FastMCP("brasil_api")

from src.tools.cep import get_cep_info
from src.tools.cnpj import get_cnpj_info
from src.tools.ddd import get_ddd_info
from src.tools.feriados import get_feriados_info
from src.tools.cambio import get_lista_cambio, get_cambio_info
from src.tools.banco import get_lista_banco, get_banco_info

@mcp.app.exception_handler(ValidationError)
async def pydantic_validation_exception_handler(request: Request, exc: ValidationError):
    return JSONResponse(
        status_code=400,
        content={"detail": exc.errors()}
    )

@mcp.tool()
async def consultar_cep(cep: str):
    """
    Obtém informações para um CEP brasileiro.
    
    Args:
        cep (str): Código postal brasileiro (CEP) no formato 'XXXXX-XXX' ou 'XXXXXXXX'.
        
    Returns:
        dict: Um dicionário contendo informações relacionadas ao CEP fornecido.
        
    Raises:
        ValidationError: Se o CEP fornecido não estiver no formato correto.
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
async def consultar_banco():
    """
    Obtém informações de um banco brasileiro.
        
    Returns:
        dict: Um dicionário contendo informações relacionadas ao banco fornecido.
    """
    return await get_lista_banco()

@mcp.tool()
async def consultar_banco_info(codigo: str):
    """
    Obtém informações de um banco específico pelo código.
    
    Args:
        codigo (str): Código do banco
        
    Returns:
        dict: Retorna dados de um banco específico, incluindo ISPB, nome, código e nome completo.
    """
    return await get_banco_info(codigo)

@mcp.tool()
async def consultar_cambio():
    """
    Obtém informações de uma lista de moedas de cambio.
    
    Returns:
        dict: Um dicionário contendo informações relacionadas a moedas de cambio.
    """
    return await get_lista_cambio()

@mcp.tool()
async def consultar_cambio_info(moeda: str, data: str):
    """
    Obtém informações de Cambio comparado ao real.
    
    Args:
        moeda (str): A Moeda será obtida através do valor do símbolo na pesquisa get_lista_cambio. Exemplo: "USD", "EUR", etc.
        data (str): A data será obtida através do input do cliente.
        
    Returns:
        dict: Um dicionário contendo informações relacionadas a moedas de cambio comparadas ao real brasileiro.
    """
    return await get_cambio_info(moeda, data)

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

if __name__ == "__main__":
    mcp.run()