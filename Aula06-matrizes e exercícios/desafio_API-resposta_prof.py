endpoints = ["/login", "/produtos", "/pedidos"]
status = [
    [200, 200, 401, 200, 500],
    [200, 200, 200, 200, 200],
    [201, 500, 502, 201, 500]
]
#
#

#função para detectar se um status é sucesso
def sucesso(codigo):
    return codigo >= 200 and codigo <= 299

# print(sucesso(401))

#função valida na lista de req DE UM endpoint SEtem DOIS erros seguidos
# status [0] =  [200, 200, 401, 200, 500] ----> false
# status [1] =  [200, 200, 200, 200, 200] ----> false
# status [2] =  [201, 500, 502, 201, 500] ----> true

def erros_seguidos(respostas_http):
    for i in range(len(respostas_http)-1):
        codigo_atual = respostas_http[i]
        prox_codigo = respostas_http[i+1]

        if not sucesso(codigo_atual) and not sucesso(prox_codigo):
            return True
    return False

def analisar_endpoint(respostas_http):
    qtd_sucesso = 0

    for cod_http in respostas_http:
        if sucesso(cod_http):
            qtd_sucesso += 1

    qtd_tot_req = len(respostas_http)
    qtd_erros =qtd_tot_req - qtd_sucesso
    percentual_sucesso = (qtd_sucesso/qtd_tot_req) *100
    tem_erros_seguidos = erros_seguidos(respostas_http)

    if tem_erros_seguidos:
        classificacao = "Crítico"
    elif percentual_sucesso:
        classificacao = "Crítico"
    else:
        classificacao = "Instável"

    return (qtd_sucesso, qtd_erros, percentual_sucesso ,classificacao)

maior_qtd_erros = -1
endpoint_maior_erros = ""

for i in range(len(endpoints)):
    nome_endpoint = endpoints[i]
    respostas_endpoint = status[i]

    sucessos, erros, percentual, classificacao = analisar_endpoint(respostas_endpoint)

    print(f"Endpoint: {nome_endpoint}")
    print(f"Status code: {respostas_endpoint}")
    print(f"Status code: {sucessos}")
    print(f"Status code: {erros}")
    print(f"Status code: {percentual}")
    print(f"Status code: {classificacao}")
    print(f"-" * 30)

    if erros > maior_qtd_erros:
        maior_qtd_erros = erros
        endpoint_maior_erros = nome_endpoint

print(f"Endpoint com mais erros: {endpoint_maior_erros}")