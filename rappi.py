import sys
from random import randint
from os import system
import datetime
import random
system("clear")

print("\n")
print("\033[1;34m (              (    (    (")     
print("\033[1;34m )\ )    (      )\ ) )\ ) )\ )")  
print("\033[1;37m(()/(    )\    (()/((()/((()/(")  
print("\033[1;37m /(_))((((_)(   /(_))/(_))/(_))") 
print("\033[1;34m(_))   )\ \033[1;32m_ \033[1;34m)\ (_)) (_)) (_))")   
print("\033[1;32m| _ \  \033[1;34m(_\033[1;34m)\033[1;32m_\033[1;34m(_) \033[1;32m| _ \| _ \|_ _|")  
print("\033[1;32m|   /   / _ \  |  _/|  _/ | |")   
print("\033[1;32m|_|_\  /_/ \_\ |_|  |_|  |___|")  
print("")                               
print("\033[1;31m                      ___")
print("\033[1;36m       HBO MAX       \033[1;31m/\*/\ ")
print("\033[1;36m      SUSCRIPCIÓN   \033[1;31m/(o o)\ ")
print("\033[1;36m                      \033[1;31m(_)")
print("")
print("\033[1;36m/* Nota: \033[1;37mIntenten generar el bin")
print("\033[1;37mcon generadas o saca live pa calar")
print("")
system("sleep 3")

bin_format = "4697000002xx"

def esValido(num_tarjeta):
  suma = 0
  num_digitos = len(num_tarjeta)
  pos_par_impar = num_digitos & 1

  for i in range(0, num_digitos):
    digito = int(num_tarjeta[i])
    if not ((i & 1) ^ pos_par_impar):
      digito = digito * 2
    if digito > 9:
      digito = digito - 9
    suma = suma + digito

  return (suma % 10 == 0)

def generar_cc(bin_format):
  cc = ""
  if len(bin_format) == 12:
    for i in range(11):
      if bin_format[i] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
        cc += bin_format[i]
        continue
      elif bin_format[i] == "x":
        cc += str(randint(0, 9))
      else:
        print("\nCaracter no valido en el formato: {}\n".format(bin_format))
        print("El formato del bin es: xxxxxxxxxxxxxxxx de 16 digitos\n")
        sys.exit()

    for i in range(10):
      verificador = cc + str(i)
      if esValido(verificador):
        cc = verificador
        break
      else:
        verificador = cc

  else:
    print("\nERROR: Inserte un bin válido\n")
    print("SOLUCIÓN: El formato del bin es: xxxxxxxxxxxxxxxx de 16 dígitos\n")
    sys.exit()

  return cc


def dategen():
  now = datetime.datetime.now()
  date = ""
  month = str(randint(1, 9))
  current_year = str(now.year)
  year = str(randint(int(current_year[-2:]) + 1, int(current_year[-2:]) + 6))
  date = month + "/" + year

  return date


def ccv_gen():
  ccv = ""
  num = randint(10, 999)
  ccv = "0" + str(num) if num < 100 else str(num)
  return ccv

def main():
 cc = generar_cc(bin_format)
 print("\033[1;31m=======\033[1;32mBIN #1\033[1;31m=======")
 print(f"\033[1;34mBIN : \033[1;37m{cc}xxxx")
 print(f"\033[1;34mFECHA : \033[1;37m{dategen()}")
 print(f"\033[1;34mCVV : \033[1;37mgnd")
main()
print("\n")

bin_format = "4697000002xx"

def esValido(num_tarjeta):
  suma = 0
  num_digitos = len(num_tarjeta)
  pos_par_impar = num_digitos & 1

  for i in range(0, num_digitos):
    digito = int(num_tarjeta[i])
    if not ((i & 1) ^ pos_par_impar):
      digito = digito * 2
    if digito > 9:
      digito = digito - 9
    suma = suma + digito

  return (suma % 10 == 0)

def generar_cc(bin_format):
  cc = ""
  if len(bin_format) == 12:
    for i in range(11):
      if bin_format[i] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
        cc += bin_format[i]
        continue
      elif bin_format[i] == "x":
        cc += str(randint(0, 9))
      else:
        print("\nCaracter no valido en el formato: {}\n".format(bin_format))
        print("El formato del bin es: xxxxxxxxxxxxxxxx de 16 digitos\n")
        sys.exit()

    for i in range(10):
      verificador = cc + str(i)
      if esValido(verificador):
        cc = verificador
        break
      else:
        verificador = cc

  else:
    print("\nERROR: Inserte un bin válido\n")
    print("SOLUCIÓN: El formato del bin es: xxxxxxxxxxxxxxxx de 16 dígitos\n")
    sys.exit()

  return cc


