from ext.banco_dados import conexaoBanco

def getDB():
    conexao = conexaoBanco()    
    cur = conexao.cursor()
    cur.execute('SELECT * FROM login')
    resultado = cur.fetchall()
    return resultado 

def emailPorMatricula(matricula):
    for values in getDB():
        if values[0] == matricula:
            return values[1]

def MatriculaDB(matricula):
    matriculas = []
    for value in getDB():
        matriculas.append(value[0])    
    return matricula in matriculas

def emailDB(email):
    emails = []
    for value in getDB():
        emails.append(value[1])    
    return email in emails

def senhaDB(senha):
    senhas = []
    for value in getDB():
        senhas.append(value[2])    
    return senha in senhas

def senhaTemporariaDB(matricula):
    for values in getDB():
        if values[0] == matricula:
            return values[3]

