import random

print("✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿")
print("► (Bienvenido al juego del AHORCADO!)> (´｡• ω •｡`)")

palabra1 = "casa"
palabra2 = "cocodrilo"
palabra3 = "xantofobia"

dicc_palabras = {"casa": 1, "cocodrilo": 2, "xantofobia": 3}
palabra_random = random.randint(1,3)
if palabra_random == 1:
    print(f"La palabra contiene {len(palabra1)} letras")

else:
    if palabra_random == 2:
        print(f"La palabra contiene {len(palabra2)} letras")

    else:
        print(f"La palabra contiene {len(palabra3)} letras")

adivinar_casa = ["c","a","s","a"]
lista_casa = ["-","-","-","-"]
adivinar_2 = ["c", "o", "c", "o", "d", "r", "i", "l", "o"]
lista2 = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
adivinar_3 = ["x", "a", "n", "t", "o", "f", "o", "b", "i", "a"]
lista3 = ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]

lista_vacia = []

vida = 5

def guion(letra):
    if palabra_random == 1:
        print(lista_casa)
    elif palabra_random == 2:
        print(lista2)
    else:
        print(lista3)

def validar_letra(letra):
    while True:
        letra = input()
        if len(letra) >= 2 or len(letra) < 1 or letra == " " or not letra.isalpha():
          print("Estas intentando romper mi juego? :(")
          print("Recuerde ingresar una única letra para poder jugar. No es tán difícil ;)")
        elif letra in lista_vacia or letra in lista_casa or letra in lista2 or letra in lista3: #ver si funciona que no repita letras en esta lista
           print("Letra ya ingresada. Pensá en otra :)")
        else:
          break
    return letra.lower()

def adivinar(letra):
      if letra == "a":
         lista_casa[1] = "a"
         lista_casa[3] = "a"
      elif letra == "s":
           lista_casa[2] = "s"
      elif letra == "c":
           lista_casa[0] = "c"
      else:
           print("══════════════════════════")
           print("(No se encontro la letra...)> (ಥ﹏ಥ) ")
           guardar(letra)
           print("══════════════════════════")
           print(lista_vacia)
           descontar_vida(letra)
      return lista_casa

def adivinar2(letra):
      if letra == "c":
         lista2[0] = "c"
         lista2[2] = "c"
      elif letra.lower() == "o":
         lista2[1] = "o"
         lista2[3] = "o"
         lista2[8] = "o"
      elif letra == "d":
           lista2[4] = "d"
      elif letra == "r":
           lista2[5] = "r"
      elif letra == "i":
           lista2[6] = "i"
      elif letra == "l":
           lista2[7] = "l"

      else:
           print("══════════════════════════")
           print("(No se encontro la letra...)> (ಥ﹏ಥ) ")
           guardar(letra)
           print("══════════════════════════")
           print(lista_vacia)
           descontar_vida2(letra)

      return lista2

def adivinar3(letra):
      if letra.lower() == "o":
         lista3[4] = "o"
         lista3[6] = "o"

      elif letra.lower() == "a":
          lista3[1] = "a"
          lista3[9] = "a"

      elif letra.lower() == "x":
           lista3[0] = "x"
      elif letra.lower() == "n":
           lista3[2] = "n"
      elif letra.lower() == "t":
           lista3[3] = "t"
      elif letra.lower() == "f":
           lista3[5] = "f"
      elif letra.lower() == "b":
           lista3[7] = "b"
      elif letra.lower() == "i":
           lista3[8] = "i"

      else:
           print("══════════════════════════")
           print("(No se encontro la letra...)> (ಥ﹏ಥ) ")
           guardar(letra)
           print("══════════════════════════")
           print(lista_vacia)
           descontar_vida3(letra)
      
      return lista3

def guardar(letra):
     letra_i = lista_vacia.append(letra) #letra_i = letras incorrectas
     return letra_i

def descontar_vida(letra):
    global vida
    if letra == "a" or letra == "s" or letra == "c":
        pass
    else:
        vida -= 1
        print(f"► (Tienes {vida} vidas restantes! ♥♥♡)> (´• ω •`) ")

def descontar_vida2(letra):
    global vida
    if letra == "c" or letra == "o" or letra == "d" or letra == "r" or letra == "i" or letra == "l":
        pass
    else:
        vida -= 1
        print(f"► (Tienes {vida} vidas restantes! ♥♥♡)> (´• ω •`) ")

def descontar_vida3(letra):
    global vida
    if letra == "o" or letra == "a" or letra == "x" or letra == "n" or letra == "t" or letra == "f" or letra == "b" or letra == "i":
        pass
    else:
        vida -= 1
        print(f"► (Tienes {vida} vidas restantes! ♥♥♡)> (´• ω •`) ")

def resultado():
    if palabra_random == 1:
        re_1 = list(filter(adivinar, letra))
    elif palabra_random == 2:
        re_2 = list(filter(adivinar2, letra))
    elif palabra_random == 3:
        re_3 = list(filter(adivinar3, letra))
    

while True:
      print("══════════════════════════")
      print("► Ingrese una letra: ")
      letra = validar_letra("")
      
      resultado()
      guion(letra)

      if adivinar_casa == lista_casa:
          print("► (Lo hiciste!! \nAdivinaste la palabra!!)> (o´▽`o)♥")
          print("✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿")
          break
      elif adivinar_2 == lista2:
          print("► (Lo hiciste!! \nAdivinaste la palabra!!)> (o´▽`o)♥")
          print("✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿")
          break
      elif adivinar_3 == lista3:
          print("► (Lo hiciste!! \nAdivinaste la palabra!!)> (o´▽`o)♥")
          print("✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿")
          break
      elif len(lista_vacia) == vida or vida == 0:
          print("► (Game Over)> (×_×)")
          print("✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿")
          break