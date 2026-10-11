import requests
import datetime

def cotar():
    cotacoes = []
    hoje = datetime.date.today()
    
    for i in range(365):
        data = hoje - datetime.timedelta(days=i)

        tem_cotacao = False
        while not tem_cotacao:

            url = fr"https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarDia(dataCotacao=@dataCotacao)?@dataCotacao='{data}'&$top=100&$format=json&$select=cotacaoCompra"
            res = requests.get(url)
            res = res.json()

            if res['value']:
                tem_cotacao = True
                cotacoes.append(res['value'][0]['cotacaoCompra'])
            else:
                dia_anterior = datetime.datetime.strptime(data, "%m-%d-%Y") - datetime.timedelta(1)
                data = datetime.datetime.strftime(dia_anterior, "%m-%d-%Y")
        
    return cotacoes
print(cotar())

