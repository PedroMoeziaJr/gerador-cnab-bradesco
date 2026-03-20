from cabecalho import gerar_cabecalho
from detalhe import gerar_detalhe
from trailer import gerar_trailer

def gerar_arquivo_rem():
    linhas = []
    linhas.append(gerar_cabecalho())

    # Exemplo de boleto fixo (vamos ler do Excel depois)
    boleto = {
        "nosso_numero": 1,
        "nome": "Cliente Teste",
        "valor": 10.00,
        "vencimento": __import__("datetime").date(2026, 4, 5)
    }

    linhas.append(gerar_detalhe(boleto, 2))
    linhas.append(gerar_trailer(3))

    with open("REMESSA_TESTE.REM", "w", encoding="latin-1") as f:
        for linha in linhas:
            f.write(linha + "\r\n")

if __name__ == "__main__":
    gerar_arquivo_rem()
    print("Arquivo REMESSA_TESTE.REM gerado.")
