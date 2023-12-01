import time
#=======^ Loading

print('3 pra 2')

v1 = int(input('Insira o valor 01: '))
v2 = int(input('Insira o valor 02: '))
v3 = int(input('Insira o valor 03: '))

print('Ok, os numeros selecionados são: {}, {}, e {} nesta mesma ordem.'.format(v1, v2, v3))

vmin = min(v1, v2, v3)

vmax = max(v1, v2, v3)

#===============================================================================================
def loading():
    for _ in range(5):  # Altere o número para ajustar a duração do loading
        print("Carregando...", end="\r")
        time.sleep(1)  # Ajuste o tempo de espera entre cada ponto (1 segundo neste exemplo)
        print("           ", end="\r")  # Limpa a linha para o próximo ponto
        time.sleep(0.5)  # Tempo de pausa entre os pontos
#===============================================================================================

loading()

print("Leitura concluída!")

print('O menor valor entre eles é {} e o maior valor é {}.'.format(vmin, vmax))