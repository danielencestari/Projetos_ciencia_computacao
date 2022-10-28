import sys


def txt_importer(path_file):
    if path_file.endswith(".txt"):
        try:
            with open(path_file, "r") as file:
                content: str = file.read()
                return content.split("\n")
        except FileNotFoundError:
            print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
    else:
        print("Formato inválido", file=sys.stderr)


"""     if not path_file.endswith(".txt"):
        print("Formato inválido", file=sys.stderr)
    else:
        with open(path_file, "r") as file:
            content: str = file.read()
            return content.split("\n") """
