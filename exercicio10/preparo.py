import re

# Abre o arquivo e lê todas as linhas
with open('exercicio10/insulina.txt', 'r') as originalFile:
  lines = originalFile.readlines()
  pass

# Remove a primeira e última linha
del lines[0]
del lines[-1]

# Para as linhas que sobraram, remove todos os números e espaços em branco
lines[0] = re.sub(r'[\d\s]', '', lines[0])
lines[1] = re.sub(r'[\d\s]', '', lines[1])


# Escreve as linhas modificadas para um novo arquivo
with open('exercicio10/insulinaFiltrada.txt', 'w') as regexFile:
  regexFile.writelines(lines)
  pass

with open('exercicio10/insulinaFiltrada.txt', 'r') as filtros:
  textoFull = filtros.readlines()
  pass

conteudo = ''.join(textoFull)

primeiraParte = conteudo[:24]
segundaParte = conteudo[24:54]
terceiraParte = conteudo[54:89]
quartaParte = conteudo[89:110]

with open('exercicio10/primeiroFiltro.txt', 'w') as primeiroFiltro:
  primeiroFiltro.write(primeiraParte)
  pass

with open('exercicio10/segundoFiltro.txt', 'w') as segundoFiltro:
  segundoFiltro.write(segundaParte)
  pass

with open('exercicio10/terceiroFiltro.txt', 'w') as terceiroFiltro:
  terceiroFiltro.write(terceiraParte)
  pass

with open('exercicio10/quartoFiltro.txt', 'w') as quartoFiltro:
  quartoFiltro.write(quartaParte)
  pass

