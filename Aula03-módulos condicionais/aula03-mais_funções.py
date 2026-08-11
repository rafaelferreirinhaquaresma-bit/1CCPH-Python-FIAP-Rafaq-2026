#função com parâmetro sem retorno
def boas_vindas(nome):
    print(f"Ola, {nome}, seja bem vindo!!!")

nome_digitado = input("digite seu nome: ")
boas_vindas(nome_digitado)

#função com parâmetro com retorno
def soma(num_a, num_b):
    soma = num_a + num_b
    return soma

resultado_soma = soma(5,9)
print(resultado_soma)
print(type(nome_digitado))