def diminutivo_word():
        word = input("Digite uma palavra na forma de diminutivo masculino padrão para convertê-la em uma forma do falar nordestino: ")
        for i in word:
            if word[-4::] == "inho":
                word2 = word [0:-4]
                word2 = ''.join((word2,'im'))
                print("A forma do diminutivo no falar nordestino", word, "é","'", word2, "'")
                break;
            else:
                print("A entrada não é um diminutivo na forma masculina padrão. Por favor, tente novamente.")
                break;

diminutivo_word()

def next():
        query = input("Deseja prosseguir? [sim/não]: ")
        while query in "sim":
            diminutivo_word()
            next()
        if query not in "sim":
            exit()

next()