def dategen():
  now = datetime.datetime.now()
  date = ""
  month = str(randint(1, 9))
  current_year = str(now.year)
  year = str(randint(int(current_year[-2:]) + 1, int(current_year[-2:]) + 6))
  date = month + "/" + year

  return date


def ccv_gen():
  ccv = ""
  num = randint(10, 999)
  ccv = "0" + str(num) if num < 100 else str(num)
  return ccv

def main():
 cc = generar_cc(bin_format)
 print("\033[1;31m=======\033[1;32mBIN #2\033[1;31m=======")
 print(f"\033[1;34mBIN : \033[1;37m{cc}xxxx")
 print(f"\033[1;34mFECHA : \033[1;37m{dategen()}")
 print(f"\033[1;34mCVV : \033[1;37mgnd")
main()
print("\n")

bin_format = "4697000002xx"

def esValido(num_tarjeta):
  suma = 0
  num_digitos = len(num_tarjeta)
  pos_par_impar = num_digitos & 1

  for i in range(0, num_digitos):
    digito = int(num_tarjeta[i])
    if not ((i & 1) ^ pos_par_impar):
      digito = digito * 2
    if digito > 9:
      digito = digito - 9
    suma = suma + digito

  return (suma % 10 == 0)

def generar_cc(bin_format):
  cc = ""
  if len(bin_format) == 12:
    for i in range(11):
      if bin_format[i] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
        cc += bin_format[i]
        continue
      elif bin_format[i] == "x":
        cc += str(randint(0, 9))
      else:
        print("\nCaracter no valido en el formato: {}\n".format(bin_format))
        print("El formato del bin es: xxxxxxxxxxxxxxxx de 16 digitos\n")
        sys.exit()

    for i in range(10):
      verificador = cc + str(i)
      if esValido(verificador):
        cc = verificador
        break
      else:
        verificador = cc

  else:
    print("\nERROR: Inserte un bin válido\n")
    print("SOLUCIÓN: El formato del bin es: xxxxxxxxxxxxxxxx de 16 dígitos\n")
    sys.exit()

  return cc


def dategen():
  now = datetime.datetime.now()
  date = ""
  month = str(randint(1, 9))
  current_year = str(now.year)
  year = str(randint(int(current_year[-2:]) + 1, int(current_year[-2:]) + 6))
  date = month + "/" + year

  return date


def ccv_gen():
  ccv = ""
  num = randint(10, 999)
  ccv = "0" + str(num) if num < 100 else str(num)
  return ccv

def main():
 cc = generar_cc(bin_format)
 print("\033[1;31m=======\033[1;32mBIN #3\033[1;31m=======")
 print(f"\033[1;34mBIN : \033[1;37m{cc}xxxx")
 print(f"\033[1;34mFECHA : \033[1;37m{dategen()}")
 print(f"\033[1;34mCVV : \033[1;37mgnd")
main()
print("\n")

bin_format = "4697000002xx"

def esValido(num_tarjeta):
  suma = 0
  num_digitos = len(num_tarjeta)
  pos_par_impar = num_digitos & 1

  for i in range(0, num_digitos):
    digito = int(num_tarjeta[i])
    if not ((i & 1) ^ pos_par_impar):
      digito = digito * 2
    if digito > 9:
      digito = digito - 9
    suma = suma + digito

  return (suma % 10 == 0)

def generar_cc(bin_format):
  cc = ""
  if len(bin_format) == 12:
    for i in range(11):
      if bin_format[i] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
        cc += bin_format[i]
        continue
      elif bin_format[i] == "x":
        cc += str(randint(0, 9))
      else:
        print("\nCaracter no valido en el formato: {}\n".format(bin_format))
        print("El formato del bin es: xxxxxxxxxxxxxxxx de 16 digitos\n")
        sys.exit()

    for i in range(10):
      verificador = cc + str(i)
      if esValido(verificador):
        cc = verificador
        break
      else:
        verificador = cc

  else:
    print("\nERROR: Inserte un bin válido\n")
    print("SOLUCIÓN: El formato del bin es: xxxxxxxxxxxxxxxx de 16 dígitos\n")
    sys.exit()

  return cc


