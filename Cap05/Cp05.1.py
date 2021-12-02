#Classes, Objetos, Atributos e Métodos
#Capítulo 5: Aulas 1, 2 e 3

class Livro():
  def __init__(self,):
    self.titulo = "O Monge e o Executivo"
    self.isbn = 9988888
    print("Construtor chamado para criar um objeto desta classe\n")

  def imprime(self):
    print("Foi criado o livro %s e ISBM %d" %(self.titulo, self.isbn))

Livro1 = Livro()
print(type(Livro1))
print(Livro1.titulo)
Livro1.imprime()


class Livro():
  def __init__(self, titulo, isbn):
    self.titulo = titulo
    self.isbn = isbn
    print("Construtor chamado para criar um objeto desta classe\n")

  def imprime(self):
    print("Foi criado o livro %s e ISBM %d \n" %(self.titulo, self.isbn))

Livro2 = Livro("A Menina que Roubava Livros", 77886611)
print(type(Livro2))
print(Livro2.titulo)
Livro2.imprime()


class Funcionarios:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def listFunc(self):
        print("O nome do funcionário é " + self.nome + " e o salário é R$" + str(self.salario))

Func1 = Funcionarios("Obama", 20000)
Func1.listFunc()
print(hasattr(Func1, "nome"))
print(hasattr(Func1, "salario"))
print(setattr(Func1, "salario", 4500))
print(hasattr(Func1, "salario"))
print(getattr(Func1, "salario"))
print(delattr(Func1, "salario"))
print(hasattr(Func1, "salario"), "\n")


class Circulo():
  pi = 3.14

  def __init__(self, raio = 5):
    self.raio = raio
  
  def area(self):
    return (self.raio * self.raio) * Circulo.pi
  
  def setRaio(self, novo_raio):
    self.raio = novo_raio
  
  def getRaio(self):
    return self.raio

circ = Circulo()
print(circ.getRaio())
circ1 = Circulo(7)
print(circ1.getRaio())

print ('O raio é: ', circ.getRaio())
print('Area igual a: ', circ.area())

circ.setRaio(3)

print ('Novo raio igual a: ', circ.getRaio())
print('A nova area igual a: ', circ.area())