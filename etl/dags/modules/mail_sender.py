import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def enviar_mail(**context):
    subject = context["var"]["value"].get("subject_mail")
    from_address = context["var"]["value"].get("email")
    password = context["var"]["value"].get("email_password")
    to_address = context["var"]["value"].get("to_address")

    # Creando a MIMEText object
    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = subject

    # Creando un HTML content
    html_content = f"""
    <html>
    <body>
        <p>Hola!</p>
        <p>El proceso de extraccion y de carga a redshift ha sido realizado con exito</p>
    </body>
    </html>
    """

    # Adjuntar contenido HTML
    msg.attach(MIMEText(html_content, 'html'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)  
        server.starttls() 

        server.login(from_address, password)

        text = msg.as_string()
        server.sendmail(from_address, to_address, text)
        server.quit()
        print("Email enviado exitosamente")
    except Exception as e:
        print(f"Error al enviar el mail: {str(e)}")