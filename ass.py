'''(Desafio) Utilizando listas, faça um programa que faça 5 perguntas para uma pessoa (ou várias pessoas) sobre um crime.
#As perguntas são:
#1.Telefonou para a vítima no dia do crime?
#2: Esteve no local do crime?
#3: Mora perto da vítima?
#4: Devia dinheiro para a vítima?
#5: Já trabalhou com a vítima?
#O programa deve no final emitir uma classificação sobre a participação da(s) pessoa(s) no crime.
#• Suspeita: 2 questões positivas (sim)
#• Cúmplice: entre 3 e 4 questões positivas
#• Assassino: 5 questões positivas
#• Inocente: menos de 2 questões positivas

print("Olá serão feitas algumas perguntas sobre o caso e gostaria que você respondesse com sinceridade!\n")
print("Responda somente:\n S - sim | N - não\n")
resA = str(input("1° - Telefonou para a Vítima no dia do crime?\n>"))
resA = resA.upper()

resB = str(input("2° - Esteve no local do crime?\n>"))
resB = resB.upper()

resC = str(input("3° - Mora perto da vítima?\n>"))
resC = resC.upper()

resD = str(input("4° - Devia dinheiro para a vítima?\n>"))
resD = resD.upper()

resE = str(input("5° - 5: Já trabalhou com a vítima?\n>"))
resE = resE.upper()

if resA == "S":
  if resB == "S":
    if resC == "S":
      if resD == "S":
        if resE == "S":                                    #-------[S=5|N=0]
          print("O(a) interrogato(a) é o Assassino!!!")
        elif resE == "N":                                  #-------[S=4|N=1]
          print("O(a) interrogado(a) é um(a) Cúmplice!")
      
      elif resD == "N":  #--D -> nao
        if resE == "S":                                    #-------[S=4|N=1]
          print("O(a) interrogado(a) é um(a) Cúmplice!")
        elif resE == "N":                                  #-------[S=3|N=2]
          print("O(a) interrogado(a) é um(a) Cúmplice!")
          
    elif resC == "N":  #--C -> nao
      if resD == "S":
        if resE == "S":                                    #-------[S=4|N=1]
          print("O(a) interrogado(a) é um(a) Cúmplice!")
        elif resE == "N":                                  #-------[S=3|N=2]
          print("O(a) interrogado(a) é um(a) Cúmplice!")
      
      elif resD == "N":
        if resE == "S":                                    #-------[S=3|N=2]
          print("O(a) interrogado(a) é um(a) Cúmplice!")
        elif resE == "N":                                  #-------[S=2|N=3]
          print("O(a) interrogado(a) é Suspeito(a).")

  elif resB == "N":  #--B -> nao
    if resC == "S":
      if resD == "S":
        if resE == "S":                                    #-------[S=4|N=1]
          print("O(a) interrogado(a) é um(a) Cúmplice!")
        elif resE == "N":                                  #-------[S=3|N=2]
          print("O(a) interrogado(a) é um(a) Cúmplice!")
      
      elif resD == "N":  #--D -> nao
        if resE == "S":                                    #-------[S=3|N=2]
          print("O(a) interrogado(a) é um(a) Cúmplice!")
        elif resE == "N":                                  #-------[S=2|N=3]
          print("O(a) interrogado(a) é Suspeito(a).")
          
    elif resC == "N":  #--C -> nao
      if resD == "S":
        if resE == "S":                                    #-------[S=3|N=2]
          print("O(a) interrogado(a) é um(a) Cúmplice!")
        elif resE == "N":                                  #-------[S=2|N=3]
          print("O(a) interrogado(a) é Suspeito(a).")
      
      elif resD == "N":
        if resE == "S":                                    #-------[S=2|N=3]
          print("O(a) interrogado(a) é Suspeito(a).")
        elif resE == "N":                                  #-------[S=1|N=4]
          print("O(a) interrogado(a) é Inocente")

  
elif resA == "N":  #--A -> nao
  if resB == "S":
    if resC == "S":
      if resD == "S":
        if resE == "S":                                    #-------[S=4|N=1]
          print("O(a) interrogado(a) é um(a) Cúmplice!")
        elif resE == "N":                                  #-------[S=3|N=2]
          print("O(a) interrogado(a) é um(a) Cúmplice!")
      
      elif resD == "N":  #--D -> nao
        if resE == "S":                                    #-------[S=3|N=2]
          print("O(a) interrogado(a) é um(a) Cúmplice!")
        elif resE == "N":                                  #-------[S=2|N=3]
          print("O(a) interrogado(a) é Suspeito(a).")
          
    elif resC == "N":  #--C -> nao
      if resD == "S":
        if resE == "S":                                    #-------[S=3|N=2]
          print("O(a) interrogado(a) é um(a) Cúmplice!")
        elif resE == "N":                                  #-------[S=2|N=3]
          print("O(a) interrogado(a) é Suspeito(a).")
      
      elif resD == "N":
        if resE == "S":                                    #-------[S=2|N=3]
          print("O(a) interrogado(a) é Suspeito(a).")
        elif resE == "N":                                  #-------[S=1|N=4]
          print("O(a) interrogado(a) é Inocente")

  elif resB == "N":  #--B -> nao
    if resC == "S":
      if resD == "S":
        if resE == "S":                                    #-------[S=3|N=2]
          print("O(a) interrogado(a) é um(a) Cúmplice!")
        elif resE == "N":                                  #-------[S=2|N=3]
          print("O(a) interrogado(a) é Suspeito(a).")
      
      elif resD == "N":  #--D -> nao
        if resE == "S":                                    #-------[S=2|N=3]
          print("O(a) interrogado(a) é Suspeito(a).")
        elif resE == "N":                                  #-------[S=1|N=4]
          print("O(a) interrogado(a) é Inocente")
          
    elif resC == "N":  #--C -> nao
      if resD == "S":
        if resE == "S":                                    #-------[S=2|N=3]
          print("O(a) interrogado(a) é Suspeito(a).")
        elif resE == "N":                                  #-------[S=1|N=4]
          print("O(a) interrogado(a) é Inocente")
      
      elif resD == "N":
        if resE == "S":                                    #-------[S=1|N=4]
          print("O(a) interrogado(a) é Inocente")
        elif resE == "N":                                  #-------[S=0|N=5]
          print("O(a) interrogado(a) é Inocente")
'''


