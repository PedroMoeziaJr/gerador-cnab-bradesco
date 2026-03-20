from cabecalho import gerar_cabecalho
from detalhe import gerar_detalhe
from trailer import gerar_trailer
from datetime import date

def gerar_arquivo_rem():
    linhas = []
    linhas.append(gerar_cabecalho())

    boleto = {
        "nosso_numero": 44,
        "nome": "Renata Nepomuceno",
        "valor": 400.00,
        "vencimento": date(2026, 4, 5),
        "endereco": "SCS QD 2 ED BRADESCO 1 SS BRASILIA DF",
        "bairro": "ASA SUL",
        "cep": "70070120",
        "cidade": "BRASILIA",
        "uf": "DF",
        "cnpj": "08505544000117"
    }

    linhas.append(gerar_detalhe(boleto, 2))
    linhas.append(gerar_trailer(3))

    with open("REMESSA_TESTE.REM", "w", encoding="latin-1") as f:
        for linha in linhas:
            f.write(linha + "\r\n")

if __name__ == "__main__":
    gerar_arquivo_rem()
    print("Arquivo REMESSA_TESTE.REM gerado com sucesso.")
