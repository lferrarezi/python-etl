# módulos python
import mysql.connector
import pyodbc
import fdb

# variáveis
from variables import datawarehouse_name

def etl(query, source_cnx, target_cnx):
    # extrai dados do bd de origem
    source_cursor = source_cnx.cursor()
    source_cursor.execute(query.extract_query)
    data = source_cursor.fetchall()
    source_cursor.close()

    # carrega os dados no bd de warehouse
    if data:
        target_cursor = target_cnx.cursor()
        target_cursor.execute("USE {}".format(datawarehouse_name))
        target_cursor.executemany(query.load_query, data)
        print('dados carregados no bd de warehouse')
        target_cursor.close()
    else:
        print('dados estão vazios')

def etl_process(queries, target_cnx, source_db_config, db_platform):
    # estabelece conexão com o bd de origem
    if db_platform == 'mysql':
        source_cnx = mysql.connector.connect(**source_db_config)
    elif db_platform == 'sqlserver':
        source_cnx = pyodbc.connect(**source_db_config)
    elif db_platform == 'firebird':
        source_cnx = fdb.connect(**source_db_config)
    else:
        return 'Erro! plataforma de bd desconhecida'

    # loop pelas consultas (queries) sql
    for query in queries:
        etl(query, source_cnx, target_cnx)

    # fecha a conexão com o bd de origem
    source_cnx.close()
