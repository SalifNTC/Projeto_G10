# Agent0_minotauro
## Sobre o projeto:
O projeto Agent0_minotauro permite explorar a interação entre um agente e um ambiente.
O ambiente consiste num tabuleiro retangular de casas quadradas, que podem conter obstáculos, perigos ou objetivos. Para se movimentar neste ambiente, o agente pode deslocar-se em frente ou mudar de direção. O agente, dependendo da sua capacidade, pode também inspecionar o tabuleiro e as suas casas.
O agente pode usar diversos algoritmos para chegar ao seu objetivo. Para os visualizar, é possível marcar as casas com várias cores.
  
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
    ```python3 client/client.py```  

### Para correr um agente (que faz uso do cliente):  
Na linha de comandos, **a partir do diretório principal do projeto**, executar, por exemplo:  
    ```python3 client/example.py```  

## Como comandar o agente:  
**TODO**
  
## Como configurar:  
A configuração do ambiente e do agente é feita no ficheiro **config.json**, através da alteração dos valores associados a cada string.  
  
## Erros conhecidos:  
A interface gráfica do servidor bloqueia enquanto espera pela conexão do cliente. No Windows, por exemplo, é necessário fechar o programa à força caso se queira terminá-lo antes de conectar o cliente.

## Contribuidores:
 - Gil Silva
 - José Cascalho
