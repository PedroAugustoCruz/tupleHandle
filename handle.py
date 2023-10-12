def testParity(tupla):
  """Função que testa se a tupla é par"""
  testa = str(len(tupla)/2)
  apos_ponto = testa[testa.index("."):len(tupla)]      
  if apos_ponto[0:3] != ".0":
    return False
  else:
    return True
      

# def final(tupla, novo_elemento=0):
#   """Função que acha qual é o ultimo elemento da tupla final"""
#   if testType(tupla) == True:
#     return len(tupla) + 1
#   else:
#     return len(tupla) + len(novo_elemento)
  
  
def final(tupla, novo_elemento=0):
  """Função que acha qual é o ultimo elemento da tupla final"""
  if testType(novo_elemento) == tuple:
    return len(novo_elemento) + len(tupla)
  else:
    return len(tupla) + 1

def testType(novo_elemento):
  """Função que testa se o elemento e um tipo de dado ou estrutura de dados"""
  if type(novo_elemento) == int or str or float :
    return (novo_elemento,)
  else:
    return tuple(novo_elemento,)

def incrementByPosition(tupla, novo_elemento, posicao):
  """Função que adiciona um novo elemento em uma tupla em um indice desejado"""
  nova_tupla = tupla[0:posicao] + testType(novo_elemento) + tupla[posicao:final(tupla)]
  return nova_tupla



def incrementByHalf(tupla, novo_elemento, posicao=0):
  """Função que adiciona um novo elemento na metade de uma tupla"""
  if posicao == 0 and testParity(tupla)==True:
    metade = len(tupla)//2
    nova_tupla = tupla[0:metade] + testType(novo_elemento) + tupla[metade:final(tupla)]
  elif posicao == -1:
    metade = len(tupla)//2
    nova_tupla = tupla[0:metade-1] + testType(novo_elemento) + tupla[metade-1:final(tupla)]
  elif posicao == 1:
    metade = len(tupla)//2
    nova_tupla = tupla[0:metade+1] + testType(novo_elemento) + tupla[metade+1:final(tupla)]
  else:
    raise Exception("Se a tupla tiver um numero ímpar de elementos, indique se o novo elemento adicionado e mais para o começo ou final da tupla faça com 1 ou -1")
  return nova_tupla


def incrementInStart(tupla, novo_elemento):
  """Função que adiciona um elemento no começo da tupla"""  
  nova_tupla = testType(novo_elemento) + tupla[0:final(tupla)]
  
  return nova_tupla
