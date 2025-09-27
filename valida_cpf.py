

def valida_cpf(cpf):
    if len(cpf) != 14:
        return False
    if cpf[3] != '.' or cpf[7] != '.' or cpf[11] != '-':
        return False
    cpf = cpf.replace('.', '')
    cpf = cpf.replace('-', '')
    if not cpf.isdigit():
        return False
    return True        

cpf = input('CPF: ')
if valida_cpf(cpf):
    print('CPF Válido')
else:
    print('CPF Inválido')