# Exercício 2
def is_palindrome(some_str):
    """
    Verifica se uma string é igual a si própria de trás para frente desconsiderando espaços

    Args: string

    Return: boolean
    """
    some_str = some_str.lower()
    some_str = some_str.replace(' ', '')
    return some_str == some_str[::-1]

some_str = input('digite algo: ')
if is_palindrome(some_str):
    print(f'{some_str} é uma palíndrome')
else:
    print(f'{some_str} não é uma palíndrome')