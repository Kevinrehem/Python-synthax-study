# Exercício 1
def convert_to_farenheit(temp_c):
    """
    Converte temperatura em Celsius para Farenheit

    Args: temperatura (float)

    return: temperatura convertida (float)
    """
    return 1.8*temp_c + 32

temp_c = float(input('Temperatura em ºC: '))
print(f'Temperatura em ºF: {convert_to_farenheit(temp_c)}')