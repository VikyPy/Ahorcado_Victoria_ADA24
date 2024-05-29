import random

print("✿✿✿✿✿✿✿✿✿✿✿")
print("► Bienvenido al juego del AHORCADO! :)")

palabra1 = "casa"
palabra2 = "cocodrilo"
palabra3 = "psicofarmacologia"

dicc_palabras = {"casa": 1, "cocodrilo": 2, "psicofarmacologia": 3}
palabra_random = random.randint(1,3)
if palabra_random == 1:
    print(f"La palabra contiene {len(palabra1)}: ----")
else:
    if palabra_random == 2:
        print(f"La palabra es {len(palabra2)}: ---------")
    else:
        print(f"La palabra es {len(palabra3)}: -----------------")

palabra = "casa"

adivinar_casa = ["c","a","s","a"]
lista_casa = ["-","-","-","-"]
#             0   1    2   3
lista_vacia = []

vida = 5

def adivinar(letra):
      if letra.lower() == "a": #minus = letra.lower()
         lista_casa[1] = "a"
         lista_casa[3] = "a"

      elif letra.lower() == "s":
         lista_casa[2] = "s"
      elif letra.lower() == "c":
           lista_casa[0] = "c"
      else:
           print("no se encontro letra")
           guardar(letra)
           print(lista_vacia)
      return lista_casa

def guardar(letra):
     letra_i = lista_vacia.append(letra) #letra_i = letras incorrectas
     return letra_i

while True:
      print("Escribe una letra: ")
      letra = input()
      resultado = list(filter(adivinar, letra))
      print(lista_casa)

      if adivinar_casa == lista_casa:
          print("Adivinaste!")
          break
      elif len(lista_vacia) == vida:
          print("game over")
          break