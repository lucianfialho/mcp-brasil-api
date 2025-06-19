class BrasilAPIError(Exception):
    """Exceção base para erros relacionados à Brasil API."""
    pass

class BrasilAPINotFoundError(BrasilAPIError):
    """Recurso não encontrado na Brasil API (HTTP 404)."""
    pass

class BrasilAPIInvalidRequestError(BrasilAPIError):
    """Requisição inválida para a Brasil API (HTTP 400) ou erro de validação de negócio."""
    pass

class BrasilAPIServiceUnavailableError(BrasilAPIError):
    """Serviço da Brasil API indisponível ou erro de servidor (HTTP 5xx)."""
    pass

class BrasilAPIUnknownError(BrasilAPIError):
    """Erro inesperado da Brasil API ou durante o processamento."""
    pass
