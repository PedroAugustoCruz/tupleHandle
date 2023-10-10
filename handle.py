def testLenth(tupla):
  """Função que testa se a tupla é par"""
  possibilidade = len(tupla)/2

  testa = str(possibilidade)

  apos_ponto = testa[testa.index("."):len(tupla)]      
  if apos_ponto[0:3] != ".0":
    raise Exception("Tupla não é par")
  return 




def incrementByPosition(tupla, novo_elemento, posicao):
  """Função que adiciona um novo elemento em uma tupla em um indice desejado"""
  tamanho = len(tupla)
  nova_tupla = tupla[0:posicao] + (novo_elemento,) + tupla[posicao: tamanho]
  return nova_tupla



def incrementByHalf(tupla, novo_elemento):
  """Função que adiciona um novo elemento na metade de uma tupla"""
  testLenth(tupla)
  tamanho = len(tupla)
  metade = len(tupla)//2
  nova_tupla = tupla[0:metade] + (novo_elemento,) + tupla[metade:tamanho]

  return nova_tupla