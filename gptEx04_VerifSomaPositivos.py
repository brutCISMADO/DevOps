# Função para exibir separadores
def exibir_separador():
    print("=" * 40)  # Imprime uma linha de 40 caracteres "="


# Função para exibir mensagem de boas-vindas
def mensagem_boas_vindas():
    print("Bem-vindo ao programa de soma de números positivos!")


# Função para calcular e exibir a soma dos números positivos
def calcular_soma_positivos():
    soma = 0  # Inicializa a soma dos números positivos

    while True:
        try:
            numero = int(
                input("Digite um número inteiro (negativo para parar): "))  # Solicita um número inteiro ao usuário

            if numero < 0:  # Condição para parar o laço
                break

            soma += numero  # Adiciona o número à soma se for positivo
        except ValueError:
            print("Entrada inválida, por favor, digite um número inteiro.")  # Mensagem de erro para entradas inválidas

    print(f"A soma dos números positivos digitados é: {soma}")  # Exibe a soma dos números positivos


# Função para agradecer e perguntar ao usuário
def agradecer_e_perguntar():
    exibir_separador()
    print("Obrigado por utilizar o script!")
    resposta = input("Você quer somar mais números? [S/N]: ").strip().upper()
    return resposta == 'S'  # Retorna True se a resposta for 'S', caso contrário, retorna False


# Função principal que executa o programa
def main():
    mensagem_boas_vindas()

    while True:
        calcular_soma_positivos()

        if not agradecer_e_perguntar():  # Condição para continuar ou parar o programa
            break

    print("Programa encerrado.")


# Chama a função principal para iniciar o programa
if __name__ == "__main__":
    main()  # Inicia o programa