def dategen():
  now = datetime.datetime.now()
  date = ""
  month = str(randint(1, 9))
  current_year = str(now.year)
  year = str(randint(int(current_year[-2:]) + 1, int(current_year[-2:]) + 6))
  date = month + "/" + year

  return date


def ccv_gen():
  ccv = ""
  num = randint(10, 999)
  ccv = "0" + str(num) if num < 100 else str(num)
  return ccv

def main():
 cc = generar_cc(bin_format)
 print("\033[1;31m=======\033[1;32mBIN #4\033[1;31m=======")
 print(f"\033[1;34mBIN : \033[1;37m{cc}xxxx")
 print(f"\033[1;34mFECHA : \033[1;37m{dategen()}")
 print(f"\033[1;34mCVV : \033[1;37mgnd")
main()
print("\n")

bin_format = "4697000002xx"

def esValido(num_tarjeta):
  suma = 0
  num_digitos = len(num_tarjeta)
  pos_par_impar = num_digitos & 1

  for i in range(0, num_digitos):
    digito = int(num_tarjeta[i])
    if not ((i & 1) ^ pos_par_impar):
      digito = digito * 2
    if digito > 9:
      digito = digito - 9
    suma = suma + digito

  return (suma % 10 == 0)

def generar_cc(bin_format):
  cc = ""
  if len(bin_format) == 12:
    for i in range(11):
      if bin_format[i] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
        cc += bin_format[i]
        continue
      elif bin_format[i] == "x":
        cc += str(randint(0, 9))
      else:
        print("\nCaracter no valido en el formato: {}\n".format(bin_format))
        print("El formato del bin es: xxxxxxxxxxxxxxxx de 16 digitos\n")
        sys.exit()

    for i in range(10):
      verificador = cc + str(i)
      if esValido(verificador):
        cc = verificador
        break
      else:
        verificador = cc

  else:
    print("\nERROR: Inserte un bin válido\n")
    print("SOLUCIÓN: El formato del bin es: xxxxxxxxxxxxxxxx de 16 dígitos\n")
    sys.exit()

  return cc


def dategen():
  now = datetime.datetime.now()
  date = ""
  month = str(randint(1, 9))
  current_year = str(now.year)
  year = str(randint(int(current_year[-2:]) + 1, int(current_year[-2:]) + 6))
  date = month + "/" + year

  return date


def ccv_gen():
  ccv = ""
  num = randint(10, 999)
  ccv = "0" + str(num) if num < 100 else str(num)
  return ccv

def main():
 cc = generar_cc(bin_format)
 print("\033[1;31m=======\033[1;32mBIN #5\033[1;31m=======")
 print(f"\033[1;34mBIN : \033[1;37m{cc}xxxx")
 print(f"\033[1;34mFECHA : \033[1;37m{dategen()}")
 print(f"\033[1;34mCVV : \033[1;37mgnd")
main()
print("\n")

bin_format = "4697000002xx"

def esValido(num_tarjeta):
  suma = 0
  num_digitos = len(num_tarjeta)
  pos_par_impar = num_digitos & 1

  for i in range(0, num_digitos):
    digito = int(num_tarjeta[i])
    if not ((i & 1) ^ pos_par_impar):
      digito = digito * 2
    if digito > 9:
      digito = digito - 9
    suma = suma + digito

  return (suma % 10 == 0)

def generar_cc(bin_format):
  cc = ""
  if len(bin_format) == 12:
    for i in range(11):
      if bin_format[i] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
        cc += bin_format[i]
        continue
      elif bin_format[i] == "x":
        cc += str(randint(0, 9))
      else:
        print("\nCaracter no valido en el formato: {}\n".format(bin_format))
        print("El formato del bin es: xxxxxxxxxxxxxxxx de 16 digitos\n")
        sys.exit()

    for i in range(10):
      verificador = cc + str(i)
      if esValido(verificador):
        cc = verificador
        break
      else:
        verificador = cc

  else:
    print("\nERROR: Inserte un bin válido\n")
    print("SOLUCIÓN: El formato del bin es: xxxxxxxxxxxxxxxx de 16 dígitos\n")
    sys.exit()

  return cc


def dategen():
  now = datetime.datetime.now()
  date = ""
  month = str(randint(1, 9))
  current_year = str(now.year)
  year = str(randint(int(current_year[-2:]) + 1, int(current_year[-2:]) + 6))
  date = month + "/" + year

  return date


