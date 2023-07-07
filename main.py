# O main.py e o arquivo principal do meu projeto
# Onde iremos executa-lo diretamente e iremos 
# Importar funções e recursos de outros modulos.

import modulo_prog

## Importando de forma restriiva os recursos de um pacote

from pacote.prog1 import var1,listacarros,calculopercentual
from pacote.prog2 import listapares


modulo_prog.calculamaior(1,4,100)

print(modulo_prog.soma(5,4))

print(var1)

print(calculopercentual(1000,10))

print(listacarros)

listapares(41)

