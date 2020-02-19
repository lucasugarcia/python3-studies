def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "banana"
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]
    enforcou = False
    acertou = False

    print(letras_acertadas)

    while(not enforcou and not acertou):
        chute = input("Qual letra?")
        chute = chute.strip()

        if(len(chute) > 1):
            print("Digite apenas uma letra!")
            continue;

        posicao = 0

        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                letras_acertadas[posicao] = letra

            posicao = posicao + 1

        print(letras_acertadas)

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
