## Este é um modulo(programa secundario do meu projeto)
# Iremos importar seus recurso e funções
# no programa main.py

## Uma função que q calcula o maior valor de uma lista

def calculamaior(x,y,z):
    lista = [x,y,z]
    print(max(lista))

# Criar uma soma

def soma(x,y):
    return x+y

# Contexto main a função ou açaõ so sera executada se for rodado diretamente 
# no programa(script)


if __name__=='__main__':
    print(soma(2,3))
    print("Executei por aqui")