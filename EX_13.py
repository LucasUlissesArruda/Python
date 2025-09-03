class Seguranca:
    def __init__(self):
        pass
    def _criptografar_msg(self, mensagem):
        return "Protegida"
    def exibir_msg_crip(self, mensagem):
        msg_crip = self._criptografar_msg(mensagem)
        print(f"Mensagem criptografada: {msg_crip}")
seg = Seguranca()
seg.exibir_msg_crip("nao entendia ")