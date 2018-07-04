# coding: utf-8
# Módulo diminutivo_sentence
# Converte um diminutivo masculino padrão, dentro de uma sentença, para uma forma do falar nordestino.
# Melhorias na função diminutivo2, criada por João Vitor e Pedro Muniz
def diminutivo_sentence():
    sentence: str = input("Digite uma sentença, contendo um diminutivo masculino na forma padrão, para convertê-lo em um falar nordestino: ")
    if "inho" in sentence:
        sentence = sentence.replace("inho", "im")
        print("Sentença convertida: ", sentence)
    else:
        print("Sua sentença não contém um diminutivo na forma masculina padrão. Por favor, tente novamente.")

diminutivo_sentence()

def next():
    query = input("Deseja Prosseguir? [sim/não]: ")
    while query in "sim":
        diminutivo_sentence()
        next()
    if query not in "sim":
        exit()

next()
