def gerar_trailer(sequencia):
    registro = "9"
    brancos = " " * 393
    numero_sequencial = str(sequencia).rjust(6, "0")
    return (registro + brancos + numero_sequencial)[:400]
