from collections import Counter
from inventory_report.reports.simple_report import SimpleReport


def empresas(data):
    resultado = ""
    for element in Counter(data).most_common():
        resultado += f"- {element[0]}: {element[1]}\n"
    return resultado


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(lista):
        empresas_lista = []
        for empresa in lista:
            empresas_lista.append(empresa["nome_da_empresa"])
        lista_empresas = empresas(empresas_lista)
        return (
            f"{SimpleReport.generate(lista)}\n"
            "Produtos estocados por empresa:\n"
            f"{lista_empresas}"
            )
