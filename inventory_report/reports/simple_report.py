from datetime import datetime


def getClosestExpiration(products):
    today = datetime.today().date()
    almost_expired = datetime.strptime('9999-01-11', '%Y-%m-%d').date()
    for product in products:
        expiration_date = datetime.strptime(
            product['data_de_validade'], '%Y-%m-%d'
            ).date()
        if expiration_date > today and expiration_date < almost_expired:
            almost_expired = expiration_date

    return almost_expired


def getOldest(products):
    oldest = datetime.strptime('9999-01-11', '%Y-%m-%d').date()
    for product in products:
        fab_date = datetime.strptime(
            product['data_de_fabricacao'], '%Y-%m-%d'
         ).date()
        if fab_date < oldest:
            oldest = datetime.strptime(
                product['data_de_fabricacao'], '%Y-%m-%d'
            ).date()

    return oldest


def getBiggestProductCount(products):
    cont_empresa = []

    for product in products:
        nome_empresa = product['nome_da_empresa']
        counter = 0
        for empresa in products:
            if empresa['nome_da_empresa'] == nome_empresa:
                counter += 1
        cont_empresa.append({'empresa': nome_empresa, 'count': counter})

    # https://reactgo.com/get-first-element-in-list-python/

    return sorted(
        cont_empresa,
        key=lambda x: x['count'],
        reverse=True
     )


class SimpleReport:
    def generate(products):

        oldest = getOldest(products)
        almost_expired = getClosestExpiration(products)
        cont_empresa = getBiggestProductCount(products)

        return (
          f'Data de fabricação mais antiga: {oldest}\n'
          f'Data de validade mais próxima: {almost_expired}\n'
          f'Empresa com mais produtos: {cont_empresa[0]["empresa"]}'
        )
