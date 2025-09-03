class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    def __str__(self):
        """Método mágico para representação em string"""
        return f"Produto: {self.nome}, Preço: R${self.preco:.2f}"
    def __eq__(self, outro_produto):
        """Método mágico para comparação de igualdade deve ser identado"""
        if isinstance(outro_produto, Produto):
            return self.preco == outro_produto.preco
        return False

# Sugestão de Teste
# Criando objetos Produto
livro = Produto("Livro 'Python Básico'", 45.50)
lapis = Produto("Lápis HB", 2.50)
outro_lapis = Produto("Lápis de Cor", 2.50)

print("--- Teste do Método __str__ ---")
print(livro)
print(lapis)

print("\n" + "="*30 + "\n")

print("--- Teste do Método __eq__ ---")
# Comparando produtos com preços iguais
print(f"Os preços são iguais? {lapis == outro_lapis}")

# Comparando produtos com preços diferentes
print(f"Os preços são iguais? {livro == lapis}")