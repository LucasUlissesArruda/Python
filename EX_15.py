class Mensagem:
    def enviar(self, conteudo, destinatario=None):
        if not isinstance(conteudo, (str, int)):
            print("Erro: o conteúdo deve ser texto (str) ou número inteiro (int).")
            return

        if destinatario:
            print(f"Enviando para {destinatario}: {conteudo}")
        else:
            print(f"Enviando mensagem: {conteudo}")

msg = Mensagem()

msg.enviar("Olá, tudo bem?")

msg.enviar(12345)

msg.enviar("Olá, João!", destinatario="João")

msg.enviar(67890, destinatario="Maria")