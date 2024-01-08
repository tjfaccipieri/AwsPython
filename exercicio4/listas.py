# Trabalhando com listas, tuplas e dicionarios

#criando e printando a lista completa, e o tipo de dado
myFruitList = ["apple", "banana", "cherry"]
print(myFruitList)
print(type(myFruitList))

#printando valores individuais da lista
print(myFruitList[0])
print(myFruitList[1])
print(myFruitList[2])

#alterando um dos valores da lista
myFruitList[2] = "orange"
print("Agora, o ultimo valor da lista foi mudado de cherry para orange")
print(myFruitList)

#trabalhando com Tuplas
myFinalAnswerTuple = ("apple", "banana", "pineapple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))

#imprimindo dados da tupla individualmente
print(myFinalAnswerTuple[0])
print(myFinalAnswerTuple[1])
print(myFinalAnswerTuple[2])

#trabalhando com dicionarios
myFavoriteFruitDictionary = {
  "Akua" : "apple",
  "Saanvi" : "banana",
  "Paulo" : "pineapple"
}

print(myFavoriteFruitDictionary)
print(type(myFavoriteFruitDictionary))

#chamando um dado do dicionario pelo "indice"
print(myFavoriteFruitDictionary["Akua"])
print(myFavoriteFruitDictionary["Saanvi"])
print(myFavoriteFruitDictionary["Paulo"])