#'''Segunda Parte

res = ['a' , 'b' , 'c' , 'd' , 'e']

res[0] = str(input("1° - Telefonou para a Vítima no dia do crime?\n>"))
res[0] = res[0].upper()

res[1] = str(input("2° - Esteve no local do crime?\n>"))
res[1] = res[1].upper()

res[2] = str(input("3° - Mora perto da vítima?\n>"))
res[2] = res[2].upper()

res[3] = str(input("4° - Devia dinheiro para a vítima?\n>"))
res[3] = res[3].upper()

res[4] = str(input("5° - 5: Já trabalhou com a vítima?\n>"))
res[4] = res[4].upper()

#-----

if res[0] == "S":
  if res[1] == "S":
    if res[2] == "S":
      if res[3] == "S":
        if res[4] == "S":                                    #-------[S=5|N=0]
          print("O(a) interrogato(a) é o Assassino!!!")
        elif res[4] == "N":                                  #-------[S=4|N=1]
          print("O(a) interrogado(a) é um(a) Cúmplice!")
      
      elif res[3] == "N":  #--D -> nao
        if res[4] == "S":                                    #-------[S=4|N=1]
          print("O(a) interrogado(a) é um(a) Cúmplice!")
        elif res[4] == "N":                                  #-------[S=3|N=2]
          print("O(a) interrogado(a) é um(a) Cúmplice!")
          
    elif res[2] == "N":  #--C -> nao
      if res[3] == "S":
        if res[4] == "S":                                    #-------[S=4|N=1]
          print("O(a) interrogado(a) é um(a) Cúmplice!")
        elif res[4] == "N":                                  #-------[S=3|N=2]
          print("O(a) interrogado(a) é um(a) Cúmplice!")
      
      elif res[3] == "N":
        if res[4] == "S":                                    #-------[S=3|N=2]
          print("O(a) interrogado(a) é um(a) Cúmplice!")
        elif res[4] == "N":                                  #-------[S=2|N=3]
          print("O(a) interrogado(a) é Suspeito(a).")

  elif res[1] == "N":  #--B -> nao
    if res[2] == "S":
      if res[3] == "S":
        if res[4] == "S":                                    #-------[S=4|N=1]
          print("O(a) interrogado(a) é um(a) Cúmplice!")
        elif res[4] == "N":                                  #-------[S=3|N=2]
          print("O(a) interrogado(a) é um(a) Cúmplice!")
      
      elif res[3] == "N":  #--D -> nao
        if res[4] == "S":                                    #-------[S=3|N=2]
          print("O(a) interrogado(a) é um(a) Cúmplice!")
        elif res[4] == "N":                                  #-------[S=2|N=3]
          print("O(a) interrogado(a) é Suspeito(a).")
          
    elif res[2] == "N":  #--C -> nao
      if res[3] == "S":
        if res[4] == "S":                                    #-------[S=3|N=2]
          print("O(a) interrogado(a) é um(a) Cúmplice!")
        elif res[4] == "N":                                  #-------[S=2|N=3]
          print("O(a) interrogado(a) é Suspeito(a).")
      
      elif res[3] == "N":
        if res[4] == "S":                                    #-------[S=2|N=3]
          print("O(a) interrogado(a) é Suspeito(a).")
        elif res[4] == "N":                                  #-------[S=1|N=4]
          print("O(a) interrogado(a) é Inocente")

