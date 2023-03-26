import sys
from random import randint
from os import system
import datetime
import random

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
print("\033[1;36m/* Nota: \033[1;37mIntenta generar el bin")
print("\033[1;37mcon generadas o saca live pa calar")
print("")
system("sleep 3")

bin_formati = "469700000225xxxx"

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
 print("\033[1;31m=======\033[1;37mBIN #1\033[1;31m=======")
 print(f"\033[1;34mBIN : \033[1;32m469700000225xxxx")
 print(f"\033[1;34mFECHA : \033[1;32m4/23")
 print(f"\033[1;34mCVV : \033[1;32mgnd")
main()
print("\n")

bin_formati = "469700000277xxxx"

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
 print("\033[1;31m=======\033[1;37mBIN #2\033[1;31m=======")
 print(f"\033[1;34mBIN : \033[1;32m469700000277xxxx")
 print(f"\033[1;34mFECHA : \033[1;32m7/24")
 print(f"\033[1;34mCVV : \033[1;32mgnd")
main()
print("\n")

bin_formati = "46970000027xxxxx"

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
 print("\033[1;31m=======\033[1;37mBIN #3\033[1;31m=======")
 print(f"\033[1;34mBIN : \033[1;32m46970000027xxxxx")
 print(f"\033[1;34mFECHA : \033[1;32m6/26")
 print(f"\033[1;34mCVV : \033[1;32mgnd")
main()
print("\n")

bin_format = "4697000002xxxxxx"

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
  if len(bin_format) == 16:
    for i in range(15):
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
 print("\033[1;31m=======\033[1;37mBIN #4\033[1;31m=======")
 print(f"\033[1;34mBIN : \033[1;35m{cc}")
 print(f"\033[1;34mFECHA : \033[1;35m{dategen()}")
 print(f"\033[1;34mCVV : \033[1;35mgnd")
main()
print("\n")

bin_format = "46970000027xxxxx"

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
  if len(bin_format) == 16:
    for i in range(15):
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
 print("\033[1;31m=======\033[1;37mBIN #5\033[1;31m=======")
 print(f"\033[1;34mBIN : \033[1;33m{cc}")
 print(f"\033[1;34mFECHA : \033[1;33m{dategen()}")
 print(f"\033[1;34mCVV : \033[1;33mgnd")
main()
print("\n")

bin_formati = "4548320027xxxxxx"

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
 print("\033[1;31m=======\033[1;37mBIN #6\033[1;31m=======")
 print(f"\033[1;34mBIN : \033[1;32m4548320027xxxxxx")
 print(f"\033[1;34mFECHA : \033[1;32m3/25")
 print(f"\033[1;34mCVV : \033[1;32mgnd")
main()
print("\n")

bin_format = "454832002xxxxxxx"

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
  if len(bin_format) == 16:
    for i in range(15):
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
 print("\033[1;31m=======\033[1;37mBIN #7\033[1;31m=======")
 print(f"\033[1;34mBIN : \033[1;35m{cc}")
 print(f"\033[1;34mFECHA : \033[1;35m{dategen()}")
 print(f"\033[1;34mCVV : \033[1;35mgnd")
main()
print("\n")

bin_formati = "454832002728xxxx"

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
 print("\033[1;31m=======\033[1;37mBIN #8\033[1;31m=======")
 print(f"\033[1;34mBIN : \033[1;32m454832002728xxxx")
 print(f"\033[1;34mFECHA : \033[1;32m5/23")
 print(f"\033[1;34mCVV : \033[1;32mgnd")
main()
print("\n")

bin_formati = "454832002728xxxx"

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
 print("\033[1;31m=======\033[1;37mBIN #9\033[1;31m=======")
 print(f"\033[1;34mBIN : \033[1;32m454832002728xxxx")
 print(f"\033[1;34mFECHA : \033[1;32m3/25")
 print(f"\033[1;34mCVV : \033[1;32mgnd")
main()
print("\n")

bin_formati = "45407500671xxxxx"

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
 print("\033[1;31m=======\033[1;37mBIN #10\033[1;31m=======")
 print(f"\033[1;34mBIN : \033[1;32m45407500671xxxxx")
 print(f"\033[1;34mFECHA : \033[1;32m6/27")
 print(f"\033[1;34mCVV : \033[1;32mgnd")
main()
print("\n")

bin_format = "4540750067xxxxxx"

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
  if len(bin_format) == 16:
    for i in range(15):
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
 print("\033[1;31m=======\033[1;37mBIN #11\033[1;31m=======")
 print(f"\033[1;34mBIN : \033[1;33m{cc}")
 print(f"\033[1;34mFECHA : \033[1;33m{dategen()}")
 print(f"\033[1;34mCVV : \033[1;33mgnd")
main()
print("\n")

bin_format = "454075006xxxxxxx"

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
  if len(bin_format) == 16:
    for i in range(15):
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
 print("\033[1;31m=======\033[1;37mBIN #12\033[1;31m=======")
 print(f"\033[1;34mBIN : \033[1;35m{cc}")
 print(f"\033[1;34mFECHA : \033[1;35m{dategen()}")
 print(f"\033[1;34mCVV : \033[1;35mgnd")
