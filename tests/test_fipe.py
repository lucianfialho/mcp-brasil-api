import pytest
from src.tools.fipe import get_tabelas_fipe
from src.exceptions import (
    BrasilAPIServiceUnavailableError,
    BrasilAPIUnknownError,
)
import asyncio

@pytest.mark.asyncio
async def test_get_tabelas_fipe_success(monkeypatch):
    async def mock_make_request(api):
        return [
            {"codigo": 271, "mes": "junho/2021"},
            {"codigo": 272, "mes": "julho/2021"}
        ]
    monkeypatch.setattr("src.utils.api.make_request", mock_make_request)
    result = await get_tabelas_fipe()
    assert isinstance(result, list)
    assert result[0]["codigo"] == 271
    assert result[0]["mes"] == "junho/2021"

@pytest.mark.asyncio
async def test_get_tabelas_fipe_service_unavailable(monkeypatch):
    async def mock_make_request(api):
        raise BrasilAPIServiceUnavailableError()
    monkeypatch.setattr("src.utils.api.make_request", mock_make_request)
    with pytest.raises(BrasilAPIServiceUnavailableError):
        await get_tabelas_fipe()

@pytest.mark.asyncio
async def test_get_tabelas_fipe_unknown_error(monkeypatch):
    async def mock_make_request(api):
        raise BrasilAPIUnknownError()
    monkeypatch.setattr("src.utils.api.make_request", mock_make_request)
    with pytest.raises(BrasilAPIUnknownError):
        await get_tabelas_fipe()
