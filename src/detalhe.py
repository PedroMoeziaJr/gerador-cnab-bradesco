def gerar_detalhe(boleto, sequencia):
    registro = "1"

    agencia = "0606"
    conta = "1656414"
    conta_dv = "4"
    carteira = "009"  # sempre 3 dígitos
    convenio = "7867330"

    nosso_numero = str(boleto["nosso_numero"]).rjust(11, "0")
    dv_nosso_numero = "0"  # você pode informar depois se quiser

    valor = f"{int(boleto['valor'] * 100):013d}"
    vencimento = boleto["vencimento"].strftime("%d%m%y")

    nome_sacado = boleto["nome"].upper().ljust(40)
    endereco = boleto["endereco"].upper().ljust(40)
    bairro = boleto["bairro"].upper().ljust(15)
    cep = boleto["cep"].replace("-", "").rjust(8, "0")
    cidade = boleto["cidade"].upper().ljust(15)
    uf = boleto["uf"].upper().ljust(2)

    brancos_1 = " " * 25
    brancos_2 = " " * 6
    brancos_3 = " " * 60
    brancos_4 = " " * 8
    brancos_5 = " " * 40

    numero_sequencial = str(sequencia).rjust(6, "0")

    linha = (
        registro +                          # 1
        agencia.rjust(4, "0") +             # 2–5
        conta.rjust(7, "0") +               # 6–12
        conta_dv +                          # 13
        brancos_1 +                         # 14–38
        nosso_numero[:10] +                 # 38–47
        dv_nosso_numero +                   # 48
        brancos_2 +                         # 49–54
        carteira +                          # 108–110
        brancos_3 +                         # 111–170
        vencimento +                        # 121–126
        valor +                             # 127–139
        brancos_4 +                         # 140–147
        nome_sacado +                       # 148–187
        endereco +                          # 188–227
        bairro +                            # 228–242
        cep +                               # 243–250
        cidade +                            # 251–265
        uf +                                # 266–267
        brancos_5 +                         # 268–307
        numero_sequencial                   # 395–400
    )

    return linha[:400]
