import random
import string

def gerar_senhas_aleatorias(quantidade, comprimento, arquivo_saida):
    alfabeto = string.ascii_letters + string.digits  # Letras maiúsculas, minúsculas e dígitos
    with open(arquivo_saida, "w") as arquivo:
        for _ in range(quantidade):
            senha = ''.join(random.choices(alfabeto, k=comprimento))
            arquivo.write(senha + "\n")
    print(f"{quantidade} senhas geradas no arquivo '{arquivo_saida}'.")

# Configurações
quantidade_senhas = 100_000_000  # X milhão de senhas
comprimento_senha = 5        # Comprimento de cada senha
arquivo_saida = "senhas100M.txt"

# Gera o arquivo
gerar_senhas_aleatorias(quantidade_senhas, comprimento_senha, arquivo_saida)