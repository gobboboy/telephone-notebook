import pprint

contatos = {}


#Função que recebe o cadastro de um ou mais usuários por vez.
def cadastro():
    x = int(input("\nQuantos usuários você deseja cadastrar?\n>> "))     
    
    
    while x > 0:
        nome = input("\nNome: ").strip().lower()
        telefone = input("Telefone: ").strip().lower()
        email = input("E-mail: ").strip().lower()
        insta = input("Instagram: ").strip().lower()
        twitter = input("Twitter: ").strip().lower()
        contatos[nome] = {
            "nome": nome,
            "telefone": telefone,
            "email": email,
            "instagram": insta,
            "twitter": twitter
            }
        x -= 1
        print("Usuário cadastrado!\n")

#Função que pesquisa e demonstra os dados do contato informado pelo nome.
def pesquisa():
    nome = input("\nNome: ").lower()
    if nome in contatos:
        pprint.pprint(contatos[nome])
    
    else:
        print(f'O nome {nome} não foi encontrado no banco de dados.')


#Função que deleta o usuário cadastrado informado pelo nome.
def deletar():
    nome = input("Qual contato deseja remover?\n>> ").lower()
    if nome in contatos:
        del contatos[nome]
        print("Contato removido com sucesso!\n")
    else:
        print(f'Não há ninguém chamado {nome} no banco de dados.')
    

#Função que edita o contato já cadastrado informado pelo nome.
def alterar():
    nome = input("Qual contato deseja alterar?\n>> ").lower()
    if nome in contatos:
        del contatos[nome]
        nome = input("Nome novo: ").strip().lower()
        telefone = input("Telefone novo: ").strip().lower()
        email = input("E-mail novo: ").strip().lower()
        insta = input("Instagram novo: ").strip().lower()
        twitter = input("Twitter novo: ").strip().lower()
        contatos[nome] = {
            "nome": nome,
            "telefone": telefone,
            "email": email,
            "instagram": insta,
            "twitter": twitter
        }
        print(f'O contato {nome} foi alterado com sucesso!\n')
    else:
        print(f'Não há ninguém chamado {nome} no banco de dados.')


#Função que lista todos o contatos cadastrados e demonstra todos os dados de cada usuário.
def listar():
    print("LISTA DE CADASTRADOS: ")
    for nome, info in contatos.items():
        print('\nContato:', nome )
        for key in info:
            print(key + ':', info[key])



#Função do menu principal que chama todas as funções anteriores, criando uma interface de uso.
def menu():
    print("\nSeja bem vindo!")
    while True:
        try: 
            x = int(input("\n1 - Cadastrar usuário\n2 - Consultar por nome\n3 - remover usuário já cadastrado\n4 - Alterar usuário\n5 - Listar usuários cadastrados\n0 - Sair\n>> "))
            if x == 1:    
                cadastro()
            elif x == 2:
                pesquisa()
            elif x == 3:
                    deletar()
            elif x == 4:
                    alterar()
            elif x == 5:
                    listar()
            else:
                    break               
        except:
            print("algo deu errado, tente novamente")
            continue

#Executando a função principal (menu).
menu()
