import mysql.connector

class Database():
    def __init__(self,banco="syspython"):
        self.banco = banco
    
    def connect(self):
        self.conn = mysql.connector.connect(host='localhost',database=self.banco,user='root',password='')

        if self.conn.is_connected():
            self.cursor=self.conn.cursor()
            db_info = self.conn.get_server_info()
            print("Conectado com sucesso!",db_info)
        else:
            print("Error")
    def insert_client(self):
        self.connect()
        try:
            args=("João ","598","meulogin03","1234562","67999122","CG")

            self.cursor.execute('INSERT INTO cliente(nome,cpf,login,senha,fone,cidade) VALUES (%s,%s,%s,%s,%s,%s)',args)
            self.conn.commit()
            print("Cliente cadastrado com sucesso!")

        except Exception as err:
            print(err)


    def select_client(self):
        self.connect()
        try:
            self.cursor.execute("SELECT * FROM cliente")
            clientes = self.cursor.fetchall()
            for item in clientes:
                print(item)

        except Exception as err:
            print(err)

    def select_client_by_id(self,id):
        self.connect()
        try:
            self.cursor.execute(f"SELECT * FROM cliente WHERE id = {id}")
            cli = self.cursor.fetchone()
            return cli

        except Exception as err:
            print(err)

    def update_client(self,id):
        self.connect()
        try:
            cliente = list(self.select_client_by_id(id))
            cliente[1]=input("Digite o novo nome:")
            cliente[2]=input("Digite o cpf: ")
            cliente[3]=input("Digite o login: ")
            cliente[4]= input("Digite o senha: ")
            cliente[5]= input("Digite o fone: ")
            cliente[6]=input("Digite o cidade: ")

            self.cursor.execute(f"""UPDATE cliente SET 
                                nome = '{cliente[1]}',
                                cpf ='{cliente[2]}',
                                login = '{cliente[3]}',
                                senha='{cliente[4]}',
                                fone='{cliente[5]}',
                                cidade='{cliente[6]}' 
                                WHERE id = {cliente[0]}""")
            self.conn.commit()
            cli_atualizado = self.select_client_by_id(cliente[0])
            print(cli_atualizado,"Cliente atualizado com sucesso!")
    
   
        except Exception as err:
            print(err)


    def delete_client(self,id):
        self.connect()
        try:
            self.cursor.execute(f"DELETE FROM cliente  WHERE id ={id}")
            self.conn.commit()
            print("Cliente Deletado com sucesso!")
        
        except Exception as err:
            print(err)

    def insert_produto(self):
        self.connect()
        try:
            args1=("Fichario ","tilibra","A5","Caderno tamnaho A3 tema Harry Potter","R$89,90","A5","21x20","180mg")

            self.cursor.execute('INSERT INTO produto (nome_prod,marca,modelo,descricao,preco,tipo,tamanho,peso) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)',args1)
            self.conn.commit()
            print("Produto cadastrado com sucesso!")

        except Exception as err:
            print(err)


    def select_produto(self):
        self.connect()
        try:
            self.cursor.execute("SELECT * FROM produto")
            produto = self.cursor.fetchall()
            for item in produto:
                print(item)

        except Exception as err:
            print(err)

    def select_produto_by_id(self,id_prod):
        self.connect()
        try:
            self.cursor.execute(f"SELECT * FROM produto WHERE id_prod = {id_prod}")
            prod = self.cursor.fetchone()
            return prod

        except Exception as err:
            print(err)

    def update_produto(self,id_prod):
        self.connect()
        try:
            produto = list(self.select_produto_by_id(id_prod))
            produto[1]=input("Digite o novo nome:")
            produto[2]=input("Digite a marca: ")
            produto[3]=input("Digite o modelo: ")
            produto[4]=input("Digite o descricao: ")
            produto[5]=input("Digite o preco: ")
            produto[6]=input("Digite o tipo: ")
            produto[7]=input("Digite o tamanho: ")
            produto[8]=input("Digite o peso: ")

            self.cursor.execute(f"""UPDATE produto SET 
                                nome_prod = '{produto[1]}',
                                marca ='{produto[2]}',
                                modelo = '{produto[3]}',
                                descricao='{produto[4]}',
                                preco='{produto[5]}',
                                tipo='{produto[6]}',
                                tamanho='{produto[7]}',
                                peso='{produto[8]}'
                                WHERE id_prod = {produto[0]}""")
            self.conn.commit()
            pro_atualizado = self.select_produto_by_id(produto[0])
            print(pro_atualizado,"Produto atualizado com sucesso!")
    
   
        except Exception as err:
            print(err)


    def delete_produto(self,id_prod):
        self.connect()
        try:
            self.cursor.execute(f"DELETE FROM produto  WHERE id_prod ={id_prod}")
            self.conn.commit()
            print("Produto Deletado com sucesso!")
        
        except Exception as err:
            print(err)
    def close_connection(self):
        if self.conn.is_connected():
            self.cursor.close()
            self.conn.close()
            print("Conexão encerrada com sucesso!")

if __name__=='__main__':
    db =Database()
    # db.insert_client()
    # db.select_client()
    # db.select_client_by_id(2)
    # db.update_client(2)
    # db.update_client(5)
    # db.insert_produto()
    # db.select_produto()
    # db.select_produto_by_id(1)
    # db.update_produto(5)
    # db.delete_produto(4)
    db.close_connection()
    
