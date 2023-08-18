# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.message import EmailMessage



def enviar_email(destinatarios, assunto, mensagem, error_message):
    # Configurar o servidor SMTP
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_username = "email_utilizado no smtp"
    smtp_password = "senha de app do google para envio smtp"

    # Criar a mensagem de e-mail
    msg = EmailMessage()
    msg["From"] = smtp_username
    msg["Subject"] = assunto
    msg["To"] = ", ".join(destinatarios)
    msg.set_content(mensagem)

    # Enviar o e-mail
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.send_message(msg)

    print(f"O e-mail foi enviado para {', '.join(destinatarios)} com sucesso!")