def ccv_gen():
  ccv = ""
  num = randint(10, 999)
  ccv = "0" + str(num) if num < 100 else str(num)
  return ccv

def main():
 cc = generar_cc(bin_format)
 print("\033[1;31m=======\033[1;32mBIN #6\033[1;31m=======")
 print(f"\033[1;34mBIN : \033[1;37m{cc}xxxx")
 print(f"\033[1;34mFECHA : \033[1;37m{dategen()}")
 print(f"\033[1;34mCVV : \033[1;37mgnd")
main()
print("\n")

bin_format = "4697000002xx"

def esValido(num_tarjeta):
  suma = 0
  num_digitos = len(num_tarjeta)
  pos_par_impar = num_digitos & 1

  for i in range(0, num_digitos):
    digito = int(num_tarjeta[i])
    if not ((i & 1) ^ pos_par_impar):
      digito = digito * 2
    if digito > 9:
      digito = digito - 9
    suma = suma + digito

  return (suma % 10 == 0)

def generar_cc(bin_format):
  cc = ""
  if len(bin_format) == 12:
    for i in range(11):
      if bin_format[i] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
        cc += bin_format[i]
        continue
      elif bin_format[i] == "x":
        cc += str(randint(0, 9))
      else:
        print("\nCaracter no valido en el formato: {}\n".format(bin_format))
        print("El formato del bin es: xxxxxxxxxxxxxxxx de 16 digitos\n")
        sys.exit()

    for i in range(10):
      verificador = cc + str(i)
      if esValido(verificador):
        cc = verificador
        break
      else:
        verificador = cc

  else:
    print("\nERROR: Inserte un bin válido\n")
    print("SOLUCIÓN: El formato del bin es: xxxxxxxxxxxxxxxx de 16 dígitos\n")
    sys.exit()

  return cc


def dategen():
  now = datetime.datetime.now()
  date = ""
  month = str(randint(1, 9))
  current_year = str(now.year)
  year = str(randint(int(current_year[-2:]) + 1, int(current_year[-2:]) + 6))
  date = month + "/" + year

  return date


def ccv_gen():
  ccv = ""
  num = randint(10, 999)
  ccv = "0" + str(num) if num < 100 else str(num)
  return ccv

def main():
 cc = generar_cc(bin_format)
 print("\033[1;31m=======\033[1;32mBIN #7\033[1;31m=======")
 print(f"\033[1;34mBIN : \033[1;37m{cc}xxxx")
 print(f"\033[1;34mFECHA : \033[1;37m{dategen()}")
 print(f"\033[1;34mCVV : \033[1;37mgnd")
main()
print("\n")

bin_format = "4697000002xx"

def esValido(num_tarjeta):
  suma = 0
  num_digitos = len(num_tarjeta)
  pos_par_impar = num_digitos & 1

  for i in range(0, num_digitos):
    digito = int(num_tarjeta[i])
    if not ((i & 1) ^ pos_par_impar):
      digito = digito * 2
    if digito > 9:
      digito = digito - 9
    suma = suma + digito

  return (suma % 10 == 0)

def generar_cc(bin_format):
  cc = ""
  if len(bin_format) == 12:
    for i in range(11):
      if bin_format[i] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
        cc += bin_format[i]
        continue
      elif bin_format[i] == "x":
        cc += str(randint(0, 9))
      else:
        print("\nCaracter no valido en el formato: {}\n".format(bin_format))
        print("El formato del bin es: xxxxxxxxxxxxxxxx de 16 digitos\n")
        sys.exit()

    for i in range(10):
      verificador = cc + str(i)
      if esValido(verificador):
        cc = verificador
        break
      else:
        verificador = cc

  else:
    print("\nERROR: Inserte un bin válido\n")
    print("SOLUCIÓN: El formato del bin es: xxxxxxxxxxxxxxxx de 16 dígitos\n")
    sys.exit()

  return cc


def dategen():
  now = datetime.datetime.now()
  date = ""
  month = str(randint(1, 9))
  current_year = str(now.year)
  year = str(randint(int(current_year[-2:]) + 1, int(current_year[-2:]) + 6))
  date = month + "/" + year

  return date


def ccv_gen():
  ccv = ""
  num = randint(10, 999)
  ccv = "0" + str(num) if num < 100 else str(num)
  return ccv

