from tools import metade, final, testParity



def incrementByPosition(tupla, posicao, *novo_elemento):
  """Função que adiciona um novo elemento em uma tupla em um indice desejado"""
  nova_tupla = tupla[0:posicao] + (*novo_elemento,) + tupla[posicao:len(tupla)+1]
  return nova_tupla

def incrementByHalf(tupla, posicao=0, *novo_elemento):
  """Função que adiciona um novo elemento na metade de uma tupla"""

  if len(novo_elemento,) > 0:
    posicao = 0

  if posicao == 0 and testParity(tupla)==True:
    nova_tupla = tupla[0:metade(tupla)] + (*novo_elemento,) + tupla[metade(tupla):final(tupla)]
  elif posicao == -1:
    nova_tupla = tupla[0:metade(tupla)-1] + (*novo_elemento,) + tupla[metade(tupla)-1:final(tupla)]
  elif posicao == 1:
    nova_tupla = tupla[0:metade(tupla)+1] + (*novo_elemento,) + tupla[metade(tupla)+1:final(tupla)]
  else:
    raise Exception("Se a tupla tiver um numero ímpar de elementos, indique se o novo elemento adicionado e mais para o começo ou final da tupla faça com 1 ou -1")
  return nova_tupla

def incrementInStart(tupla, *novo_elemento):
  """Função que adiciona um elemento no começo da tupla"""  
  nova_tupla = (*novo_elemento,) + tupla[0:final(tupla)]  
  return nova_tupla
