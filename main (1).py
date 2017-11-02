class Armbook_user:

    def __init__(self):
        self.usuario = []
        self.logado = self.logon()
        self.tela()

    def cadastra_clientes(self):
        login = self.nome.get()
        senha = self.nome.get()
        nome = self.nome.get()
        email = self.email.get()
        idade = self.idade.get()
        profissao = self.profissao.get()

        usuario = Usuario(login, senha, nome, idade, email, profissao)
        self.usuario.append(usuario)
        return usuario

    def deleta_cliente(self):
        self.nome.remove()
        self.email.remove()
        self.idade.remove()
        self.profissao.remove()
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

    def senha(self):
        return self.senha

    def nome(self):
        return self.nome

    def idade(self):
        return self.idade

    def email(self):
        return self.email

    def profissao(self):
        return self.profissao




class user(User_Armbook):
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

    def __str__(self):
        pass

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
