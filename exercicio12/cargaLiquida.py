'''
  Script desenvolvido na maior boa vontade por: Thiago Faccipieri
  Utilizado para as aulas de Paitu do bootcamp Generation AWS Re/Start
  Janeiro-2023 :)

  Utilização desse script: Fazer o calculo para a insulina humana
'''

lsInsulin = "malwmrllpllallalwgpdpaaa"  
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"  
aInsulin = "giveqcctsicslyqlenycn"  
cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"  
insulin = bInsulin + aInsulin

pKR = {
  'y': 10.07,
  'c': 8.18,
  'k': 10.53,
  'h': 6.00,
  'r': 12.48,
  'd': 3.65,
  'e': 4.25
}

float(insulin.count('y'))

seqCount = ({x: float(insulin.count(x)) for x in ['y', 'c', 'k', 'h', 'r', 'd', 'e']})

pH = 0

netCharge = (
    +(sum({x: ((seqCount[x]*(10**pKR[x]))/((10**pH)+(10**pKR[x]))) \
    for x in ['k','h','r']}.values()))
    -(sum({x: ((seqCount[x]*(10**pH))/((10**pH)+(10**pKR[x]))) \
    for x in ['y','c','d','e']}.values())))

print('{0:.2f}'.format(pH), netCharge)
pH += 1