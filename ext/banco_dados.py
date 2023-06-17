import psycopg2 as db
from ext.db_values import database_infos


def conexaoBanco():    
    conexão = db.connect(database_infos.get('database'))    
    return conexão




