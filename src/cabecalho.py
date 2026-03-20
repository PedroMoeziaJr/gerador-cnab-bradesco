def gerar_cabecalho():
    registro = "0"
    tipo_operacao = "1"
    literal_remessa = "REMESSA".ljust(7)
    codigo_servico = "01"
    literal_servico = "COBRANCA".ljust(15)

    agencia = "0606"
    conta = "1656414"  # sem hífen
    conta_dv = "4"
    convenio = "7867330"

    nome_empresa = "Prime Park Estacionamentos".upper().ljust(30)
    codigo_banco = "237"
    nome_banco = "BRADESCO".ljust(15)

    from datetime import datetime
    data_hoje = datetime.now().strftime("%d%m%y")

    complemento = " " * 294
    numero_sequencial = "000001"

    linha = (
        registro +
        tipo_operacao +
        literal_remessa +
        codigo_servico +
        literal_servico +
        agencia.rjust(4, "0") +
        conta.rjust(8, "0") +
        conta_dv +
        nome_empresa +
        codigo_banco +
        nome_banco +
        data_hoje +
        complemento +
        numero_sequencial
    )

    return linha[:400]
