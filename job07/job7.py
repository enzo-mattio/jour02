def type_code(langage):
  if langage == "javascript":
    return "Tu es un developpeur web"
  elif langage == "python":
    return "Tu es un developpeur IA"
  elif langage == "java":
    return "Tu es un developpeur logiciel"
  elif langage == "reactjs":
    return "Tu es un developpeur mobile"
  else:
    return "un jour, je serai le meilleur developpeur..."

print(type_code("javascript"))