def main():
 cc = generar_cc(bin_format)
 print("\033[1;31m=======\033[1;32mBIN #8\033[1;31m=======")
 print(f"\033[1;34mBIN : \033[1;37m{cc}xxxx")
 print(f"\033[1;34mFECHA : \033[1;37m{dategen()}")
 print(f"\033[1;34mCVV : \033[1;37mgnd")
main()
print("\n")

bin_format = "4697000002xx"

def esValido(num_tarjeta):
  suma = 0
  num_digitos = len(num_tarjeta)
  pos_par_impar = num_digitos & 1

  for i in range(0, num_digitos):
    digito = int(num_tarjeta[i])
    if not ((i & 1) ^ pos_par_impar):
      digito = digito * 2
    if digito > 9:
      digito = digito - 9
    suma = suma + digito

  return (suma % 10 == 0)

def generar_cc(bin_format):
  cc = ""
  if len(bin_format) == 12:
    for i in range(11):
      if bin_format[i] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
        cc += bin_format[i]
        continue
      elif bin_format[i] == "x":
        cc += str(randint(0, 9))
      else:
        print("\nCaracter no valido en el formato: {}\n".format(bin_format))
        print("El formato del bin es: xxxxxxxxxxxxxxxx de 16 digitos\n")
        sys.exit()

    for i in range(10):
      verificador = cc + str(i)
      if esValido(verificador):
        cc = verificador
        break
      else:
        verificador = cc

  else:
    print("\nERROR: Inserte un bin válido\n")
    print("SOLUCIÓN: El formato del bin es: xxxxxxxxxxxxxxxx de 16 dígitos\n")
    sys.exit()

  return cc


def dategen():
  now = datetime.datetime.now()
  date = ""
  month = str(randint(1, 9))
  current_year = str(now.year)
  year = str(randint(int(current_year[-2:]) + 1, int(current_year[-2:]) + 6))
  date = month + "/" + year

  return date


def ccv_gen():
  ccv = ""
  num = randint(10, 999)
  ccv = "0" + str(num) if num < 100 else str(num)
  return ccv

def main():
 cc = generar_cc(bin_format)
 print("\033[1;31m=======\033[1;32mBIN #9\033[1;31m=======")
 print(f"\033[1;34mBIN : \033[1;37m{cc}xxxx")
 print(f"\033[1;34mFECHA : \033[1;37m{dategen()}")
 print(f"\033[1;34mCVV : \033[1;37mgnd")
main()
print("\n")

bin_format = "4697000002xx"

def esValido(num_tarjeta):
  suma = 0
  num_digitos = len(num_tarjeta)
  pos_par_impar = num_digitos & 1

  for i in range(0, num_digitos):
    digito = int(num_tarjeta[i])
    if not ((i & 1) ^ pos_par_impar):
      digito = digito * 2
    if digito > 9:
      digito = digito - 9
    suma = suma + digito

  return (suma % 10 == 0)

def generar_cc(bin_format):
  cc = ""
  if len(bin_format) == 12:
    for i in range(11):
      if bin_format[i] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
        cc += bin_format[i]
        continue
      elif bin_format[i] == "x":
        cc += str(randint(0, 9))
      else:
        print("\nCaracter no valido en el formato: {}\n".format(bin_format))
        print("El formato del bin es: xxxxxxxxxxxxxxxx de 16 digitos\n")
        sys.exit()

    for i in range(10):
      verificador = cc + str(i)
      if esValido(verificador):
        cc = verificador
        break
      else:
        verificador = cc

  else:
    print("\nERROR: Inserte un bin válido\n")
    print("SOLUCIÓN: El formato del bin es: xxxxxxxxxxxxxxxx de 16 dígitos\n")
    sys.exit()

  return cc


def dategen():
  now = datetime.datetime.now()
  date = ""
  month = str(randint(1, 9))
  current_year = str(now.year)
  year = str(randint(int(current_year[-2:]) + 1, int(current_year[-2:]) + 6))
  date = month + "/" + year

  return date


def ccv_gen():
  ccv = ""
  num = randint(10, 999)
  ccv = "0" + str(num) if num < 100 else str(num)
  return ccv

def main():
 cc = generar_cc(bin_format)
 print("\033[1;31m=======\033[1;32mBIN #10\033[1;31m=======")
 print(f"\033[1;34mBIN : \033[1;37m{cc}xxxx")
 print(f"\033[1;34mFECHA : \033[1;37m{dategen()}")
 print(f"\033[1;34mCVV : \033[1;37mgnd")
main()


