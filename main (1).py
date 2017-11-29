class Armbook:

  def __init__(self):
    self.usuarios = []
    self.logado = self.logon()
    self.tela()

  def cadastra_usuario(self):
    #login = self.nome.get()
    login = input("Login: ")
    senha = input("Senha: ")
    nome = input("Nome: ")
    email = input("Email: ")
    idade = input("Idade: ")
    profissao = input("Profissão: ")

    usuario = Usuario(login, senha, nome, idade, email, profissao)
    self.usuarios.append(usuario)
    return usuario

  def deleta_usuario(self):
    #self.nome.remove()
    #self.email.remove()
    #self.idade.remove()
    #self.profissao.remove()
    self.usuario.remove(self.logado)

  def listar_usuario(self):
    print(usuario)

  def login(self):
    conta = int(input("Deseja Fazer login na sua conta? | 1 para Sim, 2 para Não, e 3 para não tenho:"))
    if conta == 1:
      email = input("Digite aqui seu Email:")
      senha = input("Digite aqui sua conta:")

    elif conta == 2:
      print ("Fechar")
    else:
      return self.cadastra_usuario()

    return self.login

  def Meny(self):
    Menu = input("Escolha uma opção: 1 Para Atualizar Usuário | 2 Para Listar Usuário | 3 Para Deletar Usuário | 4 Não fazer nada")
    if menu == 1:
      Novo_Login = input("Digite novo login")
      Nova_senha = input("Digite nova senha")
      Novo_nome = input("Digite novo nome")
      Novo_Email = input("Digte novo email")
      Novo_Idade = input("Digite nova idade")
      Novo_profissao = input("Digite nova profissão")
      return self.cadastra_usuario()
    elif menu == 2:
      return self.listar_usuario()
    elif menu == 3:
      return self.deleta_usuario()
    else:
      print ("Você não fez nada")

  def get_senha(self):
    return self.senha

  def get_nome(self):
    return self.nome

  def get_idade(self):
    return self.idade

  def get_email(self):
    return self.email

  def get_profissao(self):
    return self.profissao
