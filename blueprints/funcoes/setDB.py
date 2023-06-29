from ext.banco_dados import conexaoBanco

def setDB(matricula, email, senha_temporaria):    
    conexão = conexaoBanco()
    cur = conexão.cursor()    
    comando = f'INSERT INTO login(matricula, email, senha_temporaria) VALUES (%s, %s, %s);'
    informação = (matricula, email, senha_temporaria)
    cur.execute(comando, informação)
    conexão.commit()
    
def updateSenhaDB(senha, email):
    conexão = conexaoBanco()
    cur = conexão.cursor()   
    comando_senha = f'UPDATE login SET senha = %s WHERE email= %s;'
    informação = (senha, email)   
    cur.execute(comando_senha, informação)
    comando_senha_temporaria = f'UPDATE login SET senha_temporaria = %s WHERE email= %s;'
    informação2 = ('null', email) 
    cur.execute(comando_senha_temporaria, informação2) 
    conexão.commit()

def updateSenhaTemporaria(senha_temporaria, email):
    conexão = conexaoBanco()
    cur = conexão.cursor()   
    comando_senha_temporaria = f'UPDATE login SET senha_temporaria = %s WHERE email= %s;'
    informação = (senha_temporaria, email)   
    cur.execute(comando_senha_temporaria, informação)
    comando_senha = f'UPDATE login SET senha = %s WHERE email= %s;'
    informação2 = ('null', email)
    cur.execute(comando_senha, informação2)    
    conexão.commit()


