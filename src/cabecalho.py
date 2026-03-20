from datetime import datetime

def gerar_cabecalho():
    # Registro 0 – Cabeçalho
    registro = "0"
    tipo_operacao = "1"
    literal_remessa = "REMESSA".ljust(7)
    codigo_servico = "01"
    literal_servico = "COBRANCA".ljust(15)

    agencia = "0606"
    conta = "1656414"  # sem hífen
    conta_dv = "4"
    nome_empresa = "PRIME PARK ESTACIONAMENTOS LTDA".ljust(30)

    codigo_banco = "237"
    nome_banco = "BRADESCO".ljust(15)

    data_hoje = datetime.now().strftime("%d%m%y")

    complemento = " " * 294
    numero_sequencial = "000001"

    linha = (
        registro +                     # 1
        tipo_operacao +                # 2
        literal_remessa +              # 3–9
        codigo_servico +               # 10–11
        literal_servico +              # 12–26
        agencia.rjust(4, "0") +        # 27–30
        conta.rjust(7, "0") +          # 31–37
        conta_dv +                     # 38
        " " * 8 +                      # 39–46 (uso do banco)
        nome_empresa +                 # 47–76
        codigo_banco +                 # 77–79
        nome_banco +                   # 80–94
        data_hoje +                    # 95–100
        complemento +                  # 101–394
        numero_sequencial              # 395–400
    )

    return linha[:400]
