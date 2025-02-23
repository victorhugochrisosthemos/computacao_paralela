#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <math.h>
#include <time.h>

#define LIMITE 1000000

/*
1000 -> 1 mil
10000 -> 10 mil
100000 -> 100 mil
1000000 -> 1 milhão
10000000 -> 10 milhões
100000000 -> 100 milhões
1000000000 -> 1 bilhão (não testei ainda, demora muito)
*/

#define NUMERO_DE_THREADS 8

typedef struct {
    int start;
    int end;
    int count;
} ThreadData;

int eh_primo(int num) {
    if (num < 2) return 0;
    for (int i = 2; i <= sqrt(num); i++) {
        if (num % i == 0) return 0;
    }
    return 1;
}

// Uso de ponteiros para alocação dinâmica da memória, o terror de todo estudante
void* contador_de_primos(void* arg) {
    ThreadData* data = (ThreadData*) arg;
    data->count = 0;
    for (int i = data->start; i < data->end; i++) {
        if (eh_primo(i)) {
            data->count++;
        }
    }
    pthread_exit(NULL);
}

int main() {
    pthread_t threads[NUMERO_DE_THREADS];
    ThreadData thread_data[NUMERO_DE_THREADS];
    int chunk_size = LIMITE / NUMERO_DE_THREADS;
    clock_t start, end;
    double tempo_paralelo, tempo_sequencial;
    
    start = clock();
    for (int i = 0; i < NUMERO_DE_THREADS; i++) {
        thread_data[i].start = i * chunk_size + 1;
        thread_data[i].end = (i == NUMERO_DE_THREADS - 1) ? LIMITE : (i + 1) * chunk_size;
        pthread_create(&threads[i], NULL, contador_de_primos, &thread_data[i]);
    }
    
    int total_de_primos = 0;
    for (int i = 0; i < NUMERO_DE_THREADS; i++) {
        pthread_join(threads[i], NULL);
        total_de_primos += thread_data[i].count;
    }
    end = clock();
    tempo_paralelo = ((double)(end - start)) / CLOCKS_PER_SEC;
    
    printf("----- COM PARALELISMO -----\n");
    printf("Total de numeros primos: %d\n", total_de_primos);
    printf("Tempo de execucao: %.5f segundos\n", tempo_paralelo);

    start = clock();
    total_de_primos = 0;
    for (int i = 1; i <= LIMITE; i++) {
        if (eh_primo(i)) {
            total_de_primos++;
        }
    }
    end = clock();
    tempo_sequencial = ((double)(end - start)) / CLOCKS_PER_SEC;
    
    printf("----- SEM PARALELISMO -----\n");
    printf("Total de numeros primos: %d\n", total_de_primos);
    printf("Tempo de execucao: %.5f segundos\n", tempo_sequencial);
    
    printf("- - - - - - - - - - - - - - - - - - - -\n");
    printf("Tempo total do algoritmo: %.5f segundos\n", tempo_paralelo + tempo_sequencial);
    
    return 0;
}
