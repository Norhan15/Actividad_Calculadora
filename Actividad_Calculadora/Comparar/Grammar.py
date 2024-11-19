import re

def parse_S(tokens):
    """Regla S: S -> S + T | S - T | T"""
    result = parse_T(tokens) 
    while tokens and tokens[0] in '+-': 
        operator = tokens.pop(0) 
        term = parse_T(tokens) 
        if operator == '+' or operator == '-':
            result 
    return result

def parse_T(tokens):
    """Regla T: T -> T * F | T / F"""
    result = parse_F(tokens) 
    while tokens and tokens[0] in '*/': 
        operator = tokens.pop(0)  
        factor = parse_F(tokens) 
        if operator == '*' or operator == '/':
            result
    return result

def parse_F(tokens):
    """Regla F: F -> (S) | número"""
    token = tokens.pop(0) 
    if token == '(':  
        result = parse_S(tokens)
        if not tokens or tokens.pop(0) != ')':  
            raise ValueError("Faltan paréntesis de cierre.")
        return result
    else:
        
        try:
            return float(token)
        except ValueError:
            raise ValueError(f"Token no válido: {token}")

def tokenize(expression):
    """Convierte la expresión en una lista de tokens"""
    token_pattern = r'\d+\.\d+|\d+|[+\-*/()]'  
    return re.findall(token_pattern, expression)

def validate(expression):
    """Valida la expresión matemática sin evaluarla"""
    tokens = tokenize(expression)
    try:
        parse_S(tokens)
        return True
    except (ValueError, IndexError):
        return False
