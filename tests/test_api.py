import pytest
import httpx
from unittest.mock import patch
from src.utils.api import make_request
from src.exceptions import (
    BrasilAPINotFoundError,
    BrasilAPIInvalidRequestError,
    BrasilAPIServiceUnavailableError,
    BrasilAPIUnknownError,
)

@pytest.fixture(autouse=True)
def mock_config():
    with patch('src.config.API_BASE_URL', 'https://brasilapi.com.br/api'), \
         patch('src.config.API_PATHS', {'test_endpoint': '/test/success/'}), \
         patch('src.config.USER_AGENT', 'test-agent'):
        yield

@pytest.mark.asyncio
async def test_make_request_success(httpx_mock):
    httpx_mock.add_response(url="https://brasilapi.com.br/api/test/success/success", json={"data": "ok"}, status_code=200)
    result = await make_request("test_endpoint", "success")
    assert result == {"data": "ok"}

@pytest.mark.asyncio
async def test_make_request_not_found(httpx_mock):
    httpx_mock.add_response(url="https://brasilapi.com.br/api/test/success/notfound", status_code=404)
    with pytest.raises(BrasilAPINotFoundError):
        await make_request("test_endpoint", "notfound")

@pytest.mark.asyncio
async def test_make_request_invalid_request_400_with_message(httpx_mock):
    httpx_mock.add_response(url="https://brasilapi.com.br/api/test/success/invalid", json={"message": "Parametro inválido"}, status_code=400)
    with pytest.raises(BrasilAPIInvalidRequestError) as excinfo:
        await make_request("test_endpoint", "invalid")
    assert "Parametro inválido" in str(excinfo.value)

@pytest.mark.asyncio
async def test_make_request_invalid_request_400_without_message(httpx_mock):
    httpx_mock.add_response(url="https://brasilapi.com.br/api/test/success/invalid2", status_code=400)
    with pytest.raises(BrasilAPIInvalidRequestError) as excinfo:
        await make_request("test_endpoint", "invalid2")
    assert "Erro na requisição para a Brasil API" in str(excinfo.value)

@pytest.mark.asyncio
async def test_make_request_service_unavailable_500(httpx_mock):
    httpx_mock.add_response(url="https://brasilapi.com.br/api/test/success/server_error", status_code=500)
    with pytest.raises(BrasilAPIServiceUnavailableError):
        await make_request("test_endpoint", "server_error")

@pytest.mark.asyncio
async def test_make_request_network_error(httpx_mock):
    httpx_mock.add_exception(httpx.RequestError("Network is down"))
    with pytest.raises(BrasilAPIServiceUnavailableError) as excinfo:
        await make_request("test_endpoint", "any_param")
    assert "Erro de rede ou conexão" in str(excinfo.value)

@pytest.mark.asyncio
async def test_make_request_unknown_endpoint():
    with pytest.raises(BrasilAPIInvalidRequestError) as excinfo:
        await make_request("non_existent_endpoint_internal")
    assert "Endpoint desconhecido" in str(excinfo.value)

@pytest.mark.asyncio
async def test_make_request_unexpected_error(monkeypatch):
    async def raise_unexpected(*args, **kwargs):
        raise Exception("Erro inesperado!")
    monkeypatch.setattr("httpx.AsyncClient.send", raise_unexpected)
    with pytest.raises(BrasilAPIUnknownError) as excinfo:
        await make_request("test_endpoint", "any_param")
    assert "Um erro inesperado ocorreu" in str(excinfo.value)
