print('Bases Numéricas')
v =int(input('Insira un número: '))
vx = int(input('\n[1] Binário.\n[2] Octal.\n[3]Hexadecimal.\nSeleciona a  opção de conversão: \n'))
if vx == 1:
    print(bin(v)[2:])
elif vx == 2:
    print(oct(v)[2:])
elif vx == 3:
    print(hex(v)[2:])
else:
    print('Opção inválida.')