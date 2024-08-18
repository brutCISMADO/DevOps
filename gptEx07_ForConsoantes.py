def contar_consoantes(palavra):
    vogais = ['a', 'e', 'i', 'o', 'u']
    contador = 0
    for letra in palavra:
        if letra.isalpha() and letra.lower() not in vogais:
            contador += 1
    return contador

def main():
    palavra = input("Digite uma palavra: ")
    if not palavra.isalpha():
        print("Erro: Por favor, digite apenas letras.")
        return

    total_consoantes = contar_consoantes(palavra)
    print(f"A palavra '{palavra}' contém {total_consoantes} consoantes.")

if __name__ == "__main__":
    main()
