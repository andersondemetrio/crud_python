import sqlite3

from crud.model.cliente import Cliente

class DataBase:
    def __init__(self, nome='system.db'):
        self.connection = None
        self.name = nome

    def connect(self):
        self.connection = sqlite3.connect(self.name)

    def close_connection(self):
        try:
            self.connection.close()
        except sqlite3.Error as e:
            print(e)

    def create_table_cliente(self):
        self.connect()
        cursor = self.connection.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS CLIENTE(
            CPF TEXT,
            NOME TEXT,
            TELEFONE_FIXO TEXT,
            TELEFONE_CELULAR TEXT,
            SEXO TEXT,
            CEP TEXT,
            LOGRADOURO TEXT,
            NUMERO TEXT,
            COMPLEMENTO TEXT,
            BAIRRO TEXT,
            MUNICIPIO TEXT,
            ESTADO TEXT,
            
            PRIMARY KEY (CPF)             
            );
            """)
        self.close_connection()


    def registrar_cliente(self, cliente=Cliente):
        self.connect()
        cursor = self.connection.cursor()
        campos_cliente = ('CPF', 'NOME', 'TELEFONE_FIXO',
                          'TELEFONE_CELULAR', 'SEXO', 'CEP', 'LOGRADOURO', 'NUMERO', 'COMPLEMENTO', 'BAIRRO',
                          'MUNICIPIO', 'ESTADO')
        valores = f"'{str(cliente.cpf).replace('.','').replace('-','')}', '{cliente.nome}', '{cliente.telefone_fixo}', " \
                  f"'{cliente.telefone_celular}', '{cliente.sexo}', '{cliente.cep}', '{cliente.logradouro}', " \
                  f"'{cliente.numero}', '{cliente.complemento}', '{cliente.bairro}', '{cliente.municipio}', " \
                  f"'{cliente.estado}'"

        try:
            cursor.execute(f"""INSERT INTO CLIENTE {campos_cliente} VALUES ({valores})""")
            self.connection.commit()
            return 'Ok'

        except sqlite3.Error  as e:
            return str(e)
        finally:
            self.close_connection()


    def consultar_cliente(self, cpf):
        self.connect()
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"""SELECT * FROM CLIENTE WHERE CPF = '{str(cpf).replace('.','').replace('-','')}'""")
            return cursor.fetchone()
        except sqlite3.Error as e:
            return None
        finally:
            self.close_connection()

    def deletar_cliente (self, cpf):
        self.connect()
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"""DELETE FROM CLIENTE WHERE CPF = '{str(cpf).replace('.','').replace('-','')}'""")
            self.connection.commit()
            return 'OK'
        except sqlite3.Error as e:
            print(e)


    def atualizar_cliente (self,cliente = Cliente):
        self.connect()
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"""UPDATE CLIENTE SET
                 NOME = '{cliente.nome}'
                 TELEFONE_FIXO = '{cliente.telefone_fixo}'
                 TELEFONE_CELULAR = '{cliente.telefone_celular}'
                 SEXO = '{cliente.sexo}'
                 CEP = '{cliente.cep}'
                 LOGRADOURO = '{cliente.logradouro}'
                 NUMERO = '{cliente.numero}'
                 COMPLEMENTO = '{cliente.complemento}'
                 BAIRRO = '{cliente.bairro}'
                 MUNICIPIO = '{cliente.municipio}'
                 ESTADO = '{cliente.estado}'
                               
                 WHERE CPF = '{str(cpf).replace('.','').replace('-','')}'""")

            self.connection.commit()
            return 'OK'
        except sqlite3.Error as e:
            print(e)
