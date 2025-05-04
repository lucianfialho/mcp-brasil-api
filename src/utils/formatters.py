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

def format_data(data: str) -> str:
    """
    Formata uma data para o formato 'YYYY-MM-DD'.

    Args:
        data (str): A data a ser formatada.

    Returns:
        str: A data formatada.
    """
    if not data:
        return ""
    
    # Remove todos os caracteres não numéricos
    data = ''.join(filter(str.isdigit, data))
    
    # Verifica se a data tem 8 dígitos (DDMMAAAA)
    if len(data) != 8:
        raise ValueError("Data inválida. A data deve ter 8 dígitos numéricos.")
    
    # Formata a data para 'YYYY-MM-DD'
    return f"{data[4:8]}-{data[2:4]}-{data[0:2]}"