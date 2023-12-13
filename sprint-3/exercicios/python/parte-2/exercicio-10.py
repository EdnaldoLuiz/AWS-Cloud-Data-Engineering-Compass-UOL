def remover_duplicatas(lista):
    return list(set(lista))

lista_teste = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']

nova_lista_sem_duplicatas = remover_duplicatas(lista_teste)
print(nova_lista_sem_duplicatas)
