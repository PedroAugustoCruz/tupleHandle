def metade(tupla):
  return len(tupla)//2

def testParity(tupla):
  """Função que testa se a tupla é par"""
  resto = len(tupla) % 2
  if resto == 0:
    return True
  else:
    return False
      
def final(tupla):
  """Função que acha qual é o ultimo elemento da tupla final"""
  return len(tupla) + 1
 