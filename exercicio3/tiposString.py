# mostrar algumas tipagens com string agora

#string simples
myString1 = "This is a String"
print(myString1)
print(type(myString1))
print(myString1 + " is of the data type " + str(type(myString1)))

#print com concatenação de variaveis
firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)

#usando input de dados do usuário
name = input("What is your name??? ")
print(name)

#usando formatação no print para varias variáveis
color = input("What's your favorite color??? ")
animal = input("What's your favorite animal??? ")
print("{}, you like a {} {}!!!".format(name, color, animal))
