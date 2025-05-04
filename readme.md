# MCP Brasil API

> Plugando a Brasil API em todos os LLMs através do Model Context Protocol

## Visão Geral

MCP Brasil API é um projeto open source que disponibiliza dados da [Brasil API](https://brasilapi.com.br) através do [Model Context Protocol (MCP)](https://github.com/anthropics/anthropic-cookbook/tree/main/model_context_protocol). Funcionando como um adaptador universal (similar a uma porta USB-C para integrações de IA), este projeto transforma endpoints de dados brasileiros em serviços MCP padronizados, facilitando o acesso a informações locais por assistentes de IA, LLMs e aplicações que utilizam o padrão MCP.

## Recursos Disponíveis

- **Consulta de CEP**: Obtenha informações detalhadas de endereços a partir de um CEP
- **Consulta de CNPJ**: Recupere dados cadastrais de empresas a partir de um CNPJ
- **Consulta de DDD**: Consulte estado e cidades atendidas por um DDD brasileiro
- **Consulta de Cambio**: Consulte o cambio internacional pareado com o Real
- **Consulta de Bancos**: Consulte informações dos bancos através do nome ou codigo bancário

## Por que MCP?

Com a crescente demanda por integrações entre LLMs e dados reais, o Model Context Protocol (MCP) oferece:

- **Integração Padronizada**: Conecte diversos dados e serviços com um único protocolo
- **Escalabilidade**: Adicione ou substitua servidores MCP sem alterar a lógica do cliente
- **Segurança e Eficiência**: Gerencie integrações com melhores práticas de segurança e desempenho
- **Flexibilidade**: Permite expandir facilmente para novos endpoints da Brasil API conforme necessário

## Instalação

```bash
# Instale via pip
pip install mcp-brasil-api

# Ou clone o repositório
git clone https://github.com/lucianfialho/mcp-brasil-api
cd mcp-brasil-api
pip install -e .
```

## Configuração

Crie um arquivo `.env` baseado no `.env.example` com as seguintes configurações:

```
API_BASE_URL=https://brasilapi.com.br/api
USER_AGENT=brasil-api/1.0
```

## Uso

### Executando o servidor MCP

```bash
# Iniciar o servidor
brasil-api-mcp
```

### Configuração com Smithery

O projeto inclui configuração para Smithery, permitindo inicialização rápida:

```yaml
# Configuração em smithery.yaml
api_base_url: "https://brasilapi.com.br/api"
user_agent: "brasil-api/1.0"
```

### Exemplos de uso com cliente MCP

```python
from mcp.client import McpClient

# Conecte ao servidor MCP Brasil API
client = McpClient("http://localhost:8000")

# Liste as ferramentas disponíveis
tools = client.list_tools()
print(tools)

# Consulte um CEP
cep_info = client.invoke_tool("consultar_cep", "01001-000")
print(cep_info)

# Consulte um CNPJ
cnpj_info = client.invoke_tool("consultar_cnpj", "00.000.000/0001-91")
print(cnpj_info)

# Consulte um DDD
ddd_info = client.invoke_tool("consultar_ddd", "11")
print(ddd_info)

# Consulte um feriados
feriados_info = client.invoke_tool("consultar_feriados", "1989")
print(feriados_info)

# Consulte cotação de moedas comparadas ao Real
cambio_info = client.invoke_tool("consultar_cambio", {"moeda": "USD"}, {"data": "2025-05-02"})
print(cambio_info)

# Consulte cotação de moedas comparadas ao Real
cambio_info = client.invoke_tool("consultar_cambio", "USD", "2025-05-02")
print(cambio_info)

# Consulte informações bancárias
banco_info = client.invoke_tool("consultar_banco_info", "1")
print(banco_info)

# Consulte os feriados de um ano
feriados_info = client.invoke_tool("consultar_feriados", "2025")
print(feriados_info)

>>>>>>> 612814f (-- ajustando readme)
```

### Integração com LLMs (Claude, ChatGPT, etc.)

```python
from anthropic import Anthropic
from mcp.client import McpClient

# Configure cliente MCP
mcp_client = McpClient("http://localhost:8000")
tools = mcp_client.list_tools()

# Configure o cliente Claude com as ferramentas do MCP
anthropic = Anthropic()
response = anthropic.messages.create(
    model="claude-3-5-sonnet-20240229",
    max_tokens=1000,
    temperature=0,
    system="Você tem acesso a dados brasileiros via MCP.",
    messages=[{
        "role": "user", 
        "content": "Encontre informações sobre o CEP 01001-000"
    }],
    tools=tools  # Registra as ferramentas do MCP Brasil API
)
```

## Estrutura do Projeto

```
mcp-brasil-api/
├── src/
│   ├── tools/           # Implementações das ferramentas MCP
│   │   ├── cep.py       # Ferramenta para consulta de CEP
│   │   └── cnpj.py      # Ferramenta para consulta de CNPJ
│   ├── utils/           # Funções utilitárias
│   │   ├── api.py       # Cliente HTTP para Brasil API
│   │   ├── formatters.py # Formatação de dados
│   │   └── validators.py # Validação de dados
│   └── config.py        # Configurações da aplicação
├── server.py            # Servidor MCP principal
├── Dockerfile           # Containerização
├── pyproject.toml       # Configuração do pacote Python
└── smithery.yaml        # Configuração para Smithery
```

## Roadmap

- [x] Consulta de CEP
- [x] Consulta de CNPJ
- [x] Consulta de DDD
- [x] Suporte a câmbio
- [x] Suporte a bancos e instituições financeiras
- [x] Suporte a feriados nacionais
- [ ] Taxas e índices econômicos
- [ ] Cotações de moedas

## 🤝 Contribuições

Contribuições são bem-vindas! Por favor, leia nosso guia de contribuição antes de enviar pull requests.

1. Faça um fork do projeto
2. Crie sua branch de recurso (`git checkout -b feature/novo-recurso`)
3. Commit suas mudanças (`git commit -m 'Adiciona novo recurso'`)
4. Push para a branch (`git push origin feature/novo-recurso`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 🙏 Agradecimentos

- [Brasil API](https://brasilapi.com.br) por fornecer os dados públicos
- [MCP (Model Context Protocol)](https://github.com/anthropics/anthropic-cookbook/tree/main/model_context_protocol) por padronizar a comunicação entre modelos e fontes de dados
