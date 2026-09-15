from idlelib import query
from os import name
from re import search

from model import model_lead
import control
def add_lead():
    name = input("Nome: ")
    email = input("Email: ")
    company = input("Empresa: ")
    stage = input("Estágio de Vendas: ")

    if not name or not email or "@" not in email:
        print("Nome e/ou email válido são obrigatórios.")
        return

    # chamar model para modelar dados
    print(name, email, company, stage)

    # Depois de modelado
    # chamar control.py para enviar os dados modelados para o banco de dados json
    #print(model_lead(name, email, company, stage))

    control.create_lead(model_lead(name, email, company, stage))

def list_leads():
    leads = control.read_leads()

    if not leads:
        print("nenhum lead ainda")
        return

    print("\n |Nome                | Empresa             |E-mail")
    for i, lead in enumerate(leads):
        print(f"{i:02d} : {lead["nome"]:<20} {lead["email"]:<17}  {lead["company"]: <20}")

def search_leads():
    query = input("Buscar por: ").strip().lower()
    if not query:
        print("consulta vazia")
        return
# nesse mon=mento irei enviar minha usca para control
# o control.read_lead_search
leads_finded = control.search_leads(query)

print(f"\n# |{"Nome":<20}| {Empresa:<}             | E-mail")
for i, lead in enumerate(leads_finded):
    print(f"{i:02d} : {lead["nome"]:<20} {lead["company"]:<17}  {lead["email"]: <20}")

def export_leads():
    path_csv = control.export_csv()

    if path_csv is None:
        print("nenhum lead nao encontrado")
    else:
        print(f"CSV exportado para {path_csv}")

def main():
    while True:
        print("\nMini CRM - 1º Aula - (adicionar/listar")
        print("[1] Adicionar lead")
        print("[2] Listar lead")
        print("[3] Buscar (nome, email, empresa)")
        print("[4] Listar lead")
        print("[0] Sair")

        cpt = input("Escolha uma opcao: ")
        if cpt == "1":
            add_lead()
        elif cpt == "2":
            list_leads()
        elif cpt == "3":
            search.leads()
        elif cpt == "4":
            export.leads()
        elif cpt == "0":
            print("Sair")
            break
        else:
            print("Opcao invalida!")


if __name__ == "__main__":
    main()