import os

def ctof(c):
    return c * 1.8 + 32

def ftoc(f):
    return (f - 32) * 5 / 9

def kgtolb(kg):
    return kg / 0.45359237

def lbtokg(lb):
    return lb * 0.45359237

while True:
    pergunta = float(input("Oque deseja converter:  \n 1 (temperatura) \n 2 (peso) \n 3 (tamanho) \n \n  "))

    if pergunta ==  1:
        perguntaTemp = input("Gostaria de converter como: \n  1 (Celsius para Fahrenheit) \n  2 (Fahrenheit para Celsius) \n \n  ")
        os.system('cls')
        if perguntaTemp == "1":
            valorC = float(input("Celsius to Fahrenheit: "))
            print("A temperatura é aproximadamente de: ", round(ctof(valorC), 2), "Fahrenheit")
        elif perguntaTemp == "2":
            valorF = float(input("Fahrenheit to Celsius: "))
            print("A temperatura é aproximadamente de: ", round(ftoc(valorF), 2), "Celsius")
        else:
            print("Ouve um erro nas escolhas")
    elif pergunta ==  2:
        perguntaPeso = input("Gostara de converter como: \n  1 (Quilogramas para Libras) \n  2 (Libras para Quilogramas) \n \n  ")
        if perguntaPeso == "1":
            os.system('cls')
            valorKG = float(input("Qual o peso em Quilogramas que deseja converter: "))
            print("O peso é aproximadamente de: ", round(kgtolb(valorKG), 2), "Libras")
        elif perguntaPeso == "2":
            os.system('cls')
            valorLB = float(input("Qual o peso em Libras que deseja converter: "))
            print("O peso é aproximadamente de: ", round(lbtokg(valorLB), 2), "Quilogramas")
    else:
            print("Ouve um erro nas escolhas")

    deseja = input("\n  Deseja realizar outra conversão: \n  (s/n): ")
    if deseja == "s":
        os.system('cls')
    elif deseja == "sim":
        os.system('cls')
    else:
        break
