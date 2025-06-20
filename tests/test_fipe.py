import pytest
from src.tools.fipe import get_tabelas_fipe, get_marcas_fipe, get_veiculos_fipe
from src.exceptions import (
    BrasilAPINotFoundError,
    BrasilAPIInvalidRequestError,
    BrasilAPIServiceUnavailableError,
    BrasilAPIUnknownError,
)
import asyncio

@pytest.mark.asyncio
async def test_get_tabelas_fipe_success(monkeypatch):
    async def mock_make_request(*args, **kwargs):
        return [
            {"codigo": 271, "mes": "junho/2021"},
            {"codigo": 272, "mes": "julho/2021"}
        ]
    monkeypatch.setattr("src.tools.fipe.make_request", mock_make_request)
    result = await get_tabelas_fipe()
    assert isinstance(result, list)
    assert result[0]["codigo"] == 271
    assert result[0]["mes"] == "junho/2021"

@pytest.mark.asyncio
async def test_get_tabelas_fipe_service_unavailable(monkeypatch):
    async def mock_make_request(*args, **kwargs):
        raise BrasilAPIServiceUnavailableError()
    monkeypatch.setattr("src.tools.fipe.make_request", mock_make_request)
    with pytest.raises(BrasilAPIServiceUnavailableError):
        await get_tabelas_fipe()

@pytest.mark.asyncio
async def test_get_tabelas_fipe_unknown_error(monkeypatch):
    async def mock_make_request(*args, **kwargs):
        raise BrasilAPIUnknownError()
    monkeypatch.setattr("src.tools.fipe.make_request", mock_make_request)
    with pytest.raises(BrasilAPIUnknownError):
        await get_tabelas_fipe()

@pytest.mark.asyncio
async def test_get_marcas_fipe_success(monkeypatch):
    async def mock_make_request(*args, **kwargs):
        return [
            {"nome": "FIAT", "valor": 21},
            {"nome": "FORD", "valor": 22}
        ]
    monkeypatch.setattr("src.tools.fipe.make_request", mock_make_request)
    result = await get_marcas_fipe("carros")
    assert isinstance(result, list)
    assert result[0]["nome"] == "FIAT"
    assert result[1]["valor"] == 22

@pytest.mark.asyncio
async def test_get_marcas_fipe_with_tabela(monkeypatch):
    async def mock_make_request(*args, **kwargs):
        assert kwargs.get("query_params") == {"tabela_referencia": 271}
        return [{"nome": "FIAT", "valor": 21}]
    monkeypatch.setattr("src.tools.fipe.make_request", mock_make_request)
    result = await get_marcas_fipe("carros", 271)
    assert result[0]["nome"] == "FIAT"

@pytest.mark.asyncio
async def test_get_marcas_fipe_not_found(monkeypatch):
    async def mock_make_request(*args, **kwargs):
        raise BrasilAPINotFoundError()
    monkeypatch.setattr("src.tools.fipe.make_request", mock_make_request)
    with pytest.raises(BrasilAPINotFoundError):
        await get_marcas_fipe("carros")

@pytest.mark.asyncio
async def test_get_marcas_fipe_invalid_request(monkeypatch):
    async def mock_make_request(*args, **kwargs):
        raise BrasilAPIInvalidRequestError()
    monkeypatch.setattr("src.tools.fipe.make_request", mock_make_request)
    with pytest.raises(BrasilAPIInvalidRequestError):
        await get_marcas_fipe("carros")

@pytest.mark.asyncio
async def test_get_marcas_fipe_service_unavailable(monkeypatch):
    async def mock_make_request(*args, **kwargs):
        raise BrasilAPIServiceUnavailableError()
    monkeypatch.setattr("src.tools.fipe.make_request", mock_make_request)
    with pytest.raises(BrasilAPIServiceUnavailableError):
        await get_marcas_fipe("carros")

@pytest.mark.asyncio
async def test_get_marcas_fipe_unknown_error(monkeypatch):
    async def mock_make_request(*args, **kwargs):
        raise BrasilAPIUnknownError()
    monkeypatch.setattr("src.tools.fipe.make_request", mock_make_request)
    with pytest.raises(BrasilAPIUnknownError):
        await get_marcas_fipe("carros")

@pytest.mark.asyncio
async def test_get_veiculos_fipe_success(monkeypatch):
    async def mock_make_request(endpoint, tipo_veiculo, marca, query_params=None):
        assert endpoint == "veiculos_fipe"
        assert tipo_veiculo == "carros"
        assert marca == "21"
        assert query_params == {"tabela_referencia": 271}
        return [
            {"nome": "UNO MILLE", "valor": 1234},
            {"nome": "PALIO", "valor": 5678}
        ]
    monkeypatch.setattr("src.tools.fipe.make_request", mock_make_request)
    result = await get_veiculos_fipe("carros", 21, 271)
    assert isinstance(result, list)
    assert result[0]["nome"] == "UNO MILLE"
    assert result[1]["valor"] == 5678

@pytest.mark.asyncio
async def test_get_veiculos_fipe_no_tabela(monkeypatch):
    async def mock_make_request(endpoint, tipo_veiculo, marca, query_params=None):
        assert query_params is None
        return [{"nome": "UNO MILLE", "valor": 1234}]
    monkeypatch.setattr("src.tools.fipe.make_request", mock_make_request)
    result = await get_veiculos_fipe("carros", 21)
    assert result[0]["nome"] == "UNO MILLE"

@pytest.mark.asyncio
async def test_get_veiculos_fipe_not_found(monkeypatch):
    async def mock_make_request(endpoint, tipo_veiculo, marca, query_params=None):
        raise BrasilAPINotFoundError()
    monkeypatch.setattr("src.tools.fipe.make_request", mock_make_request)
    with pytest.raises(BrasilAPINotFoundError):
        await get_veiculos_fipe("carros", 21)

@pytest.mark.asyncio
async def test_get_veiculos_fipe_invalid_request(monkeypatch):
    async def mock_make_request(endpoint, tipo_veiculo, marca, query_params=None):
        raise BrasilAPIInvalidRequestError()
    monkeypatch.setattr("src.tools.fipe.make_request", mock_make_request)
    with pytest.raises(BrasilAPIInvalidRequestError):
        await get_veiculos_fipe("carros", 21)

@pytest.mark.asyncio
async def test_get_veiculos_fipe_service_unavailable(monkeypatch):
    async def mock_make_request(endpoint, tipo_veiculo, marca, query_params=None):
        raise BrasilAPIServiceUnavailableError()
    monkeypatch.setattr("src.tools.fipe.make_request", mock_make_request)
    with pytest.raises(BrasilAPIServiceUnavailableError):
        await get_veiculos_fipe("carros", 21)

@pytest.mark.asyncio
async def test_get_veiculos_fipe_unknown_error(monkeypatch):
    async def mock_make_request(endpoint, tipo_veiculo, marca, query_params=None):
        raise BrasilAPIUnknownError()
    monkeypatch.setattr("src.tools.fipe.make_request", mock_make_request)
    with pytest.raises(BrasilAPIUnknownError):
        await get_veiculos_fipe("carros", 21)
