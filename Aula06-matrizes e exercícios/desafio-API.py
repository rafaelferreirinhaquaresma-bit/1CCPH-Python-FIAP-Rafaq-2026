endpoints = ["/login", "/produtos", "/pedidos"]
status = [
    [200, 200, 401, 200, 500],
    [200, 200, 200, 200, 200],
    [201, 500, 502, 201, 500]
]

def analisar_endpoints(endpoints, status):
    resultados = {}
    for i, endpoint in enumerate(endpoints):
        reqs = status[i]
        total = len(reqs)
        sucessos = sum(1 for r in reqs if 200 <= r <= 299)
        erros = total - sucessos
        porcentagem = (sucessos / total) * 100

        # Verificar erros consecutivos
        erros_consecutivos = any(reqs[j] >= 300 and reqs[j+1] >= 300 for j in range(total-1))

        # Classificação
        if erros_consecutivos:
            classificacao = "CRÍTICO"
        elif porcentagem >= 80:
            classificacao = "ESTÁVEL"
        else:
            classificacao = "INSTÁVEL"

        resultados[endpoint] = {
            "sucesso_%": porcentagem,
            "erros": erros,
            "erros_consecutivos": erros_consecutivos,
            "classificacao": classificacao
        }
    return resultados

resultados = analisar_endpoints(endpoints, status)

# Identificar endpoint com mais erros
endpoint_mais_erros = max(resultados, key=lambda e: resultados[e]["erros"])

# Exibir resultados
for ep, dados in resultados.items():
    print(f"Endpoint: {ep}")
    print(f"  Sucesso: {dados['sucesso_%']:.2f}%")
    print(f"  Erros: {dados['erros']}")
    print(f"  Dois erros seguidos: {dados['erros_consecutivos']}")
    print(f"  Classificação: {dados['classificacao']}")
    print()

print(f"Endpoint com mais erros: {endpoint_mais_erros}")
