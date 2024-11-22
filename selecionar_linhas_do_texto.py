def contar_linhas(arquivo):
    with open(arquivo, "r") as f:
        return sum(1 for linha in f)
    
def ler_linha_especifica(arquivo, numero_linha):
    with open(arquivo, "r") as f:
        for i, linha in enumerate(f, start=1):  # A contagem começa do 1
            if i == numero_linha:
                return linha.strip()  # Remove espaços e quebras de linha extras
    return None  # Retorna None se a linha não existir000

# Exemplo de uso:
nome_arquivo = "combinacoes_alfanumericas.txt"

# Exemplo de uso:
nome_arquivo = "senhas100M.txt"
numero_linhas = contar_linhas(nome_arquivo)
print(f"O arquivo '{nome_arquivo}' contém {numero_linhas} linhas.")

print(f"'{ler_linha_especifica(nome_arquivo, 1)}','{ler_linha_especifica(nome_arquivo, 10000000)}','{ler_linha_especifica(nome_arquivo, 20000000)}','{ler_linha_especifica(nome_arquivo, 30000000)}','{ler_linha_especifica(nome_arquivo, 40000000)}','{ler_linha_especifica(nome_arquivo, 50000000)}','{ler_linha_especifica(nome_arquivo, 60000000)}','{ler_linha_especifica(nome_arquivo, 70000000)}','{ler_linha_especifica(nome_arquivo, 80000000)}','{ler_linha_especifica(nome_arquivo, 90000000)}','{ler_linha_especifica(nome_arquivo, 100000000)}'")

'''

print(f"Linha 1: {ler_linha_especifica(nome_arquivo, 1)}")
print(f"Linha 1.000.000: {ler_linha_especifica(nome_arquivo, 1000000)}")
print(f"Linha 2.000.000: {ler_linha_especifica(nome_arquivo, 2000000)}")
print(f"Linha 3.000.000: {ler_linha_especifica(nome_arquivo, 3000000)}")
print(f"Linha 4.000.000: {ler_linha_especifica(nome_arquivo, 4000000)}")
print(f"Linha 5.000.000: {ler_linha_especifica(nome_arquivo, 5000000)}")
print(f"Linha 6.000.000: {ler_linha_especifica(nome_arquivo, 6000000)}")
print(f"Linha 7.000.000: {ler_linha_especifica(nome_arquivo, 7000000)}")
print(f"Linha 8.000.000: {ler_linha_especifica(nome_arquivo, 8000000)}")
print(f"Linha 9.000.000: {ler_linha_especifica(nome_arquivo, 9000000)}")
print(f"Linha 10.000.000: {ler_linha_especifica(nome_arquivo, 10000000)}")

'''