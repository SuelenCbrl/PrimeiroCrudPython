from Entity.Cliente import Cliente 



########## CADASTRO DO CLIENTE ###############
cli1= Cliente()
clientes = cli1.selecionar()
for cliente in clientes:
    print(cliente)


print("\n SELECIONE UM CLIENTE PARA EDITAR!")
id_selecao=int(input("DIGITE O ID: "))

cli_selecionado = list(cli1.selecionar_por_id(id_selecao))

cli_selecionado[1]=input("Digite o novo nome:")
cli_selecionado[2]=input("Digite o cpf: ")
cli_selecionado[3]=input("Digite o login: ")
cli_selecionado[4]= input("Digite o senha: ")
cli_selecionado[5]= input("Digite o fone: ")
cli_selecionado[6]=input("Digite o cidade: ")

atualiza = cli1.atualizar(cli_selecionado)

if atualiza:
    print("\n Cliente Atualizado com Sucesso!!!")


# print("\n DESEJA DELETAR ALGUEM? ")
# id_deletar=int(input("Digite o Id do Abençoado: "))
# cli_deletado = cli1.deletar(id_deletar)

# if cli_deletado == True:
#     print("Cliente deletado com sucesso")
#     clientes = cli1.selecionar()
#     for cliente in clientes:
#         print(cliente)

# print("\n CADASTRAR UM CLIENTE?")
# cli1.nome=input("Digite seu Nome: ")
# cli1.cpf=input("Digite seu Cpf: ")
# cli1.login=input("Digite seu Login: ")
# cli1.senha=input("Digite seu Senha: ")
# cli1.fone=input("Digite seu Fone: ")
# cli1.cidade=input("Digite seu Cidade: ")

# cadastro = cli1.cadastrar()
# if cadastro == True:
#     print("NO FRONT, CLIENTE CADASTRARDO COM SUCESSO!!")




#########################################################
# banco= Database()

# dados = banco.select_client()

# print("Clientes Cadastrados: ")
# for item in dados:
#     print(item)


# print("\n SELECIONE UM CLIENTE PARA EDITAR!")
# id_selecao=int(input("DIGITE O ID: "))

# cli_selecionado = list(banco.select_client_by_id(id_selecao))


# cli_selecionado[1]=input("Digite o novo nome:")
# cli_selecionado[2]=input("Digite o cpf: ")
# cli_selecionado[3]=input("Digite o login: ")
# cli_selecionado[4]= input("Digite o senha: ")
# cli_selecionado[5]= input("Digite o fone: ")
# cli_selecionado[6]=input("Digite o cidade: ")

# atualiza =banco.update_client(cli_selecionado)

# if atualiza:
#     print("\n Cliente Atualizado com Sucesso!!!")