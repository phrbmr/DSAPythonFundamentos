#Herança e Métodos Especiais
#Capítulo 5: Aulas 4 e 5

##Super-classe ou Classe Mãe
class Animal():
  def __init__(self):
    print("Animal criado")

  def Identif(self):
    print("Anumal")

  def comer(self):
    print("Comendo")

##Sub-classe
class Cachorro(Animal):
  def __init__(self):
    Animal.__init__(self)
    print("Objeto Cachorro criado")

  def Identif(self):
    print("Cachorro")
  
  def latir(self):
    print("Au Au")
  
rex = Cachorro()
rex.Identif()
rex.comer()
rex.latir()

# Métodos especiais
class Livro():
  def __init__(self, titulo, autor, paginas):
    print("Livro criado")
    self.titulo = titulo
    self.autor = autor
    self.paginas = paginas

  def __str__(self):
    return "Título: %s , autor: %s, páginas: %s " \
    %(self.titulo, self.autor, self.paginas)

  def __len__(self):
    return self.paginas

  def len(self):
    return print("Páginas do livro com método comum: ", self.paginas)

livro1 = Livro("Os Lusíadas", "Luis de Camões", 8816)
print(livro1)
print(len(livro1))
livro1.len()
del livro1.paginas
print(hasattr(livro1, "paginas"))