"""
    Funções para formatação de dados e manipulação de strings
"""

def format_document(document: str) -> str:
    """
    Remove a formatação de um documento (CNPJ), deixando apenas dígitos.

    Args:
        document (str): O documento com ou sem formatação.

    Returns:
        str: O documento contendo apenas dígitos.
    """
    # Remove todos os caracteres não numéricos
    return ''.join(filter(str.isdigit, document))

def format_cep(cep: str) -> str:
    """
    Formata um CEP para o formato.

    Args:
        cep (str): O CEP a ser formatado.

    Returns:
        str: O CEP formatado.
    """
    if not cep:
        return ""
    
    return "".join(c for c in cep if c.isdigit())