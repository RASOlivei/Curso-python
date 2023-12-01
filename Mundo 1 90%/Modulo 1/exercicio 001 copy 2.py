import random

def eh_primo(n):
    """Verifica se um número é primo ou não."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def gerar_numero_primo():
    """Gera um número primo aleatório."""
    while True:
        num = random.randint(100, 1000000)  # Gerando um número aleatório
        if eh_primo(num):
            return num

# Exemplo de uso para gerar um número primo aleatório
numero_primo_aleatorio = gerar_numero_primo()
print("Número primo aleatório gerado:", numero_primo_aleatorio)