print("Hello world")

print(7 + 4)
print("7 + 4")
print("7"+"4") #concatenando strings
# comentários de uma linha

'''
comentários de 
multiplas
linhas
'''
# variáveis
nome = "Rafael" #str
idade = 18 #int
peso= 83,5 #float

print(nome, idade, peso)

#input
nome = input("digite o seu nome: ")
idade = int(input("digite a sua idade: "))
peso = float(input("digite o seu peso: "))

print(nome, idade, peso)

print(f"oiii,{nome} !!!")

ano_nascimento = 2007
ano_atual = 2026
idade =ano_atual - ano_nascimento
print (idade)