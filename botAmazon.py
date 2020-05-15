import requests
from bs4 import BeautifulSoup
import smtplib
import time
import getpass


URL = input("Por favor ingrese una url de amazon:")
precioDeseado= int(input('Ingrese el precio deseado:'))
email = input("Ingrese su email (gmail:)")
password = getpass.getpass('Password:')
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0'}


def checkearPrecio():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'lxml')
    title =soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    price = (price[0: (len(price)-5)])
    price = price.replace('.', '')
    price = int(price)
    print(title.strip())
    print (price)
    if(price < precioDeseado ):
        sendMail(title, price, precioDeseado)
    else:
        print('Volve Mañana')

def sendMail(title, price,precioDeseado):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login( email, password)
    subject = 'BAJO EL PRECIO DEL PRODUCTO'
    body = f'ENTRA AL LINK DE AMAZON QUE BAJO EL PRECIO DE {title.strip()} ESTABA:{price} y AHORA ESTA MENOS QUE: {precioDeseado} \n\n {URL}'
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
        'matiasamazonprice@gmail.com',
        'matias_rodriguez_t@hotmail.com',
        msg
    )

    print('El email ha sido enviado')
    server.quit()

checkearPrecio()