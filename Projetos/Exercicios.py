
# Adcionando as entradas

def Calculo_IMC():
    Distancia = int(input("Digite a Distância:  "))
    Diametro1 = int(input("Digite o Diâmetro 1:  "))
    Diametro2 = int(input("Digite a Diametro 2:  "))

    Calculo = (Distancia)/ (Diametro1 + Diametro2)
    return float(Calculo)

Resultado = Calculo_IMC()
print(f'A interferência de Comunnicação Mágica é : {round(Resultado,2)}')




#---------------------------------------------------------------------------------------------------------------

def Calculo_Media():
    Valores = input().split()
    Tot_Participantes = int(Valores[0])
    Tot_HotDog = int(Valores[1])

    if Tot_Participantes >= 1 and Tot_Participantes <= 1000 and Tot_HotDog >= 1 and Tot_HotDog <=1000: 
        Media =  Tot_Participantes / Tot_HotDog 

    return float(Media)

Resultado = Calculo_Media()

print(round(Resultado,2))

#---------------------------------------------------------------------------------------------------------------
"""
    Desafio
Rubens quer calcular e mostrar a quantidade de litros de combustível gastos em uma viagem de carro, sendo que seu carro faz 12 KM/L.
Como ele não sabe fazer um programa que o auxilie nessa missão, ele te pede ajuda. Para efetuar o cálculo, deve-se fornecer o tempo
gasto em horas na viagem e a velocidade média durante a mesma em km/h. Assim, você conseguirá passar para Rubens qual a distância percorrida
e, em seguida, calcular quantos litros serão necessários para a viagem que ele quer fazer. Mostre o valor com 3 casas decimais após o ponto.
"""

Rendimento = 12
def Calculo_Carro():
    Dados = input("Digite o valor do tempo e da velocidade respectivamente: ").split()

    Tempo = int(Dados[0])
    Velocidade = int(Dados[1])

    if isinstance(Tempo, int) and isinstance(Velocidade, int):
        Distancia = Tempo * Velocidade

        Quantidade = Distancia / Rendimento

        return float(Quantidade)

Combustível = Calculo_Carro()

print(round(Combustível,3))

#---------------------------------------------------------------------------------------------------------------

"""
    Desafio
    Dada a letra N do alfabeto, nos diga qual a sua posição.
"""

#Definindo uma função que receberá e retornará a posição
def Numerico():
    Letra = input("Digite a letra que deseja: ").upper()    #Deixará todos as letras em maisculo

    Posicao1 = int(ord(Letra))
    Posicao2 = Posicao1 - 64
    return Posicao2

Resultado = Numerico()
print(Resultado)

#---------------------------------------------------------------------------------------------------------------
"""
Desafio
Humberto tem um papagaio muito esperto. Quando está com as duas pernas no chão, o papagaio fala em português.
Quando levanta a perna esquerda, fala em inglês. Por fim, quando levanta a direita fala em francês. Nico, amigo
de Humberto, ficou fascinado com o animal. Em sua emoção perguntou: “E quando ele levanta as duas?”. Antes que
Humberto pudesse responder, o papagaio gritou: “Aí eu caio, idiota!”.

Entrada
A entrada consiste de diversos casos de teste. Cada caso de teste consiste uma string informando qual a 
situação de levantamento de pernas do papagaio.

Saída
Para cada condição de levantamento de pernas do papagaio, imprima a linguagem que ele utilizará. 
Caso ele levante ambas as pernas, imprima “caiu”. Quebre uma linha a cada caso de teste.
"""

while True: 
    try: 
        Ordem = input().lower()

        if Ordem == "esquerda":
            print("ingles")

        elif Ordem == "direita":
            print("frances")

        elif Ordem == "nenhuma":
            print("portugues")
        else:
            print("caiu")


    except EOFError: 
        break

#---------------------------------------------------------------------------------------------------------------
"""
    A empresa que você trabalha resolveu conceder um aumento salarial a todos funcionários, de acordo com a tabela abaixo:

    Salário	Percentual de Reajuste
    0 - 600.00
    600.01 - 900.00
    900.01 - 1500.00
    1500.01 - 2000.00
    Acima de 2000.00

    17%
    13%
    12%
    10%
    5%

Leia o salário do funcionário e calcule e mostre o novo salário, bem como o valor de reajuste ganho e o índice reajustado, em percentual.

A entrada contém apenas um valor de ponto flutuante, que pode ser maior ou igual a zero, com duas casas decimais, conforme exemplos abaixo.

Exemplo 1

Entrada	Saída
1000	Novo salario: 1120,00 
Reajuste ganho: 120,00                                                                                     
Em percentual: 12 %
 
"""

def Calculo(Salario):
    if Salario <= 600:
        Novo_Salario = (Salario*0.17) + Salario
        Reajuste = (Salario*0.17)
        Percentual = "17%"

        print(f"Novo salario: {round(Novo_Salario,2)}")
        print(f"Reajuste ganho: {round(Reajuste,2)}")
        print(f"Novo salario: {Percentual}")

    elif Salario > 600 and Salario <= 900:
        Novo_Salario = (Salario*0.13) + Salario
        Reajuste = (Salario*0.13)
        Percentual = "13%"

        print(f"Novo salario: {round(Novo_Salario,2)}")
        print(f"Reajuste ganho: {round(Reajuste,2)}")
        print(f"Novo salario: {Percentual}")

    elif Salario > 900 and Salario <= 1500:
        Novo_Salario = (Salario*0.12) + Salario
        Reajuste = (Salario*0.12)
        Percentual = "12%"

        print(f"Novo salario: {round(Novo_Salario,2)}")
        print(f"Reajuste ganho: {round(Reajuste,2)}")
        print(f"Novo salario: {Percentual}")

    elif Salario > 1500 and Salario <= 2000:
        Novo_Salario = (Salario*0.10) + Salario
        Reajuste = (Salario*0.10)
        Percentual = "10%"

        print(f"Novo salario: {round(Novo_Salario,2)}")
        print(f"Reajuste ganho: {round(Reajuste,2)}")
        print(f"Novo salario: {Percentual}")

    elif Salario > 2000:
        Novo_Salario = (Salario*0.05) + Salario
        Reajuste = (Salario*0.05)
        Percentual = "5%"

        print(f"Novo salario: {round(Novo_Salario,2)}")
        print(f"Reajuste ganho: {round(Reajuste,2)}")
        print(f"Novo salario: {Percentual}")

Calculo(int(input()))

#---------------------------------------------------------------------------------------------------------------
