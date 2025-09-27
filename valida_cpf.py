def calcula_verificador(cpf, type):
    dig=0
    last = 0
    peso=10
    if(type == 1):
        last = len(cpf) - 2
    elif(type == 2):
        last = len(cpf) - 1
        peso=11
        
    for i in range(last):
        dig+=int(cpf[i])*peso
        peso-=1
    dig%=11
    if dig <= 1:
        dig = 0
    else:
        dig = 11 - dig
    return dig

def valida_cpf(cpf):
    if len(cpf) != 14:
        return False
    if cpf[3] != '.' or cpf[7] != '.' or cpf[11] != '-':
        return False
    cpf = cpf.replace('.', '')
    cpf = cpf.replace('-', '')
    if not cpf.isdigit():
        return False
    if calcula_verificador(cpf, 1) != int(cpf[-2]):
        return False
    if calcula_verificador(cpf, 2) != int(cpf[-1]):
        return False
    if cpf == 11*cpf[0]:
        return False
    return True        

cpf = input('CPF: ')
if valida_cpf(cpf):
    print('CPF Válido')
else:
    print('CPF Inválido')