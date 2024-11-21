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
    db.update_client(5)
    db.close_connection()
    
