import json
from urllib.parse import urlencode
from urllib.request import urlopen


busca = input("Digite uma condição médica em inglês: ")

filtros = {
    "terms": busca,
    "maxList": 10,
    "df": "consumer_name,primary_name",
    "ef": "icd10cm_codes"
}

link = "https://clinicaltables.nlm.nih.gov/api/conditions/v3/search?"
link += urlencode(filtros)

try:
    resposta = urlopen(link)
    dados = json.loads(resposta.read().decode())

    condicoes = dados[3]
    codigos = dados[2]["icd10cm_codes"]

    if len(condicoes) == 0:
        print("Nenhuma condição foi encontrada.")

    for i in range(len(condicoes)):
        nome = condicoes[i][0]

        if i < len(codigos) and codigos[i]:
            codigo = codigos[i]
        else:
            codigo = "Não informado"

        print()
        print("Condição:", nome)
        print("Código sugerido:", codigo)

except Exception:
    print("Não foi possível consultar a API.")
