from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path, encoding="utf-8") as file:
        csv_file = csv.DictReader(file, delimiter=",", quotechar='"')
        lista = list(csv_file)
        return lista


"""
tem q importar o csv para ler o arquivo.
ai le o arquivo p/ retornar o stack_list.
usa o metodo de ler, e faz a delimitacao, e diz que tem que ficar entre aspas.
retorna essa informacao tratada na lista.
"""
