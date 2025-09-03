class Funcionario:
    # Atributo de classe: pertence à classe
    empresa = "TechCorp"

    def __init__(self, nome):
        self.nome = nome

    @classmethod
    def mudar_empresa(cls, novo_nome_empresa):
        """Método de classe para alterar o nome da empresa os funcionários."""
        print(f"Alterando nome da empresa de '{cls.empresa}' para '{novo_nome_empresa}'.")
        cls.empresa = novo_nome_empresa

    def mostrar_dados(self):
        """Método de instância para mostrar os dados do funcionário."""
        print(f"Nome: {self.nome}, Empresa: {self.empresa}")

# Sugestão de Teste - deve ficar fora da classe.

# Criando dois funcionários
print("--- Funcionários antes da mudança ---")
funcionario1 = Funcionario("João")
funcionario2 = Funcionario("Maria")

funcionario1.mostrar_dados()
funcionario2.mostrar_dados()

print("\n" + "="*40 + "\n")

# Alterando o nome da empresa usando o método de classe
Funcionario.mudar_empresa("Global Solutions")

print("\n" + "="*40 + "\n")

# Verificando dados dos funcionários pós a mudança
print("--- Funcionários após a mudança ---")
funcionario1.mostrar_dados()
funcionario2.mostrar_dados()