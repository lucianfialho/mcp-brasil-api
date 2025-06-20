API_BASE_URL = "https://brasilapi.com.br/api"
USER_AGENT = "brasil-api/1.0"

API_PATHS = {
    "cep": "/cep/v2",
    "cnpj": "/cnpj/v1",
    "ddd": "/ddd/v1",
    "feriados": "/feriados/v1",
    "lista_cambio": "/cambio/v1/moedas",
    "cambio": "/cambio/v1/cotacao",
<<<<<<< HEAD
    "banco": "/banks/v1",
    "taxas": "/taxas/v1",
    "tabelas_fipe": "/fipe/tabelas/v1",
    "marcas_fipe": "/fipe/marcas/v1",
    "veiculos_fipe": "/fipe/veiculos/v1",
    "test_endpoint": "/test/success",  # endpoint fake para testes unitários
=======
    "lista_banco": "/banks/v1",
    "banco": "/banks/v1",
    "taxas": "/taxas/v1/",
    "tabelas_fipe": "/fipe/tabelas/v1",
    "marcas_fipe": "/fipe/marcas/v1",
    "veiculos_fipe": "/fipe/veiculos/v1",
>>>>>>> 6ad4d73
    # Add more API paths as needed
}