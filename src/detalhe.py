from datetime import datetime

def gerar_detalhe(boleto, sequencia):
    # Dados fixos / da empresa
    carteira = "09"
    agencia = "0606"
    conta = "1656414"
    conta_dv = "4"
    convenio = "7867330"  # 7 dígitos
    identificacao_empresa = convenio.rjust(17, "0")  # posições 021–037

    # Dados do boleto
    nosso_numero = str(boleto["nosso_numero"]).rjust(11, "0")
    dv_nosso_numero = "0"

    numero_documento = nosso_numero[-10:].rjust(10, "0")
    vencimento = boleto["vencimento"].strftime("%d%m%y")
    valor = f"{int(boleto['valor'] * 100):013d}"

    data_emissao = datetime.now().strftime("%d%m%y")

    nome = boleto["nome"].upper().ljust(40)
    endereco = boleto["endereco"].upper().ljust(40)

    cnpj = boleto["cnpj"].rjust(14, "0")
    tipo_inscricao = "02"  # CNPJ

    cep = boleto["cep"].replace("-", "")
    cep5 = cep[:5]
    cep3 = cep[5:]

    linha = (
        "1" +                                # 001
        "0" * 5 +                             # 002–006 Agência débito
        "0" +                                 # 007 DV agência débito
        "0" * 5 +                             # 008–012 Razão conta débito
        "0" * 7 +                             # 013–019 Conta débito
        "0" +                                 # 020 DV conta débito
        identificacao_empresa +               # 021–037 Identificação empresa
        " " * 25 +                            # 038–062 Controle do participante
        "237" +                               # 063–065 Código banco
        "0" +                                 # 066 Multa
        "0000" +                              # 067–070 Percentual multa
        nosso_numero +                        # 071–081 Nosso número
        dv_nosso_numero +                     # 082 DV
        "0" * 10 +                            # 083–092 Desconto por dia
        "2" +                                 # 093 Emissão do boleto (2 = cliente)
        "N" +                                 # 094 Débito automático
        " " * 10 +                            # 095–104 Identificação operação
        " " +                                 # 105 Rateio
        " " +                                 # 106 Aviso débito automático
        "00" +                                # 107–108 Quantidade pagamentos
        "01" +                                # 109–110 Ocorrência (01 = registrar)
        numero_documento +                    # 111–120 Número documento
        vencimento +                          # 121–126 Vencimento
        valor +                               # 127–139 Valor
        "000" +                               # 140–142 Banco cobrança
        "00000" +                             # 143–147 Agência depositária
        "01" +                                # 148–149 Espécie
        "N" +                                 # 150 Identificação
        data_emissao +                        # 151–156 Data emissão
        "00" +                                # 157–158 1ª instrução
        "00" +                                # 159–160 2ª instrução
        "0" * 13 +                            # 161–173 Mora
        "000000" +                            # 174–179 Data desconto
        "0" * 13 +                            # 180–192 Valor desconto
        "0" * 13 +                            # 193–205 IOF
        "0" * 13 +                            # 206–218 Abatimento
        tipo_inscricao +                      # 219–220 Tipo inscrição
        cnpj +                                # 221–234 CNPJ
        nome +                                # 235–274 Nome pagador
        endereco +                            # 275–314 Endereço
        " " * 12 +                            # 315–326 Mensagem 1
        cep5 +                                # 327–331 CEP
        cep3 +                                # 332–334 Sufixo CEP
        " " * 60 +                            # 335–394 Beneficiário final
        str(sequencia).rjust(6, "0")          # 395–400 Sequencial
    )

    return linha
