import re
def diminutivo_split():
    text: str = input("Digite um breve texto, contendo ao menos duas sentenças, onde haja algum diminutivo masculino na forma padrão, para convertê-lo(s) em um falar nordestino: ")
    if "inho" in text:
        text = text.replace("inho", "im")
        sentences = re.split(r"[\.\!\?]", text)
        for sentence in sentences:
          print("Sentença convertida: ",sentence)  
    else:
        print("Seu texto não contém um diminutivo na forma masculina padrão. Por favor, tente novamente.")

diminutivo_split()