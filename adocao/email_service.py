from django.core.mail import send_mail


def enviar_email_confirmacao(adocao):
    assunto = "Adoçao realizada com sucesso!"
    conteudo = f"Parabéns por realizar a adoção do pet {adocao.pet.nome} com o valor mensal de R${adocao.valor:.2f}."
    remetente = "raphaelaraujotoc@gmail.com"  # apenas para testes.
    destinatario = [adocao.email]

    send_mail(assunto, conteudo, remetente, destinatario)
