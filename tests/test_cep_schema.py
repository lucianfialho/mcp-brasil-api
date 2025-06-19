import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

import pytest
from pydantic import ValidationError
from src.tools.schemas import ConsultarCepInput

def test_cep_valido():
    data = ConsultarCepInput(cep="01001000")
    assert data.cep == "01001000"

def test_cep_invalido_tamanho():
    with pytest.raises(ValidationError) as exc:
        ConsultarCepInput(cep="1234567")
    assert "string_too_short" in str(exc.value)

def test_cep_invalido_letras():
    with pytest.raises(ValidationError) as exc:
        ConsultarCepInput(cep="abcdefgh")
    assert "string_pattern_mismatch" in str(exc.value)

def test_cep_invalido_caracteres_especiais():
    with pytest.raises(ValidationError) as exc:
        ConsultarCepInput(cep="12345-678")
    assert "string_too_long" in str(exc.value)
