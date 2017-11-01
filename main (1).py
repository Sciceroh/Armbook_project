class Pessoa(object):
  def __init__(self, nome, email, idade, profissao):
    super(Pessoa, self).__init__()
    self._nome = nome
    self._email = email 
    self._idade = idade 
    self._profissao = profissao 
  
  def __str__(self):

class user(Pessoa):
  def __init__(self, nome, email, idade, profissao):
    super(user, self).__init__(nome, email, idade, profissao)
    self._user = user

  def getuser(self, i):
    return self._user

  def __str__(self):
    pass