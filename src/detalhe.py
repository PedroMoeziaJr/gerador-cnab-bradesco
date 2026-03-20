from datetime import datetime

def gerar_detalhe(boleto, sequencia):
    registro = "1"

    agencia = "0606"
    conta = "1656414"
    conta_dv = "4"
    carteira = "009"

    nosso_numero = str(boleto["nosso_numero"]).rjust(11, "0")
    dv_nosso_numero = "0"

    valor = f"{int(boleto['valor'] * 100):013d}"
    vencimento = boleto["vencimento"].strftime("%d%m%y")

    nome_sacado = boleto["nome"].upper().ljust(40)
    endereco = boleto["endereco"].upper().ljust(40)
    bairro = boleto["bairro"].upper().ljust(12)
    cep = boleto["cep"].replace("-", "").rjust(8, "0")
    cidade = boleto["cidade"].upper().ljust(15)
    uf = boleto["uf"].upper().ljust(2)

    linha = (
        registro +                          # 1
        agencia.rjust(4, "0") +             # 2–5
        conta.rjust(7, "0") +               # 6–12
        conta_dv +                          # 13
        carteira +                          # 14–16
        nosso_numero +                      # 17–27
        dv_nosso_numero +                   # 28
        " " * 6 +                           # 29–34
        "0" * 13 +                          # 35–47 (uso do banco)
        " " * 4 +                           # 48–51
        vencimento +                        # 52–57
        valor +                             # 58–70
        "0" * 3 +                           # 71–73
        " " * 25 +                          # 74–98
        nome_sacado +                       # 99–138
        endereco +                          # 139–178
        bairro +                            # 179–190
        cep +                               # 191–198
        cidade +                            # 199–213
        uf +                                # 214–215
        " " * 178 +                         # 216–393
        str(sequencia).rjust(6, "0")        # 394–399
    )

    return linha[:400]
