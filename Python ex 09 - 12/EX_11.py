class Matematica:
    @staticmethod
    def eh_primo(numero):
        """
        Verifica se um número é primo.
        """
        if numero <= 1:
            return False  # <--- Esta linha deve estar identada corretamente
        
        for i in range(2, int(numero**0.5) + 1):
            if numero % i == 0:
                return False  # <--- Esta linha também
        
        return True  # <--- E esta aqui
    
# --- Teste da Classe ---

print(f"O número 7 é primo? {Matematica.eh_primo(7)}")
print(f"O número 10 é primo? {Matematica.eh_primo(10)}")
print(f"O número 2 é primo? {Matematica.eh_primo(2)}")
print(f"O número 1 é primo? {Matematica.eh_primo(1)}")
print(f"O número 23 é primo? {Matematica.eh_primo(23)}")