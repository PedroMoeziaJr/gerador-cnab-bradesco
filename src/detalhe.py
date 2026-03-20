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
    bairro = boleto["bairro"].upper().ljust(15)
    cep = boleto["cep"].replace("-", "").rjust(8, "0")
    cidade = boleto["cidade"].upper().ljust(15)
    uf = boleto["uf"].upper().ljust(2)

    linha = (
        registro +                          # 1
        agencia.rjust(4, "0") +             # 2–5
        conta.rjust(7, "0") +               # 6–12
        conta_dv +                          # 13
        " " * 25 +                          # 14–38
        nosso_numero[:10] +                 # 38–47
        dv_nosso_numero +                   # 48
        " " * 60 +                          # 49–108
        carteira +                          # 109–111
        " " * 10 +                          # 112–121
        vencimento +                        # 122–127
        valor +                             # 128–140
        " " * 7 +                           # 141–147
        nome_sacado +                       # 148–187
        endereco +                          # 188–227
        bairro +                            # 228–242
        cep +                               # 243–250
        cidade +                            # 251–265
        uf +                                # 266–267
        " " * 127 +                         # 268–394
        str(sequencia).rjust(6, "0")        # 395–400
    )

    return linha[:400]
