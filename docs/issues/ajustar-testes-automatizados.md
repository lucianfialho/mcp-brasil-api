# Ajustar testes automatizados para mocks e endpoints reais

## Problema

Os testes automatizados que dependem de mocks ou endpoints fictícios (ex: "test_endpoint") estão falhando porque:
- O endpoint não existe em `API_PATHS`, causando erro antes do mock ser chamado.
- Alguns testes de FIPE e taxas não estão utilizando corretamente o mock, resultando em chamadas reais e falhas por redirecionamento (308).

## Contexto

- Testes de schemas e validação passam normalmente.
- Testes de integração e mocks precisam ser adaptados para a estrutura real do projeto.

## Sugestão

- Refatorar os testes para usar endpoints reais do projeto ou garantir que o mock seja corretamente aplicado.
- Ajustar o tratamento de respostas 308 (redirect) na função `make_request`.
- Garantir que todos os testes de FIPE e taxas usem apenas mocks e não dependam da API real.

**Labels:** bug, testes, qualidade
