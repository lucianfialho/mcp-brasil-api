"""
    Funções para validação de dados Brasileiros
"""

def is_valid_cep(cep: str) -> bool:
    """
    Valida um CEP (Código de Endereçamento Postal) brasileiro.

    Args:
        cep (str): O CEP a ser validado.

    Returns:
        bool: True se o CEP for válido, False caso contrário.
    """

    if not cep or len(cep) != 8 or not cep.isdigit():
        return False
    return True


def validar_cnpj(cnpj: str) -> bool:
    """
    Valida um CNPJ verificando seus dígitos verificadores.
    
    Args:
        cnpj: string com 14 dígitos (com ou sem máscara)
        
    Returns:
        True se for válido, False caso contrário
    """
    # Remove caracteres não numéricos
    cnpj = ''.join(filter(str.isdigit, cnpj))
    
    # Verifica o tamanho e se não é uma sequência de dígitos iguais
    if len(cnpj) != 14 or cnpj == cnpj[0] * 14:
        return False
    
    def calcular_digito(cnpj_parcial, pesos):
        soma = sum(int(digito) * peso for digito, peso in zip(cnpj_parcial, pesos))
        resto = soma % 11
        return '0' if resto < 2 else str(11 - resto)
    
    # Pesos para o primeiro e segundo dígitos
    pesos1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    pesos2 = [6] + pesos1
    
    # Cálculo dos dois dígitos
    digito1 = calcular_digito(cnpj[:12], pesos1)
    digito2 = calcular_digito(cnpj[:12] + digito1, pesos2)
    
    return cnpj[-2:] == digito1 + digito2


def is_valid_cnpj(cnpj: str) -> bool:
    """
    Verifica se um CNPJ brasileiro é válido matematicamente.
    Wrapper para manter compatibilidade com o código existente.
    
    Args:
        cnpj: CNPJ a ser validado, com ou sem formatação.
        
    Returns:
        True se o CNPJ é válido, False caso contrário.
    """
    return validar_cnpj(cnpj)

def is_valid_ddd(ddd: str) -> bool:
    """
    Valida um código DDD brasileiro.

    Args:
        ddd (str): O código DDD a ser validado.

    Returns:
        bool: True se o DDD for válido, False caso contrário.
    """
    # Remove qualquer caractere não-numérico
    ddd_clean = ''.join(filter(str.isdigit, ddd))
    
    # Verifica se o DDD tem entre 2 e 3 dígitos (para suportar possíveis formatos)
    if not ddd_clean or not (2 <= len(ddd_clean) <= 3) or not ddd_clean.isdigit():
        return False
        
    # Aqui poderíamos adicionar verificações adicionais para DDDs válidos no Brasil
    # Por enquanto, apenas validamos o formato
    return True

def is_valid_year(year: str) -> bool:
    """
    Valida um ano no formato YYYY.

    Args:
        year (str): O ano a ser validado.

    Returns:
        bool: True se o ano for válido, False caso contrário.
    """
    if not year or len(year) != 4 or not year.isdigit():
        return False
    return True