import handle

"""Para passar varios argumento em formato de coleção, use * antes da coleção, como{*lista}"""
lista = [1,2,3,4]
tupla = ("Pedro", "BCMT", 19, 9.5)
tupla_metade = handle.incrementByHalf(tupla, "pedro", "augusto", *lista, lista)
tupla_indice = handle.incrementByPosition(tupla, 3, "pedro", "augusto", *lista, lista)
tupla_comeco = handle.incrementInStart(tupla, "augusto", *lista, lista)

print(50*"-")
print("adicionando na metade", tupla_metade, sep=" ")
print(50*"-")
print("adicionando pela posição", tupla_indice, sep=" ")
print(50*"-")
print("adicionando no começo", tupla_comeco, sep=" ")
print(50*"-")
