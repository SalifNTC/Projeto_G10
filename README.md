# Agent0_minotauro Algoritmo A*
## Sobre o projeto:
Na cadeira de Inteligência Artificial, do 3º Ano da Licenciatura em Informática, foi-nos
proposto a interpretação e implementação do algoritmo A* no Agente0. 
A versão utilizada neste projeto foi o Agent0_minotauro, que permite explorar a interação
entre um agente e um ambiente. Este software consiste num ambiente com um tabuleiro
onde o agente se pode movimentar. De modo a movimentar-se, o agente explora o 
tabuleiro e desloca-se em frente ou muda de direção nas respetivas casas. O agente
pode utilizar diversos algoritmos para chegar ao seu objetivo e é possível observar as casas com diversas cores.

## Sobre o algoritmo A*
O algoritmo A* é um algoritmo de pesquisa do tipo best-first, isto é, um tipo de algoritmo de 
pesquisa informada em árvore ou grafo em que os nós a expandir são os com menor 
custo com base numa função de avaliação denominada de f(n). A pesquisa diz-se 
informada pois esta função de avaliação recorre a conhecimento específico ao problema, 
ou heurísticas. No caso do algoritmo A*, f(n) é a soma do custo para chegar ao nó em questão 
(função denominada por g(n)) e uma estimativa do custo para chegar desse nó até ao 
objetivo (função conhecida como heurística ou h(n)). 
O algoritmo A* pode ser visto como uma expansão mais eficiente do algoritmo Uniform Cost Search, 
uma vez que neste último, a função de avaliação é apenas g(n). Ambos são ótimos e completos.
Pode ser também contrastado com o algoritmo Greedy Best-First Search, um algoritmo informado 
que usa apenas a função h(n) como função de avaliação, mas não é nem ótimo, nem completo. 
  
A interação entre o agente e o ambiente é comandada através de um cliente e acontece no servidor.

## Como instalar
Para correr o servidor e o cliente, o utilizador deve ter instalada a versão 3 do Python. Além do Python 3, o cliente necessita da biblioteca Pillow
  
### Instalar o Python 3:
 
**Nota: para facilitar a utilização no Windows, o Python deve ser adicionado ao PATH**  
- Windows: https://docs.python.org/3/using/windows.html  
- Mac: https://docs.python.org/3/using/mac.html  
- Linux: https://docs.python.org/3/using/unix.html#on-linux  
  
### Instalar a biblioteca Pillow:
  Após instalar o Python, executar na linha de comandos:  
    ```python3 -m pip install --upgrade pip```  
    ```python3 -m pip install --upgrade Pillow```  

## Como correr:
### Para correr o servidor:  
Na linha de comandos, **a partir do diretório principal do projeto**, executar:  
    ```python3 server/main.py```  
  
### Para correr o cliente:  
Na linha de comandos, **a partir do diretório principal do projeto**, executar:  
    ```python3 client/a_star.py```  

### Para correr um agente (que faz uso do cliente):  
Na linha de comandos, **a partir do diretório principal do projeto**, executar, por exemplo:  
    ```python3 client/example.py```  

## Como comandar o agente:  
**TODO**
  
## Como configurar:  
A configuração do ambiente e do agente é feita no ficheiro **config.json**, através da alteração dos valores associados a cada string.
Para melhor  a interação entre o utilizador e  programa formam criados vários ficheiros **config.json** que contém ambientes distintos 
para facilitar a o teste.

##Como mudar o ambiente:
1-Abrir a pasta sever 
2-Abrir o ficheiro main.py
3-Na função def main() fazer o seguinte:
    with open("nomedoficheiro.json") as config_file:
  
## Erros conhecidos:  
A interface gráfica do servidor bloqueia enquanto espera pela conexão do cliente. No Windows, por exemplo, é necessário fechar o programa à força caso se queira terminá-lo antes de conectar o cliente.

## Contribuidores:
 - Salif Henrique Faustino
 - Beatriz Silva
 - Pedro Sousa
