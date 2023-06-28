from ext.banco_dados import conexaoBanco

def getDB():
    conexão = conexaoBanco()
    cur = conexão.cursor()
    cur.execute('SELECT * FROM teste;')
    resultado = cur.fetchall()
    return resultado  

def setDB(matricula, email, senha):    
    conexão = conexaoBanco()
    cur = conexão.cursor()    
    comando = f'INSERT INTO teste(matricula, email, senha) VALUES (%s, %s, %s);'
    informação = (matricula, email, senha)
    cur.execute(comando, informação)
    conexão.commit()
    
def updateDB(senha, email):
    conexão = conexaoBanco()
    cur = conexão.cursor()   
    comando = f'UPDATE teste SET senha = %s WHERE email= %s;' 
    informação = (senha, email)   
    cur.execute(comando, informação)
    conexão.commit()

#setDB('f12345', 'rogerio@123', 'seila')
#updateDB('teste', 'rogerio@123')