elif res[0] == "N":  #--A -> nao
  if res[1] == "S":
    if res[2] == "S":
      if res[3] == "S":
        if res[4] == "S":                                   #-------[S=4|N=1]
          print("O(a) interrogado(a) é um(a) Cúmplice!")
        elif res[4] == "N":                                  #-------[S=3|N=2]
          print("O(a) interrogado(a) é um(a) Cúmplice!")
      
      elif res[3] == "N":  #--D -> nao
        if res[4] == "S":                                    #-------[S=3|N=2]
          print("O(a) interrogado(a) é um(a) Cúmplice!")
        elif res[4] == "N":                                  #-------[S=2|N=3]
          print("O(a) interrogado(a) é Suspeito(a).")
          
    elif res[2] == "N":  #--C -> nao
      if res[3] == "S":
        if res[4] == "S":                                    #-------[S=3|N=2]
          print("O(a) interrogado(a) é um(a) Cúmplice!")
        elif res[4] == "N":                                  #-------[S=2|N=3]
          print("O(a) interrogado(a) é Suspeito(a).")
      
      elif res[3] == "N":
        if res[4] == "S":                                    #-------[S=2|N=3]
          print("O(a) interrogado(a) é Suspeito(a).")
        elif res[4] == "N":                                  #-------[S=1|N=4]
          print("O(a) interrogado(a) é Inocente")

  elif res[1] == "N":  #--B -> nao
    if res[2] == "S":
      if res[3] == "S":
        if res[4] == "S":                                    #-------[S=3|N=2]
          print("O(a) interrogado(a) é um(a) Cúmplice!")
        elif res[4] == "N":                                  #-------[S=2|N=3]
          print("O(a) interrogado(a) é Suspeito(a).")
      
      elif res[3] == "N":  #--D -> nao
        if res[4] == "S":                                    #-------[S=2|N=3]
          print("O(a) interrogado(a) é Suspeito(a).")
        elif res[4] == "N":                                  #-------[S=1|N=4]
          print("O(a) interrogado(a) é Inocente")
          
    elif res[2] == "N":  #--C -> nao
      if res[3] == "S":
        if res[4] == "S":                                    #-------[S=2|N=3]
          print("O(a) interrogado(a) é Suspeito(a).")
        elif res[4] == "N":                                  #-------[S=1|N=4]
          print("O(a) interrogado(a) é Inocente")
      
      elif res[3] == "N":
        if res[4] == "S":                                    #-------[S=1|N=4]
          print("O(a) interrogado(a) é Inocente")
        elif res[4] == "N":                                  #-------[S=0|N=5]
          print("O(a) interrogado(a) é Inocente")
