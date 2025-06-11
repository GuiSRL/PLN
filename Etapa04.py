import re
import nltk
from nltk.corpus import stopwords
from collections import defaultdict

# Função para ler o arquivo
def ler(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            return arquivo.read()
    except Exception as e:
        print(f"Erro ao abrir o arquivo: {e}")
        return None

# Função para limpar lista de palavras
def limpar(lista):
    lixo = '.,:;?!"`´^~()}{[]/\\|@#$%¨&*-'
    quase_limpo = [x.strip(lixo).lower() for x in lista]
    return [x for x in quase_limpo if x.isalpha() or '-' not in x]

# Função de busca com contexto
def buscador(alvo, texto):
    texto = texto.replace('\n', ' ').replace('\t', ' ')
    texto_lower = texto.lower()
    alvo_lower = alvo.lower()
    ocorrencias = []
    encontrado_aqui = texto_lower.find(alvo_lower)
    while encontrado_aqui >= 0:
        pos_inicial = max(encontrado_aqui - 10, 0)
        pos_final = min(encontrado_aqui + len(alvo_lower) + 10, len(texto_lower))
        trecho = texto[pos_inicial:pos_final]
        ocorrencias.append(trecho)
        encontrado_aqui = texto_lower.find(alvo_lower, encontrado_aqui + 1)
    return ocorrencias, f"--- A palavra se repetiu {len(ocorrencias)} vezes. ---"

# Função para contar ocorrências
def ocorrencias(lista_palavras):
    dicionario = defaultdict(int)
    for p in lista_palavras:
        dicionario[p] += 1
    return dicionario

# --- Execução ---
texto = ler('Ubirajara.txt')

if texto:
    print(f"Tamanho original do texto: {len(texto)}")

    palavras = limpar(texto.split())
    print(f"Total de palavras (limpas): {len(palavras)}")

    # Dimensão do vocabulário
    vocabulario = set(palavras)
    print(f"Dimensão do vocabulário: {len(vocabulario)}")

    # Riqueza textual
    riqueza = len(vocabulario) / len(palavras)
    print(f"Riqueza textual: {riqueza:.4f}")

    # Dicionário de ocorrências
    dic = ocorrencias(palavras)

    # Top 50 palavras mais frequentes
    mf = sorted(dic.items(), key=lambda tupla: tupla[1], reverse=True)[:50]
    print("\nTop 50 palavras mais frequentes:")
    for palavra, n in mf:
        print(f"{palavra}\t{n}")

    # Remover stopwords
    stopwords_pt = stopwords.words('portuguese')
    frequentes_plenas = [x for x in mf if x[0] not in stopwords_pt]

    print("\nTop palavras frequentes (sem stopwords):")
    for palavra, n in frequentes_plenas:
        print(f"{palavra}\t{n}")

    # Exemplo de busca contextual
    termo = 'peito'
    resultados, resumo = buscador(termo, texto)
    print(f"\nOcorrências da palavra '{termo}':")
    for trecho in resultados:
        print(trecho)
    print(resumo)
else:
    print("Não foi possível ler o arquivo.")
