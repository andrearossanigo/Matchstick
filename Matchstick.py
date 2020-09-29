from random import *

def aff(t):
  x = 1
  print("*"*len(t)*4)
  for i in range(len(t)):
    print("{0:2} {1:10} {2}".format("*",(len(t)-i)*" "+"|"*t[i],"*"))
    x=x+2
  print("*"*len(t)*4)

def plan1(nb_lignes):
  x = 1
  t = []
  for i in range(nb_lignes):
    t.append(x)
    x=x+2
  return t



def xor(t):
  xor = 0
  for i in range(len(t)):
    xor = xor ^ t[i]
  return xor

def IA(t, nb_lignes):
  n = randint(0,nb_lignes-1)
  if xor(t) == 0:
    while t[n] == 0: n = (n+1) % nb_lignes
    t[n] -= 1
    return [n + 1, 1]
  else:
    while xor(t) != 0:
      n = (n+1) % nb_lignes
      while t[n] == 0: n = (n+1) % nb_lignes
      v = t[n]
      while (xor(t) != 0 and t[n] > 0): t[n] -= 1
      if (xor(t) != 0): t[n] = v
    return [n + 1, v - t[n]]

def nim():
  print("But: tirer derniere allumette")
  nb_lignes = input("Le nombre de lignes ? ")
  nb_max = input("le nombre maximal d’allumettes ? ")
  #t = [randint(1,m) for i in range(int(nb_lignes))]
  t = plan1(int(nb_lignes))
  joueur = True
  while True:
    aff(t)
    if joueur:
      c = input("A toi (ex 1.4) : ").split(".")
      while (int(c[1])>int(nb_max) or int(c[1])<1 or int(c[0])<1 or int(c[0])>len(t)):
        c = input("svp choisir une bonne combinaison : ").split(".")
      [r, n] = [int(c[0]) - 1, int(c[1])]
      t[r] -= n
      joueur = False    
      if sum(t) == 0:
        print("Tu es trop fort !")
        return
    else:
      ordi = IA(t, int(nb_lignes))
      coup = str(ordi[0])+"."+str(ordi[1])
      print("Je joue " + coup)
      if sum(t) == 0:
        print("Tu as perdu !")
        return
      joueur = True
        
nim()
