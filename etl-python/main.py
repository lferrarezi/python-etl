# variáveis
from db_credentials import datawarehouse_db_config, sqlserver_db_config, mysql_db_config, fdb_db_config
from sql_queries import fbd_queries, sqlserver_queries, mysql_queries
from variables import *

# métodos
from etl import etl_process
import pyodbc

def main():
    print('iniciando etl-python')

    # estabelecimento de conexão com o banco de dados alvo (sql-server)
    target_cnx = pyodbc.connect(**datawarehouse_db_config)

    # loop através das credenciais

    # mysql
    for config in mysql_db_config:
        try:
            print("carregando bd: " + config['database'])
            etl_process(mysql_queries, target_cnx, config, 'mysql')
        except Exception as error:
            print("etl para {} apresenta erro".format(config['database']))
            print('mensagem de erro: {}'.format(error))
            continue

    # sql-server
    for config in sqlserver_db_config:
        try:
            print("carregando bd: " + config['database'])
            etl_process(sqlserver_queries, target_cnx, config, 'sqlserver')
        except Exception as error:
            print("etl para {} apresenta erro".format(config['database']))
            print('mensagem de erro: {}'.format(error))
            continue

    # firebird
    for config in fbd_db_config:
        try:
            print("carregando bd: " + config['database'])
            etl_process(fbd_queries, target_cnx, config, 'firebird')
        except Exception as error:
            print("etl para {} apresenta erro".format(config['database']))
            print('mensagem de erro: {}'.format(error))
            continue

    target_cnx.close()

if __name__ == "__main__":
    main()
