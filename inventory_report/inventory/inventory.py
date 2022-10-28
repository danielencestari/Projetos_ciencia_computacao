from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport
import csv
import json
import xml.etree.ElementTree as ET


def readJSON(path):  # json is the best
    with open(path) as f:
        array = json.load(f)
    return array


def readCSV(path):  # csv is complicated
    with open(path, encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=',', quotechar='"')
        header, *data = reader

    array = []
    for row in data:
        file = {}
        for index in range(len(header)):
            file[header[index]] = row[index]
        array.append(file)

    return array


def readXML(path):  # xml is the worst... it's a nightmare
    file = []
    tree = ET.parse(path)
    armazenamento = 'instrucoes_de_armazenamento'
    for product in tree.findall('record'):
        file.append(
          {
            'id': product.find('id').text,
            'nome_do_produto': product.find('nome_do_produto').text,
            'nome_da_empresa': product.find('nome_da_empresa').text,
            'data_de_fabricacao': product.find('data_de_fabricacao').text,
            'data_de_validade': product.find('data_de_validade').text,
            'numero_de_serie': product.find('numero_de_serie').text,
            armazenamento: product.find(armazenamento).text,
           }
         )
    return file


def readTypeOfpath(path):
    if path.endswith('csv'):
        return readCSV(path)

    if path.endswith('json'):
        return readJSON(path)

    if path.endswith('xml'):
        return readXML(path)


class Inventory:
    def import_data(path, type):
        inventory = readTypeOfpath(path)
        report = ''
        if (type == 'simples'):
            report = SimpleReport.generate(inventory)
        else:
            report = CompleteReport.generate(inventory)
        return report
