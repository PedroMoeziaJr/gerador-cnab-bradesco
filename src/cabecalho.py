from datetime import datetime

def gerar_cabecalho():
    codigo_empresa = "0000000007867330"  # 20 posições (convênio alinhado à direita)
    nome_empresa = "PRIME PARK ESTACIONAMENTOS LTDA".ljust(30)
    data_hoje = datetime.now().strftime("%d%m%y")

    linha = (
        "0" +
        "1" +
        "REMESSA" +
        "01" +
        "COBRANCA".ljust(15) +
        codigo_empresa +
        nome_empresa +
        "237" +
        "BRADESCO".ljust(15) +
        data_hoje +
        " " * 8 +
        "MX" +
        "0000001" +
        " " * 277 +
        "000000"
    )

    return linha
