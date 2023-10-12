import handle


lista = [1,2,3,4]
tupla = ("Pedro", "BCMT", 19, 9.5, 8)

tupla_metade = handle.incrementByHalf(tupla, "pedro", -1)
tupla_indice = handle.incrementByPosition(tupla, lista, 3)
tupla_comeco = handle.incrementInStart(tupla, "primeiro período")

print(tupla_metade)
print(tupla_indice)
print(tupla_comeco)



print(type(tupla_indice[0]))
