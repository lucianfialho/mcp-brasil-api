"""
    Funções para formatação de dados e manipulação de strings
"""

def format_document(document: str) -> str:
    """
    Formata um documento (CPF ou CNPJ) para o formato padrão.

    Args:
        document (str): O documento a ser formatado.

    Returns:
        str: O documento formatado.
    """
    if len(document) == 11:  # CPF
        return f"{document[:3]}.{document[3:6]}.{document[6:9]}-{document[9:]}"
    elif len(document) == 14:  # CNPJ
        return f"{document[:2]}.{document[2:5]}.{document[5:8]}/{document[8:12]}-{document[12:]}"
    else:
        raise ValueError("Invalid document length")

def format_cep(cep: str) -> str:
    """
    Formata um CEP para o formato padrão.

    Args:
        cep (str): O CEP a ser formatado.

    Returns:
        str: O CEP formatado.
    """
    if not cep:
        return ""
    
    return "".join(c for c in cep if c.isdigit())