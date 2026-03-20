from datetime import datetime

def gerar_cabecalho():
    registro = "0"
    tipo_operacao = "1"
    espaco = " "
    literal_remessa = "REMESSA".ljust(7)
    codigo_servico = "01"
    literal_servico = "COBRANCA".ljust(15)

    agencia = "0606"
    conta = "1656414"
    conta_dv = "4"

    nome_empresa = "PRIME PARK ESTACIONAMENTOS LTDA".ljust(30)
    codigo_banco = "237"
    nome_banco = "BRADESCO".ljust(15)

    data_hoje = datetime.now().strftime("%d%m%y")

    uso_do_banco = " " * 8
    complemento = " " * 294
    numero_sequencial = "000001"

    linha = (
        registro +
        espaco +               # <<<<<<<<<< AQUI ESTAVA O ERRO
        tipo_operacao +
        literal_remessa +
        codigo_servico +
        literal_servico +
        agencia.rjust(4, "0") +
        conta.rjust(7, "0") +
        conta_dv +
        uso_do_banco +
        nome_empresa +
        codigo_banco +
        nome_banco +
        data_hoje +
        complemento +
        numero_sequencial
    )

    return linha[:400]