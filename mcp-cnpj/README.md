# mcp-cnpj

O módulo mcp-cnpj é responsável por expor uma ferramenta MCP para consulta de CNPJs brasileiros, consumindo dados da Brasil API. Ele foi desenvolvido utilizando Python, com chamadas assíncronas via HTTPX e integração com o framework FastMCP para padronizar a comunicação de ferramentas conforme o [Model Context Protocol (MCP)](https://www.anthropic.com/news/model-context-protocol).

## Visão Geral

Este módulo implementa um servidor MCP específico para consulta de CNPJs. As principais funções são:

* **Consulta de CNPJ:** Realiza requisições assíncronas à Brasil API para obter informações relacionadas ao CNPJ informado.
* **Ferramenta MCP:** A função `get_cnpj_info` é exposta como uma ferramenta MCP, permitindo que clientes se conectem e solicitem dados de CNPJ de forma padronizada.
* **Configuração via Ambiente:** O endpoint base da API é configurado por meio da variável de ambiente `API_BASE_URL`.

## Modo de Desenvolvimento

- [Debugging](https://modelcontextprotocol.io/docs/tools/debugging)
- [Inspector](https://modelcontextprotocol.io/docs/tools/inspector)
