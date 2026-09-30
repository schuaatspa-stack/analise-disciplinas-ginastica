from ast import Lambda


disciplinas = [
    {"ies": "IFPR Palmas", "nome": "Ginástica Geral", "ch_total": 80, "ch_ext": 16, "perc_ext": 20.0},
    {"ies": "IFPR Palmas", "nome": "Ginástica Artística", "ch_total": 40, "ch_ext": 8, "perc_ext": 20.0},
    {"ies": "IFPR Palmas", "nome": "Estudos Avançados da Ginástica Rítmica", "ch_total": 40, "ch_ext": 8, "perc_ext": 20.0},
    {"ies": "IFPR Palmas", "nome": "Ginástica Rítmica", "ch_total": 40, "ch_ext": 8, "perc_ext": 20.0},
    {"ies": "UEL", "nome": "Ginástica", "ch_total": 60, "ch_ext": 0, "perc_ext": 0.0},
    {"ies": "UEL", "nome": "Ginástica Artística", "ch_total": 30, "ch_ext": 0, "perc_ext": 0.0},
    {"ies": "UEM", "nome": "Introdução à Ginástica", "ch_total": 68, "ch_ext": 0, "perc_ext": 0.0},
    {"ies": "UEM", "nome": "Ginástica e Esportes Ginásticos", "ch_total": 34, "ch_ext": 0, "perc_ext": 0.0},
    {"ies": "UEM", "nome": "Ginásticas", "ch_total": 34, "ch_ext": 0, "perc_ext": 0.0},
    {"ies": "UEM Ivaiporã", "nome": "Fundamentos Ginásticos", "ch_total": 80, "ch_ext": 12, "perc_ext": 15.0},
    {"ies": "UEM Ivaiporã", "nome": "Treinamento Desportivo em Ginástica Rítmica", "ch_total": 68, "ch_ext": 0, "perc_ext": 0.0},
    {"ies": "UEPG", "nome": "Ginástica", "ch_total": 68, "ch_ext": 15, "perc_ext": 22.1},
    {"ies": "UEPG", "nome": "Ginástica Artística (Bacharel)", "ch_total": 68, "ch_ext": 0, "perc_ext": 0.0},
    {"ies": "UEPG", "nome": "Ginástica Artística (Licenc.)", "ch_total": 68, "ch_ext": 0, "perc_ext": 0.0},
    {"ies": "UEPG", "nome": "Ginástica Rítmica (Bacharel)", "ch_total": 68, "ch_ext": 0, "perc_ext": 0.0},
    {"ies": "UEPG", "nome": "Ginástica Rítmica (Licenc.)", "ch_total": 68, "ch_ext": 0, "perc_ext": 0.0},
    {"ies": "UNICENTRO", "nome": "Ginástica", "ch_total": 102, "ch_ext": 4, "perc_ext": 3.9},
    {"ies": "UNICENTRO", "nome": "Ginástica Escolar", "ch_total": 102, "ch_ext": 0, "perc_ext": 0.0},
    {"ies": "UNICENTRO Irati", "nome": "Fundamentos Da Ginástica", "ch_total": 68, "ch_ext": 0, "perc_ext": 0.0},
    {"ies": "UNICENTRO Irati", "nome": "Ginástica Escolar", "ch_total": 68, "ch_ext": 0, "perc_ext": 0.0},
    {"ies": "UENP", "nome": "Ginástica Geral", "ch_total": 60, "ch_ext": 0, "perc_ext": 0.0},
    {"ies": "UNIOESTE", "nome": "Ginásticas", "ch_total": 68, "ch_ext": 0, "perc_ext": 0.0},
    {"ies": "UFPR Litoral", "nome": "Ginástica", "ch_total": 60, "ch_ext": 30, "perc_ext": 50.0},
    {"ies": "UFPR Litoral", "nome": "Ginástica Escolar", "ch_total": 60, "ch_ext": 0, "perc_ext": 0.0},
    {"ies": "UFPR Curitiba", "nome": "Fundamentos da Ginástica e do Circo", "ch_total": 60, "ch_ext": 15, "perc_ext": 25.0},
    {"ies": "UFPR Curitiba", "nome": "Esportes Ginásticos", "ch_total": 60, "ch_ext": 15, "perc_ext": 25.0},
    {"ies": "UTFPR", "nome": "Fundamentos de Ginástica", "ch_total": 60, "ch_ext": 0, "perc_ext": 0.0},
    {"ies": "UTFPR", "nome": "Ginástica Artística", "ch_total": 30, "ch_ext": 0, "perc_ext": 0.0},
    {"ies": "UTFPR", "nome": "Ginástica Rítmica", "ch_total": 45, "ch_ext": 0, "perc_ext": 0.0},
    {"ies": "UTFPR", "nome": "Ginástica Para Todos", "ch_total": 45, "ch_ext": 0, "perc_ext": 0.0},
]
soma = 0
for disciplina in disciplinas:
    soma = soma + disciplina["perc_ext"]

media = soma / len(disciplinas)
print(f"Média de % de extensão: {media:.1f}%")

zero_ext = 0
for disciplina in disciplinas:
    if disciplina["perc_ext"] == 0:
        zero_ext = zero_ext + 1

print(f"Disciplinas sem nenhuma extensão: {zero_ext} de {len(disciplinas)}")

maior_perc = 0
maior_disciplina = ""

for disciplina in disciplinas:
    if disciplina["perc_ext"] > maior_perc:
        maior_perc = disciplina["perc_ext"]
        maior_disciplina = disciplina["nome"] + " (" + disciplina["ies"] + ")"

print(f"Maior % de extensão: {maior_disciplina} com {maior_perc}%")

soma_por_ies = {}
contagem_por_ies = {}

for disciplina in disciplinas:
    ies = disciplina["ies"]
    if ies not in soma_por_ies:
        soma_por_ies[ies] = 0
        contagem_por_ies[ies] = 0
    soma_por_ies[ies] = soma_por_ies[ies] + disciplina["perc_ext"]
    contagem_por_ies[ies] = contagem_por_ies[ies] + 1

for ies in soma_por_ies:
    media_ies = soma_por_ies[ies] / contagem_por_ies[ies]
    print(f"{ies}: {media_ies:.1f}% de média")
lista_media = []
for ies in soma_por_ies:
    media_ies = soma_por_ies[ies] / contagem_por_ies[ies]
    lista_media.append((ies, media_ies))

lista_media.sort(key=lambda x: x[1], reverse=True)

print("\n== Ranking de IES por % de extensão ==\n")
for ies, media_ies in lista_media:
    print(f"{ies}: {media_ies:.1f}%")

import csv

with open("ranking_ies.csv", "w", newline="", encoding="utf-8") as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerow(["IES", "Media_Perc_Extensao"])
    for ies, media_ies in lista_media:
        escritor.writerow([ies, f"{media_ies:.1f}"])

print("\nArquivo ranking_ies.csv salvo com sucesso!")
        
        