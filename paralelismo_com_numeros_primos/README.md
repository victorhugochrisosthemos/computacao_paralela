### Ao tentar descobrir a quantidade de números primos de 1 até 100 milhões utilizando um algoritmo em C, o processo sequencial demorou 427,89 segundos e o processo usando paralelismo demorou 152,41 segundos

- 427,89 - 152,41 = 275,48 segundos de diferença entre um processo e outro

- 275,48 / 427,89 = 0,6438 relação entre a diferença com o processo sequencial

- 0,6438 * 100 = 64,38%

- Posso afirmar que o processo usando paralelismo é 64,38% mais rápido 
do que o sequencial nesse caso
---
- Na faculdade de Ciência da Computação, mais de uma vez mais de um professor já falou isso: “um bom programador é aquele em que programa levando em consideração os aspectos do hardware que vai rodar o seu código”. Agora, um artifício ensinado nas aulas que comprova essa afirmação de maneira bem clara é referente ao paralelismo.
- Por que o paralelismo é tão importante? Quando se fala de  paralelizar um processo busca-se com essa ação melhorar o desempenho, e sobre a questão de desempenho entende-se diminuir o tempo de processamento de um algoritmo, por exemplo. No mundo atual, certos processos não são aptos a serem paralelizados como os processos de Redes Neurais Concorrentes (RNNs) e o de Redes de Computadores devido às suas dependências sequenciais. Sobre modelos de Inteligência Artificial, ganhos em relação a desempenho foram observados no modelo Transformer e no atual modelo da DeepSeek devido a conseguirem paralelizar processos que envolvam o treinamento. Porém, em relação a Redes de Computadores as etapas de processamento parecem depender de sequência porque os dados passam por camadas (modelo OSI) de comunicação entre sistemas.
- Quantos números primos existem entre 1 e 10 mil? E de 1 até 100 milhões? Um pequeno teste que realizei para observar o paralelismo em prática foi gerar um algoritmo que conta a quantidade de números primos em um determinado range. A ideia for realizar o processo de maneira sequencial, maneira normal de processamento com uma task entregando um processo por vez ao processador, e também testei o gerenciando as threads do processador (8 threads) dividindo as tasks de 8 em 8. Então, na parte paralelizada é feito a divisão do LIMITE (rannge máximo que será procurado números primos) pela quantidade de threads configurada (8).
- As threads são componentes importantes para o entendimento da prática da computação paralela. Threads podem ser traduzidas nesse contexto como “linha de execução”, considere que em um algoritmo existe diversas linhas de comandos que devem ser executadas, threads são a menor unidade de processamento que pode ser executada de maneira independente. Uma thread pode conter mais de uma instrução a ser processada.
- Bibliotecas utilizadas no código:<br>
    --> stdio.h → Funções para interagir com o usuário<br>
    --> stdlib.h → Para manipulação da memória, conversão numérica<br>
    --> pthread.h → Para gerenciamento de threads, permitindo a execução de tarefas paralelas<br>
    --> math.h → Para funções matemáticas<br>
    --> time.h → Para manipular o tempo de processamento<br>
- Sobre a biblioteca pthread, ela é a responsável pelo paralelismo ser executado. Sabe-se que essa estrutura vem da API POSIX que padroniza a interação entre aplicações e sistemas operacionais baseados em Linux e macOS. Porém, no meu PC que roda Windows consegui fazer rodar essa biblioteca porque o meu compilador de algoritmos em C é o MinGW64, que permite a compatibilidade com funcionalidades de sistemas Linux.
- Nesse contexto do algoritmo em linguagem C, um compilador traduz o algoritmo para linguagem de máquina que aí  sim será executado em um processador.
- No meu PC, o processador possui 4 núcleos físicos e possibilidade de rodar até 8 threads. A diferença entre núcleos físicos e threads ocorre porque não necessariamente todas as partes de um núcleo físico estarão ocupadas. Em um exemplo de uma pipeline de 5 estágios de uma CPU (fetch, decode, execute, memory access e write back), no momento em que uma dessas etapas estiverem ociosas elas podem ser ocupadas por outra instrução para ser processada.
- Em experimentos realizados com um grupo de colegas de faculdade conseguimos perceber algumas questões interessantes:<br>
--> Percebemos que o desempenho do algoritmo paralelizado não melhora necessariamente conforme aumenta o número de threads, é preciso ser ajustado a relação entre núcleos físicos, clock do processador e número de threads.
<br>
--> Para um algoritmo usar paralelismo é conveniente alinhar uma quantidade de instruções suficientes nessas threads que serão paralelizadas para conseguir sobrepor o bom desempenho sobre o sobrecusto (overhead) do aparato de utilizar a biblioteca. Em testes de paralelizar ataques de força bruta (ataques de dicionário), percebemos que a simples validação booleana para saber se a senha estava correta não era maior que o sobrecusto de do algoritmo acessar uma linha de um arquivo .txt, comparar com a senha correta e ainda o custo de tempo de utilizar a biblioteca pthread <br>
--> O desempenho do algoritmo com paralelismo está diretamente relacionado com o coeficiente do cálculo entre o número de threads dividido pelo clock do processador. Observou-se que bons computadores tendo um alto número de clock tinha um desempenho inferior na velocidade do processamento se aumentasse o número de threads acima de o dobro de núcleos físicos
<br>
- Algo percebido ao ler que não usei nesse teste foi que paralelizar as vezes é necessário a sincronização dos dados depois de processados, o método pthread_join é indicado para cuidar disso. Outra questão foi sobre a uma possível disputa, pelo que eu li parece que no paralelismo, por haver compartilhamento de recursos (CPU), é possível que aja “condições de corrida” entre as instruções, para resolver essa questão pode ser usado os métodos pthread_mutex_lock e o pthread_mutex_lock