main()
print("\n")

bin_format = "454640007xxxxxxx"

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
  if len(bin_format) == 16:
    for i in range(15):
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
 print("\033[1;31m=======\033[1;37mBIN #13\033[1;31m=======")
 print(f"\033[1;34mBIN : \033[1;35m{cc}")
 print(f"\033[1;34mFECHA : \033[1;35m{dategen()}")
 print(f"\033[1;34mCVV : \033[1;35mgnd")
main()
print("\n")

bin_format = "4546408005xxxxxx"

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
  if len(bin_format) == 16:
    for i in range(15):
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
 print("\033[1;31m=======\033[1;37mBIN #14\033[1;31m=======")
 print(f"\033[1;34mBIN : \033[1;33m{cc}")
 print(f"\033[1;34mFECHA : \033[1;33m{dategen()}")
 print(f"\033[1;34mCVV : \033[1;33mgnd")
main()
print("\n")

bin_format = "454640800xxxxxxx"

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
  if len(bin_format) == 16:
    for i in range(15):
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
 print("\033[1;31m=======\033[1;37mBIN #15\033[1;31m=======")
 print(f"\033[1;34mBIN : \033[1;35m{cc}")
 print(f"\033[1;34mFECHA : \033[1;35m{dategen()}")
 print(f"\033[1;34mCVV : \033[1;35mgnd")
main()
print("\n")

bin_formati = "43383080016xxxxx"

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
 print("\033[1;31m=======\033[1;37mBIN #16\033[1;31m=======")
 print(f"\033[1;34mBIN : \033[1;32m43383080016xxxxx")
 print(f"\033[1;34mFECHA : \033[1;32m9/23")
 print(f"\033[1;34mCVV : \033[1;32mgnd")
main()
print("\n")

bin_formati = "433830800164xxxx"

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
 print("\033[1;31m=======\033[1;37mBIN #17\033[1;31m=======")
 print(f"\033[1;34mBIN : \033[1;32m433830800164xxxx")
 print(f"\033[1;34mFECHA : \033[1;32m9/23")
 print(f"\033[1;34mCVV : \033[1;32mgnd")
main()
print("\n")

bin_format = "43383080016xxxxx"

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
  if len(bin_format) == 16:
    for i in range(15):
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
 print("\033[1;31m=======\033[1;37mBIN #18\033[1;31m=======")
 print(f"\033[1;34mBIN : \033[1;33m{cc}")
 print(f"\033[1;34mFECHA : \033[1;33m{dategen()}")
 print(f"\033[1;34mCVV : \033[1;33mgnd")
main()
print("\n")

bin_format = "4338308001xxxxxx"

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
  if len(bin_format) == 16:
    for i in range(15):
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
 print("\033[1;31m=======\033[1;37mBIN #19\033[1;31m=======")
 print(f"\033[1;34mBIN : \033[1;33m{cc}")
 print(f"\033[1;34mFECHA : \033[1;33m{dategen()}")
 print(f"\033[1;34mCVV : \033[1;33mgnd")
main()
print("\n")

bin_format = "433830800xxxxxxx"

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
  if len(bin_format) == 16:
    for i in range(15):
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
 print("\033[1;31m=======\033[1;37mBIN #20\033[1;31m=======")
 print(f"\033[1;34mBIN : \033[1;35m{cc}")
 print(f"\033[1;34mFECHA : \033[1;35m{dategen()}")
 print(f"\033[1;34mCVV : \033[1;35mgnd")
main()
print("\n")
print("\033[1;31m`0-0-'`-0-0-'`-0-0-'`-0-0-'`-0-0-'`0-0-'")
print("  `0-0-'`-0-0-'`-0-0-'`-0-0-'`-0-0-'")
print("")
print("\033[1;34mBIN VALIDOS     = \033[1;37mCOLOR \033[1;32mVERDE")
print("\033[1;34mBIN CERCANOS    = \033[1;37mCOLOR \033[1;33mAMARILLO")
print("\033[1;34mBIN APROXIMADOS = \033[1;37mCOLOR \033[1;35mPURPURA")
print("")
print("\033[1;37mLOS BIN \033[1;33mAMARILLOS \033[1;37mY \033[1;35mPURPURAS \033[1;37mTIENEN")
print("QUE EXTRAPOLARLE LA CC GENERADA")
print("")
print("\033[1;34m=================================")
print("\033[1;34mEJEMPLO     : \033[1;31m4338308001662180")
print("\033[1;34mEXTRAPOLADO : \033[1;36m433830800166xxxx")
print("\033[1;34mEXTRAPOLADO : \033[1;36m43383080016xxxxx")
print("\033[1;34mEXTRAPOLADO : \033[1;36m4338308001xxxxxx")
print("")
print("\033[1;37mLA FECHA QUEDARA IGUAL, CON LA CVV SIN GENERAR")
print("\033[1;37mGENERA LOS BIN O SACA LIVE PARA CALAR MEJOR")

