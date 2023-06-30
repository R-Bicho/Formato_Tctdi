from email.message import EmailMessage
import ssl
import smtplib
from ext.email_values import email_infos
import re

def enviandoEmail(email_destino, senha_temporaria):

    password = email_infos.get('password')
    email_sender = email_infos.get('email')
    email_reciver = email_destino   

    subject = 'Senha Temporaria'

    body = f'''Segue senha Temporaria: {senha_temporaria}\n
    A senha deverá ser alterada no primeiro acesso!\n
    Basta efetuar o login com sua matricula e com a senha temporaria que você será redirecionado para alterar a senha
    '''      

    em = EmailMessage()
    em["From"] = email_sender
    em["to"] = email_reciver
    em["Subject"] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(email_sender, password)
        smtp.sendmail(email_sender, email_reciver,em.as_string())


def validandoEmail(email):
    email_regexp = re.compile(r'^[A-Za-z]*@timbrasil\.com\.br$')
    email_regexp = re.compile(r'^[A-Za-z]*-([A-Za-z]*)? @outlook\.com$')

    if email_regexp.search(email):
        return True
    return False
    

