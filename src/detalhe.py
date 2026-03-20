from datetime import datetime

def gerar_detalhe(boleto, sequencia):
    carteira = "09"
    agencia = "0606"
    conta = "1656414"
    conta_dv = "4"
    convenio = "7867330"

    identificacao_empresa = convenio.rjust(17, "0")

    nosso_numero = str(boleto["nosso_numero"]).rjust(11, "0")
    dv_nosso_numero = "0"

    numero_documento = nosso_numero[-10:].rjust(10, "0")
    vencimento = boleto["vencimento"].strftime("%d%m%y")
    valor = f"{int(boleto['valor'] * 100):013d}"

    data_emissao = datetime.now().strftime("%d%m%y")

    nome = boleto["nome"].upper().ljust(40)
    endereco = boleto["endereco"].upper().ljust(40)

    cnpj = boleto["cnpj"].rjust(14, "0")
    tipo_inscricao = "02"

    cep = boleto["cep"].replace("-", "")
    cep5 = cep[:5]
    cep3 = cep[5:]

    linha = (
        "1" +
        "0" * 5 +
        "0" +
        "0" * 5 +
        "0" * 7 +
        "0" +
        identificacao_empresa +
        " " * 25 +
        "237" +
        "0" +
        "0000" +
        nosso_numero +
        dv_nosso_numero +
        "0" * 10 +
        "2" +
        "N" +
        " " * 10 +
        " " +
        " " +
        "00" +
        "01" +
        numero_documento +
        vencimento +
        valor +
        "000" +
        "00000" +
        "01" +
        "N" +
        data_emissao +
        "00" +
        "00" +
        "0" * 13 +
        "000000" +
        "0" * 13 +
        "0" * 13 +
        "0" * 13 +
        tipo_inscricao +
        cnpj +
        nome +
        endereco +
        " " * 12 +
        cep5 +
        cep3 +
        " " * 60 +
        str(sequencia).rjust(6, "0")
    )

    return linha
