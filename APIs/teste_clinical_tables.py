import json
from urllib.parse import urlencode
from urllib.request import urlopen


termo = input("Digite uma condição médica em inglês: ")

parametros = urlencode({
    "terms": termo,
    "maxList": 10,
    "df": "consumer_name,primary_name",
    "ef": "icd10cm_codes"
})

url = f"https://clinicaltables.nlm.nih.gov/api/conditions/v3/search?{parametros}"

try:
    with urlopen(url, timeout=15) as resposta:
        dados = json.loads(resposta.read().decode("utf-8"))

    nomes = dados[3]
    codigos = dados[2].get("icd10cm_codes", [])

    if not nomes:
        print("\nNenhuma condição foi encontrada.")
    else:
        print("\nResultados encontrados:\n")

        for posicao, nomes_condicao in enumerate(nomes):
            nome = nomes_condicao[0]
            codigo = (
                codigos[posicao]
                if posicao < len(codigos) and codigos[posicao]
                else "Não informado"
            )

            print(f"Condição: {nome}")
            print(f"Código sugerido: {codigo}")
            print()

except Exception as erro:
    print(f"Não foi possível consultar a API: {erro}")
