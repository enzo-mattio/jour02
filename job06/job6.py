def pos_or_neg(nombre):
  if nombre > 0:
    return "Le nombre est positif"
  elif nombre < 0:
    return "Le nombre est négatif"
  else:
    return "Le nombre est 0"


print(pos_or_neg(0))