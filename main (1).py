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
