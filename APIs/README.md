# Teste da Clinical Tables API

O código pede que o usuário digite uma condição médica em inglês, envia a pesquisa para a API e mostra os nomes e códigos sugeridos encontrados. Caso não existam resultados ou ocorra algum problema na consulta, o programa apresenta uma mensagem informando o que aconteceu.
Essa API ajuda a pesquisar e padronizar os nomes das condições médicas. No MedMap, isso pode evitar registros confusos ou escritos de formas diferentes, deixando o histórico familiar mais organizado e fácil de compreender.
Para executar o teste:


python APIs/teste_clinical_tables.py


Quando o programa solicitar uma condição, pode ser digitado o termo `diabetes`. O resultado esperado é uma lista com as condições encontradas e seus códigos sugeridos.

# resumo do código

O código recebe o nome de uma condição médica digitada pelo usuário, envia essa informação para a Clinical Tables API e apresenta os nomes e códigos sugeridos encontrados. Caso não existam resultados ou ocorra algum problema na consulta, o programa informa ao usuário.
