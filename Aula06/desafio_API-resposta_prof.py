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

print(sucesso(status[2][1]))
