#atividade_1
'''valor1 = int(input("Me diga o primeiro valor: \n--> "))
valor2 = int(input("Me diga o segundo valor: \n--> "))
if valor1 == valor2:
    print("Informe valores diferentes!!!")
elif valor1 > valor2:
    print(f"o valor {valor1} é maior que o valor {valor2}.")
else:
    print(f"o valor {valor2} é maior que o valor {valor1}.")'''

#atividade_2
'''ano = int(input("Em que ano você nasceu?\n--> "))
idade = 2025 - ano
if idade <= 16:
    print("Não pode votar!!!")
else:
    print("Pode votar!!!")'''

#atividade_3
'''senha = 1234
password = int(input("Me diga sua senha: "))
if password == senha:
    print("Bem-Vindo de volta, Acesso Liberado!!!")
else:
    print("Acesso Negado!!!")'''

#atividade_4
'''quantidade = int(input("Diga a quantidade de maçãs: "))
if quantidade >= 12:
    preco = 0.25
else:
    preco = 0.3
total = quantidade*preco
print(f"Voce pagará R${preco:.2f} por maçã, totalizando R${total:.2f}")'''

#atividade_5
'''a = int(input("Me diga o primeiro valor: "))
b = int(input("Me diga o segundo valor: "))
c = int(input("Me diga o terceiro valor: "))
maior = a
if b > maior:
    maior = b
if c > maior:
    maior = c
menor = a
if b < menor:
    menor = b
if c < menor:
    menor = c
meio = a + b + c - maior - menor
print(menor,meio,maior)'''

#atividade_6
'''altura = float(input("Diga sua altura: "))
genero = input("Digite 'masculino' ou 'feminino': ")
if genero == 'masculino':
    peso_ideal = 72.7 * altura - 58
else:
    peso_ideal = 62.1*altura - 44.7
print(f"O peso ideal para pessoas do genero {genero} e altura de {altura} é {peso_ideal:.2f}kg")'''

#atividade_7_e_8
'''lados = int(input("Diga a qtd de lados: "))
medida = float(input("Diga a medida do lado: "))
if lados < 3:
    print("Não é um polígono!!")
elif lados == 3:
    perimetro = lados*medida
    print(f"Triângulo de perímetro {perimetro}")
elif lados == 4:
    perimetro = lados * medida
    print(f"Quadrado de perímetro {perimetro}")
elif lados == 5:
    perimetro = lados * medida
    print(f"Pentágono de perímetro {perimetro}")
else:
    print("Polígono não identificado!")'''

#atividade_9
'''a = int(input("Diga o primeiro numero: "))
b = int(input("Diga o segundo numero: "))
c= int(input("Diga o terceiro numero: "))
if a == b and b == c:
     print("Os valores precisam ser diferentes!!!")
elif a > b and a > c:
        print(f"O {a} é o maior")
elif b > c:
    print(f"O {b} é o maior")
else:
    print(f"O {c} é o maior")'''

#atividade_10
'''lado_1 = int(input("Diga o primeiro lado: "))
lado_2 = int(input("Diga o segundo lado: "))
lado_3= int(input("Diga o terceiro lado: "))
if lado_3 == lado_2 and lado_1 == lado_3:
    print("Esse triangulo é equilatero")
elif lado_1 == lado_2 or lado_1 == lado_3 or lado_2 == lado_3:
    print("Esse triangulo é isosceles")
else:
    print("Escaleno")'''

#atividade_11
'''ang_1 = int(input("Diga o primeiro angulo: "))
ang_2 = int(input("Diga o segundo angulo: "))
ang_3= int(input("Diga o terceiro angulo: "))
if ang_1 + ang_2 + ang_3 == 180:
    if ang_1 == 90 or ang_2 == 90 or ang_3 == 90:
        print("Retângulo!!!")
    elif ang_1 > 90 or ang_2 > 90 or ang_3 > 90:
        print("Obtuso!!!")
    else:
        print("Agudo")
else:
    print("Esses angulos não formam um triangulo!!!")''' 

