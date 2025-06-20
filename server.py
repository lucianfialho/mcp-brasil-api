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
from src.tools.taxas import get_taxa_info
from src.tools.schemas import ConsultarTaxaInput, ListarMarcasFIPEInput, ListarVeiculosFIPEInput
from src.tools.fipe import get_tabelas_fipe, get_marcas_fipe, get_veiculos_fipe
from src.exceptions import (
    BrasilAPINotFoundError,
    BrasilAPIInvalidRequestError,
    BrasilAPIServiceUnavailableError,
    BrasilAPIUnknownError,
)

@mcp.app.exception_handler(ValidationError)
async def pydantic_validation_exception_handler(request: Request, exc: ValidationError):
    return JSONResponse(
        status_code=400,
        content={"detail": exc.errors()}
    )

@mcp.app.exception_handler(BrasilAPINotFoundError)
async def brasil_api_not_found_exception_handler(request: Request, exc: BrasilAPINotFoundError):
    return JSONResponse(
        status_code=404,
        content={"detail": str(exc) if str(exc) else "Recurso não encontrado na Brasil API. Verifique o identificador fornecido."}
    )

@mcp.app.exception_handler(BrasilAPIInvalidRequestError)
async def brasil_api_invalid_request_exception_handler(request: Request, exc: BrasilAPIInvalidRequestError):
    return JSONResponse(
        status_code=400,
        content={"detail": str(exc) if str(exc) else "Requisição inválida para a Brasil API. Verifique os dados de entrada."}
    )

@mcp.app.exception_handler(BrasilAPIServiceUnavailableError)
async def brasil_api_service_unavailable_exception_handler(request: Request, exc: BrasilAPIServiceUnavailableError):
    return JSONResponse(
        status_code=503,
        content={"detail": str(exc) if str(exc) else "O serviço da Brasil API está temporariamente indisponível. Tente novamente mais tarde."}
    )

@mcp.app.exception_handler(BrasilAPIUnknownError)
async def brasil_api_unknown_exception_handler(request: Request, exc: BrasilAPIUnknownError):
    return JSONResponse(
        status_code=500,
        content={"detail": str(exc) if str(exc) else "Ocorreu um erro interno inesperado. Por favor, tente novamente ou contate o suporte."}
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

@mcp.tool()
async def consultar_taxa_oficial(input_data: ConsultarTaxaInput):
    """
    Obtém o valor atual de uma taxa de juros ou índice oficial do Brasil.

    Args:
        input_data (ConsultarTaxaInput): Objeto contendo a sigla da taxa desejada.

    Returns:
        dict: Um dicionário contendo o nome e o valor da taxa/índice.

    Raises:
        ValidationError: Se a sigla fornecida não estiver no formato correto.
        BrasilAPINotFoundError: Se a taxa/índice não for encontrado.
        BrasilAPIInvalidRequestError: Se a requisição para a Brasil API for inválida.
        BrasilAPIServiceUnavailableError: Se o serviço da Brasil API estiver indisponível.
        BrasilAPIUnknownError: Para outros erros inesperados.
    """
    return await get_taxa_info(input_data.sigla)

@mcp.tool()
async def listar_tabelas_fipe():
    """
    Lista todas as tabelas de referência disponíveis para consulta na Tabela FIPE.

    Returns:
        list: Uma lista de dicionários, cada um contendo o código e o mês da tabela de referência.

    Raises:
        BrasilAPIServiceUnavailableError: Se o serviço da Brasil API estiver indisponível.
        BrasilAPIUnknownError: Para outros erros inesperados.
    """
    return await get_tabelas_fipe()

@mcp.tool()
async def listar_marcas_fipe(input_data: ListarMarcasFIPEInput):
    """
    Lista as marcas de veículos disponíveis na Tabela FIPE para um tipo de veículo específico.

    Args:
        input_data (ListarMarcasFIPEInput): Objeto contendo o tipo de veículo e, opcionalmente, o código da tabela de referência.

    Returns:
        list: Uma lista de dicionários, cada um representando uma marca FIPE com 'nome' e 'valor'.

    Raises:
        ValidationError: Se os parâmetros fornecidos não forem válidos.
        BrasilAPINotFoundError: Se o tipo de veículo ou a tabela não for encontrada na Brasil API.
        BrasilAPIInvalidRequestError: Se a requisição para a Brasil API for inválida.
        BrasilAPIServiceUnavailableError: Se o serviço da Brasil API estiver indisponível.
        BrasilAPIUnknownError: Para outros erros inesperados.
    """
    return await get_marcas_fipe(input_data.tipo_veiculo, input_data.tabela_referencia)

@mcp.tool()
async def listar_veiculos_fipe(input_data: ListarVeiculosFIPEInput):
    """
    Lista os modelos de veículos FIPE para uma marca e tipo de veículo específicos.

    Args:
        input_data (ListarVeiculosFIPEInput): Objeto contendo tipo_veiculo, codigo_marca e tabela_referencia (opcional).

    Returns:
        list: Uma lista de dicionários, cada um representando um modelo FIPE.

    Raises:
        ValidationError: Se os parâmetros fornecidos não forem válidos.
        BrasilAPINotFoundError: Se a marca, tipo de veículo ou tabela não for encontrada na Brasil API.
        BrasilAPIInvalidRequestError: Se a requisição para a Brasil API for inválida.
        BrasilAPIServiceUnavailableError: Se o serviço da Brasil API estiver indisponível.
        BrasilAPIUnknownError: Para outros erros inesperados.
    """
    return await get_veiculos_fipe(
        input_data.tipo_veiculo,
        input_data.codigo_marca,
        input_data.tabela_referencia
    )

if __name__ == "__main__":
    mcp.run()