class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas

    def calcular_media(self):
        """
        Calcula a média das notas do aluno.
        """
        if not self.notas:
            return 0  # Retorna 0 se a lista de notas estiver vazia
        return sum(self.notas) / len(self.notas)

    def verificar_aprovacao(self):
        """
        Verifica se o aluno foi aprovado (média >= 7).
        """
        media = self.calcular_media()
        if media >= 7:
            return True
        else:
            return False

# Criando dois objetos Aluno
aluno1 = Aluno("Jonas", [8.0, 7.3, 9.6])
aluno2 = Aluno("Maria", [6.0, 5.5, 7.0])

print(f"A média de {aluno1.nome} é {aluno1.calcular_media():.2f}.")
if aluno1.verificar_aprovacao():
    print(f"{aluno1.nome} foi aprovado(a)!")
else:
    print(f"{aluno1.nome} foi reprovado(a).")

print("\n" + "="*30 + "\n")

print(f"A média de {aluno2.nome} é {aluno2.calcular_media():.2f}.")
if aluno2.verificar_aprovacao():
    print(f"{aluno2.nome} foi aprovado(a)!")
else:
    print(f"{aluno2.nome} foi reprovado(a).")