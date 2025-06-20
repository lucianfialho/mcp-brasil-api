# Importação de modelos Pydantic no server.py

## Problema

Atualmente, o arquivo `server.py` importa explicitamente o modelo `ConsultarTaxaInput` de `src.tools.schemas` para a ferramenta MCP `consultar_taxa_oficial`, mas não faz o mesmo para outros endpoints como CEP, CNPJ, etc., que também possuem validação de entrada.

## Contexto

- A ferramenta `consultar_taxa_oficial` recebe um objeto Pydantic como parâmetro, por isso a importação explícita.
- As demais ferramentas MCP recebem tipos primitivos (ex: `cep: str`) e a validação ocorre internamente ou em outro ponto do fluxo.

## Sugestão

Padronizar o uso de modelos Pydantic para todos os endpoints MCP, tornando a validação explícita e centralizada, além de facilitar a documentação e o autocomplete.

**Labels:** melhoria, arquitetura, validação
