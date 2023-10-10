import handle


tupla = ("Pedro", "BCMT", 19, 9.5)

tupla_metade = handle.incrementByHalf(tupla, "primeiro período")
tupla_indice = handle.incrementByPosition(tupla, "primeiro período", 3)
tupla_comeco = handle.incrementInStart(tupla, "primeiro período")

print(tupla_metade)
print(tupla_indice)
print(tupla_comeco)