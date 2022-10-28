import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    lines = txt_importer(path_file)
    fileFinal = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(lines),
        "linhas_do_arquivo": lines
    }

    if (instance.data.count(fileFinal) == 0):
        instance.enqueue(fileFinal)
        print(fileFinal)


def remove(instance):
    if len(instance) == 0:
        print("Não há elementos")
    else:
        removed = instance.dequeue()
        print(f"Arquivo {removed['nome_do_arquivo']} removido com sucesso")


def file_metadata(instance, position):
    if position > len(instance.data) or position < 0:
        print("Posição inválida", file=sys.stderr)
    else:
        print(instance.data[position], file=sys.stdout)
