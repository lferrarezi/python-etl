from variables import datawarehouse_name

# sql-server (bd alvo, datawarehouse)
datawarehouse_db_config = {
    'Trusted_Connection': 'yes',
    'driver': '{SQL Server}',
    'server': 'datawarehouse_sql_server',
    'database': '{}'.format(datawarehouse_name),
    'user': 'usuário_bd',
    'password': 'senha_bd',
    'autocommit': True,
}

# sql-server (bd origem)
sqlserver_db_config = [
    {
        'Trusted_Connection': 'yes',
        'driver': '{SQL Server}',
        'server': 'nome_sql_server',
        'database': 'db1',
        'user': 'usuário_bd',
        'password': 'senha_bd',
        'autocommit': True,
    }
]

# mysql
mysql_db_config = [
    {
        'user': 'seu_usuário_1',
        'password': 'sua_senha_1',
        'host': 'db_connection_string_1',
        'database': 'db_1',
    },
    {
        'user': 'seu_usuário_2',
        'password': 'sua_senha_2',
        'host': 'db_connection_string_2',
        'database': 'db_2',
    },
]

# firebird
fdb_db_config = [
    {
        'dsn': '/seu/caminho/para/origem.db',
        'user': 'seu_usuário',
        'password': 'sua_senha',
    }
]
