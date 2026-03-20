def gerar_trailer(sequencia):
    linha = (
        "9" +
        " " * 393 +
        str(sequencia).rjust(6, "0")
    )
    return linha
