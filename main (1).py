class Armbook:

    def __init__(self):
        #self.usuarios = []
        #self.logado = self.logon()
        #self.tela()

    def cadastra_clientes(self):
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

    def deleta_cliente(self):
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
            return self.cadastra_clientes()
       
        return self.login

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




class user(Armbook):
    def __init__(self, login, senha nome, email, idade, profissao):
        self.login = login
        self.senha = senha
        self.nome = nome
        self.email = email
        self.idade = idade
        self._profissao = profissao

    def __init__(self, nome, email, idade, profissao):
        super(user, self).__init__(nome, email, idade, profissao)
        self._user = user

    def getuser(self, i):
        return self._user

   

    def set_nome(self, nome):
        if len(nome) > 0:
            self.nome = nome

    def set_idade(self, idade):
        if idade > 0:
            self.idade = idade

    def set_email(self,email):
        if len(nome) > 0:
            self.email = email

    def set_profissao(self, profissao):
        if len(nome) > 0:
            self.profissao = profissao
