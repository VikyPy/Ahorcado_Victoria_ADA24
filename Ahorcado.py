import random

print("✿✿✿✿✿✿✿✿✿✿✿")
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
        elif letra in lista_vacia: #ver si funciona que no repita letras en esta lista
           print("Letra ya ingresada. Pensá en otra :)")
        else:
          break
    return letra.lower()

def adivinar(letra):
      if letra.lower() == "a":
         lista_casa[1] = "a"
         lista_casa[3] = "a"

      elif letra.lower() == "s":
         lista_casa[2] = "s"
      elif letra.lower() == "c":
           lista_casa[0] = "c"
      else:
           print("══════════════════════════")
           print("(No se encontro la letra...)> (ಥ﹏ಥ) ")
           guardar(letra)
           print("══════════════════════════")
           print(lista_vacia)
           descontar_vida(letra)
      return lista_casa

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

while True:
      print("══════════════════════════")
      print("► Ingrese una letra: ")
      letra = validar_letra("")
      resultado = list(filter(adivinar, letra))
      print(lista_casa)

      if adivinar_casa == lista_casa:
          print("► (Lo hiciste!! \nAdivinaste la palabra!!)> (o´▽`o)♥")
          print("✿✿✿✿✿✿✿✿✿✿✿")
          break
      elif len(lista_vacia) == vida or vida == 0:
          print("► (Game Over)> (×_×)")
          print("✿✿✿✿✿✿✿✿✿✿✿")
          break