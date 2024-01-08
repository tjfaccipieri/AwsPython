#usar uma estrutura de FOR para printar valores e tipos

#criação da lista
myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]

#criação do FOR para printar tudo
for item in myMixedTypeList:
  print("{} iso of the data type {}".format(item, type(item)))