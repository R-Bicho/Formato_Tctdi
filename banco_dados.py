import psycopg2 as db
from db_values import database_infos


def conexaoBanco():    
    conexão = db.connect(database = database_infos.get('database'), 
                     host = database_infos.get('host'), 
                     user = database_infos.get('user'), 
                     password = database_infos.get('password'), 
                     port = database_infos.get('port'))
    
    return conexão




