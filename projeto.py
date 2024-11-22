import hashlib
import multiprocessing
import time

# Função para calcular o hash de uma senha
def sha256_hash(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Função para verificar se uma tentativa corresponde à senha alvo
def check_password(password_hash, attempt):
    return sha256_hash(attempt.strip()) == password_hash

# Função para verificar senhas em um intervalo de linhas do arquivo
def process_chunk(chunk, password_hash):
    for attempt in chunk:
        if check_password(password_hash, attempt):
            return attempt
    return None

# Função para dividir o arquivo em pedaços e realizar o ataque de dicionário
def parallel_dictionary_attack(file_path, password, num_processes):
    password_hash = sha256_hash(password)
    with open(file_path, 'r', encoding='latin-1') as f:
        attempts = f.readlines()

    # Divide as tentativas em pedaços para processamento paralelo
    chunk_size = len(attempts) // num_processes
    chunks = [attempts[i:i + chunk_size] for i in range(0, len(attempts), chunk_size)]

    # Processa os pedaços em paralelo
    with multiprocessing.Pool(num_processes) as pool:
        results = pool.starmap(process_chunk, [(chunk, password_hash) for chunk in chunks])

    # Retorna a primeira senha encontrada ou None
    return next((res for res in results if res), None)

if __name__ == "__main__":
    file_path = "senhas100M.txt"  # Caminho do arquivo de senhas

    num_processes = multiprocessing.cpu_count()  # Usa o número máximo de processos disponíveis

    print("senha; sem paralelo; com paralelo; Overhead do paralelismo; Speedup; Eficiência")

    for i in ['AwHCW','q8hF3']:
        #'AwHCW','6C6YG','0E6l0','UkMC5','LYms3','tguKO','hRv9n','ErKA9','A3OYi','959v5','q8hF3'
        target_password = i
        start_seq = time.time()
        with open(file_path, 'r', encoding='latin-1') as f:
            for line in f:
                if check_password(sha256_hash(target_password), line):
                    found_password_seq = line.strip()
                    break
            else:
                found_password_seq = None
        end_seq = time.time()

        resultado = found_password_seq
        tempo_sequencial = end_seq - start_seq

        start_par = time.time()
        found_password_par = parallel_dictionary_attack(file_path, target_password, num_processes)
        end_par = time.time()

        tempo_paralelo = end_par - start_par

        overhead = tempo_paralelo - (tempo_sequencial / num_processes)
        speedup = tempo_sequencial / tempo_paralelo
        eficiencia = speedup / num_processes

        print(f"{resultado}; {tempo_sequencial:.2f}; {tempo_paralelo:.2f}; {overhead:.2f}; {speedup:.2f}; {eficiencia:.2f}")

 