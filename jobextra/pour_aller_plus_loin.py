import math

def type_triangle(a, b, c):
  # Vérifie s'il est possible de construire un triangle avec les longueurs données
  if a + b > c and a + c > b and b + c > a:
    
    # Triangle rectangle
    
    if a**2 + b**2 == int(c**2) or a**2 + int(c**2) == b**2 or b**2 + int(c**2) == a**2:
      if a == b or a == c or b == c:
        print("Triangle rectangle isocèle")
      else:
        print("Triangle rectangle")
       
    # Triangle équilatéral
    
    elif a == b and b == c:
      print("Triangle équilatéral")
    
    # Triangle isocèle
    
    elif a == b or a == c or b == c:
      print("Triangle isocèle")
    

    # Triangle quelconque
    
    else:
      print("Triangle quelconque")
  else:
    print("Il n'est pas possible de construire un triangle avec ces longueurs")


type_triangle(1,1,math.sqrt(2)) # Affiche "Triangle rectangle Isocèle"
type_triangle(3,4,5) # Affiche "Triangle rectangle"
type_triangle(3,3,3) # Affiche "Triangle équilatéral"
type_triangle(6,6,9) # Affiche "Triangle Isocèle"
type_triangle(4,8,6) # Affiche "Triangle quelconque"
type_triangle(9,15,25) # Affiche "Il n'est pas possible de construire un triangle avec ces longueurs"