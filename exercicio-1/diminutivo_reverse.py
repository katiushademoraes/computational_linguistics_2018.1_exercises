#Módulo que retorna a forma do diminutivo padrão, a partir de um diminutivo masculino do falar nordestino


def diminutivo_reverse():

    reverse: str = input("Digite uma palavra, no diminutivo masculino do falar nordestino, para convertê-la na forma padrão: ")
    for i in reverse:
        if reverse[-2::] == "im":
            word = reverse[0:-2]
            word = ''.join((word, 'inho'))
            dict=open("deadjectivals.mbr.dict.txt","r")
            check=dict.read()
            dict2= open("denominals.mbr.dict.txt", "r")
            check2 = dict2.read()
            if word in check or check2:
                print("A forma padrão do diminutivo", reverse, "é", "'", word, "'")
                break;
            else:
                print("A entrada não é um diminutivo.")
                break;
        else:
            print("A entrada não é um diminutivo masculino do falar nordestino. Por favor, tente novamente.")
            break;


diminutivo_reverse()


def next():
    query = input("Deseja Prosseguir? [sim/não]: ")
    while query in "sim":
        diminutivo_reverse()
        next()
    if query not in "sim":
        exit()

next()
