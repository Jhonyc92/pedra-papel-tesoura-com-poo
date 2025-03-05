# Importa o módulo random para gerar números aleatórios, que serão usados para a escolha do computador
import random

# Define a classe JogoPedraPapelTesoura, que encapsulará toda a lógica do jogo
class JogoPedraPapelTesoura:

    # Método construtor (__init__) que é chamado automaticamente quando 
    # uma nova instância da classe é criada
    def __init__(self):

        # Inicializa a pontuação do jogador com 0
        # Este atributo irá armazenar os pontos acumulados pelo jogador durante o jogo
        self.pontuacao_jogador = 0

        # Inicializa a pontuação do computador com 0
        # Este atributo irá armazenar os pontos acumulados pelo computador durante o jogo
        self.pontuacao_computador = 0

        # Inicializa uma lista com as possíveis escolhas do jogo: 'Pedra', 'Papel' e 'Tesoura'
        # Este atributo será usado para validar e comparar as escolhas do jogador e do computador
        self.escolhas = ['Pedra', 'Papel', 'Tesoura']
        
    # Define um método para obter a escolha do jogador
    def obter_escolha_jogador(self):

        # Imprime as opções disponíveis para o jogador escolher
        print("\n1. Pedra")
        print("2. Papel")
        print("3. Tesoura")

        # Solicita a escolha do jogador através do input e converte para um inteiro
        escolha = int(input("Escolha sua opção (1, 2 ou 3): "))

        # Retorna a escolha do jogador como uma string, convertendo o número 
        # escolhido para o equivalente na lista 'self.escolhas'
        # Subtrai 1 porque as listas em Python são indexadas a partir de 0
        return self.escolhas[escolha - 1]
    
    # Define um método para obter a escolha do computador
    def obter_escolha_computador(self):

        # Utiliza a função 'choice' do módulo 'random' para 
        # escolher aleatoriamente 
        # uma opção da lista 'self.escolhas'
        return random.choice(self.escolhas)
    
    # Define um método para determinar o vencedor do jogo
    def determinar_vencedor(self, escolha_jogador, escolha_computador):
        
        # Imprime a escolha feita pelo jogador
        print(f"Você escolheu {escolha_jogador}")

        # Imprime a escolha feita pelo computador
        print(f"O computador escolheu {escolha_computador}")
        
        # Verifica se as escolhas são iguais, o que resulta em um empate
        if escolha_jogador == escolha_computador:
            print("É um empate!")

        # Verifica se o jogador ganhou utilizando operadores lógicos para combinar várias condições
        # As condições são as regras do jogo: Pedra ganha de Tesoura, Papel ganha de Pedra, Tesoura ganha de Papel
        elif (escolha_jogador == 'Pedra' and escolha_computador == 'Tesoura') or \
             (escolha_jogador == 'Papel' and escolha_computador == 'Pedra') or \
             (escolha_jogador == 'Tesoura' and escolha_computador == 'Papel'):

            # Se o jogador ganhou, imprime uma mensagem e incrementa a pontuação do jogador em 1
            print("Você ganhou!")
            self.pontuacao_jogador += 1

        # Se nenhum dos casos acima se aplica, o jogador perdeu
        else:

            # Imprime uma mensagem informando que o jogador perdeu e incrementa a
            # pontuação do computador em 1
            print("Você perdeu!")
            self.pontuacao_computador += 1
            
    # Define um método para exibir a pontuação atual do jogo
    def exibir_pontuacao(self):
        
        # Imprime a pontuação atual do jogador e do computador
        print(f"Pontuação: Você {self.pontuacao_jogador} x Computador {self.pontuacao_computador}")
        
    
    # Define o método principal para executar o jogo
    def jogar(self):
        
        # Imprime uma mensagem de boas-vindas ao jogo
        print("Bem-vindo ao jogo Pedra, Papel e Tesoura!")

        # Pede ao usuário para entrar com o número de rodadas que deseja jogar
        rodadas = int(input("Quantas rodadas você quer jogar? "))

        # Loop for para jogar várias rodadas; o número de rodadas é determinado pelo usuário
        for _ in range(rodadas):

            # Obtém a escolha do jogador chamando o método obter_escolha_jogador()
            escolha_jogador = self.obter_escolha_jogador()

            # Obtém a escolha do computador chamando o método obter_escolha_computador()
            escolha_computador = self.obter_escolha_computador()

            # Determina e anuncia o vencedor da rodada
            self.determinar_vencedor(escolha_jogador, escolha_computador)

            # Exibe a pontuação atual após cada rodada
            self.exibir_pontuacao()

        # Imprime uma mensagem indicando o fim do jogo
        print("Fim do jogo!")
            

# Verifica se este script é o ponto de entrada do programa
# Isso é útil para garantir que o código só será executado se este arquivo for o script principal
# e não quando for importado como um módulo
if __name__ == "__main__":

    # Cria uma nova instância da classe JogoPedraPapelTesoura
    # Isso inicializa um novo jogo, criando um novo objeto 'jogo'
    jogo = JogoPedraPapelTesoura()

    # Chama o método jogar() do objeto 'jogo'
    # Isso começa o jogo, perguntando ao usuário quantas rodadas deseja jogar,
    # coletando as escolhas do jogador e do computador, determinando o vencedor de cada rodada,
    # e atualizando e exibindo a pontuação
    jogo.jogar()
