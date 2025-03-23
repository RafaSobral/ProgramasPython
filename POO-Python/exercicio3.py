class Cliente:
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        self.lista_planos = ["Basic", "Premium"]
        if plano in self.lista_planos:
            self.plano = plano
        else:
            raise Exception("Esse plano nao esta na lista")
        
    def mudar_plano(self, novo_plano):
        if novo_plano in self.lista_planos:
            self.plano = novo_plano
            print("Plano alterado com sucesso")
        else:
            raise Exception("Esse plano nao esta na lista")
        
    def ver_filme(self, filme, plano_filme):
        if self.plano == plano_filme:
            print(f"Ver filme {filme}")
        elif self.plano == "Premium":
            print(f"Ver filme {filme}")
        elif self.plano == "Basic" and plano_filme == "Premium":
            print("faça upgrade para premium para poder ver o esse filme")
        else:
            raise Exception("Esse plano nao esta na lista")



cliente = Cliente("Rafael", "Rafael@gmail.com", "Basic")
print(cliente.plano)
cliente.mudar_plano("Premium")
print(cliente.plano)
cliente.mudar_plano("Basic")
cliente.ver_filme("O Galinho Chiken Little", "Premium")