def gerar_detalhe(boleto, sequencia):
    registro = "1"

    agencia = "0606"
    conta = "1656414"
    conta_dv = "4"
    carteira = "09"
    convenio = "7867330"

    nosso_numero = str(boleto["nosso_numero"]).rjust(11, "0")

    nome_sacado = boleto["nome"].upper().ljust(40)
    vencimento = boleto["vencimento"].strftime("%d%m%y")
    valor = f"{int(boleto['valor']*100):013d}"

    codigo_banco = "237"
    especie = "01"
    aceite = "N"

    from datetime import datetime
    data_emissao = datetime.now().strftime("%d%m%y")

    brancos = " " * 200
    numero_sequencial = str(sequencia).rjust(6, "0")

    linha = (
        registro +
        agencia.rjust(4, "0") +
        conta.rjust(8, "0") +
        conta_dv +
        nosso_numero +
        carteira +
        convenio.rjust(7, "0") +
        nome_sacado +
        vencimento +
        valor +
        codigo_banco +
        especie +
        aceite +
        data_emissao +
        brancos +
        numero_sequencial
    )

    return linha[:400]
