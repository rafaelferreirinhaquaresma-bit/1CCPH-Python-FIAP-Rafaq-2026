#LOGICA E(and)
from astropy.io.fits.scripts.fitsheader import print_headers_as_table

verifica_email = True
verifica_senha = False

verifica_login = verifica_email and verifica_senha
print(verifica_login)

if verifica_login:
    print("Entrar no prgorama")

#logica OU (or)
logica_ou = True or False or False
print(logica_ou)

#Operador NOT
negacao = not True
print(negacao)

if not verifica_login:
    print("Loga certo ai cara!")

