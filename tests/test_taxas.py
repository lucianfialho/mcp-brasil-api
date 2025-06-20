import pytest
from pydantic import ValidationError
from src.tools.taxas import get_taxa_info
from src.tools.schemas import ConsultarTaxaInput
from src.exceptions import (
    BrasilAPINotFoundError,
    BrasilAPIInvalidRequestError,
    BrasilAPIServiceUnavailableError,
    BrasilAPIUnknownError,
)

import asyncio

@pytest.mark.asyncio
async def test_get_taxa_info_success(monkeypatch):
    async def mock_make_request(api, sigla):
        return {"nome": "SELIC", "valor": 10.75}
    monkeypatch.setattr("src.utils.api.make_request", mock_make_request)
    result = await get_taxa_info("SELIC")
    assert result["nome"] == "SELIC"
    assert "valor" in result

@pytest.mark.asyncio
async def test_get_taxa_info_not_found(monkeypatch):
    async def mock_make_request(api, sigla):
        raise BrasilAPINotFoundError()
    monkeypatch.setattr("src.utils.api.make_request", mock_make_request)
    with pytest.raises(BrasilAPINotFoundError):
        await get_taxa_info("FAKE")

@pytest.mark.asyncio
async def test_get_taxa_info_invalid_request(monkeypatch):
    async def mock_make_request(api, sigla):
        raise BrasilAPIInvalidRequestError()
    monkeypatch.setattr("src.utils.api.make_request", mock_make_request)
    with pytest.raises(BrasilAPIInvalidRequestError):
        await get_taxa_info("")

@pytest.mark.asyncio
async def test_get_taxa_info_service_unavailable(monkeypatch):
    async def mock_make_request(api, sigla):
        raise BrasilAPIServiceUnavailableError()
    monkeypatch.setattr("src.utils.api.make_request", mock_make_request)
    with pytest.raises(BrasilAPIServiceUnavailableError):
        await get_taxa_info("SELIC")

@pytest.mark.asyncio
async def test_get_taxa_info_unknown_error(monkeypatch):
    async def mock_make_request(api, sigla):
        raise BrasilAPIUnknownError()
    monkeypatch.setattr("src.utils.api.make_request", mock_make_request)
    with pytest.raises(BrasilAPIUnknownError):
        await get_taxa_info("SELIC")

def test_consultar_taxa_input_validation():
    # Sigla válida
    input_data = ConsultarTaxaInput(sigla="SELIC")
    assert input_data.sigla == "SELIC"
    # Sigla inválida (muito longa)
    with pytest.raises(ValidationError):
        ConsultarTaxaInput(sigla="A"*21)
    # Sigla vazia
    with pytest.raises(ValidationError):
        ConsultarTaxaInput(sigla="")
