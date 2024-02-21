# import PyPDF2
# import re

# def encontrar_sequencia(texto_pagina):
#     # Encontrar a sequência "DEMONSTRATIVO DE CÁLCULO" seguida de "DEPRE 3.4"
#     padrao_sequencia = r'DEMONSTRATIVO DE CÁLCULO.*?DEPRE 3\.4'
#     return re.search(padrao_sequencia, texto_pagina, re.IGNORECASE | re.DOTALL)

# def extrair_informacoes(texto):
#     informacoes = {}

#     # Procurar padrões de informações específicas
#     padrao_processo = r'Processo Nº: (\S+)'
#     padrao_ep = r'E\.P\. Nº: (\S+)'
#     padrao_vara = r'Vara: (\S+)'
#     padrao_comarca = r'Comarca: (\S+)'
#     padrao_autor = r'Autor: (.+)'
#     padrao_advogado = r'Advogado: (.+)'
#     padrao_entidade = r'Entidade: (.+)'
#     padrao_acao = r'Ação: (.+)'
#     padrao_liquidação = r'Liquidação: (\S+)'
#     padrao_valor_principal = r'VALOR PRINCIPAL: (\S+)'
#     padrao_honorarios = r'HONORÁRIOS ADVOCATÍCIOS: (.+)'
#     padrao_custas = r'CUSTAS: (\S+)'
#     padrao_embargos = r'EMBARGOS A EXECUÇÃO: (\S+)'
#     padrao_despesas = r'DESPESAS: (\S+)'
#     padrao_total = r'TOTAL: (\S+)'

#     informacoes['Processo Nº'] = re.search(padrao_processo, texto, re.IGNORECASE).group(1) if re.search(padrao_processo, texto, re.IGNORECASE) else None
#     informacoes['E.P. Nº'] = re.search(padrao_ep, texto, re.IGNORECASE).group(1) if re.search(padrao_ep, texto, re.IGNORECASE) else None
#     informacoes['Vara'] = re.search(padrao_vara, texto, re.IGNORECASE).group(1) if re.search(padrao_vara, texto, re.IGNORECASE) else None
#     informacoes['Comarca'] = re.search(padrao_comarca, texto, re.IGNORECASE).group(1) if re.search(padrao_comarca, texto, re.IGNORECASE) else None
#     informacoes['Autor'] = re.search(padrao_autor, texto, re.IGNORECASE).group(1) if re.search(padrao_autor, texto, re.IGNORECASE) else None
#     informacoes['Advogado'] = re.search(padrao_advogado, texto, re.IGNORECASE).group(1) if re.search(padrao_advogado, texto, re.IGNORECASE) else None
#     informacoes['Entidade'] = re.search(padrao_entidade, texto, re.IGNORECASE).group(1) if re.search(padrao_entidade, texto, re.IGNORECASE) else None
#     informacoes['Ação'] = re.search(padrao_acao, texto, re.IGNORECASE).group(1) if re.search(padrao_acao, texto, re.IGNORECASE) else None
#     informacoes['Valor em'] = re.search(padrao_liquidação, texto, re.IGNORECASE).group(1) if re.search(padrao_liquidação, texto, re.IGNORECASE) else None
#     informacoes['VALOR PRINCIPAL'] = re.search(padrao_valor_principal, texto, re.IGNORECASE).group(1) if re.search(padrao_valor_principal, texto, re.IGNORECASE) else None
#     informacoes['HONORÁRIOS ADVOCATÍCIOS'] = re.search(padrao_honorarios, texto, re.IGNORECASE).group(1) if re.search(padrao_honorarios, texto, re.IGNORECASE) else None
#     informacoes['CUSTAS'] = re.search(padrao_custas, texto, re.IGNORECASE).group(1) if re.search(padrao_custas, texto, re.IGNORECASE) else None
#     informacoes['EMBARGOS A EXECUÇÃO'] = re.search(padrao_embargos, texto, re.IGNORECASE).group(1) if re.search(padrao_embargos, texto, re.IGNORECASE) else None
#     informacoes['DESPESAS'] = re.search(padrao_despesas, texto, re.IGNORECASE).group(1) if re.search(padrao_despesas, texto, re.IGNORECASE) else None
#     informacoes['TOTAL'] = re.search(padrao_total, texto, re.IGNORECASE).group(1) if re.search(padrao_total, texto, re.IGNORECASE) else None

#     return informacoes

# def aplicar_filtro_paginas(caminho_pdf):
#     with open(caminho_pdf, 'rb') as arquivo:
#         leitor_pdf = PyPDF2.PdfReader(arquivo)
#         for numero_pagina, pagina in enumerate(leitor_pdf.pages, start=1):
#             texto_pagina = pagina.extract_text()
#             if "DEMONSTRATIVO DE CÁLCULO" in texto_pagina and "DEPRE 3.4" in texto_pagina:
#                 # Encontrar as posições das linhas de "Contador(a) Judiciário" e "Supervisor(a) de Serviço"
#                 linha_contador = texto_pagina.find("Contador(a) Judiciário")
#                 linha_supervisor = texto_pagina.find("Supervisor(a) de Serviço")
                
#                 # Remover as informações especificadas do texto da página
#                 texto_pagina = texto_pagina[:linha_contador].strip()
#                 texto_pagina = texto_pagina.replace("Proc.DEPRE Nº", "")
#                 texto_pagina = texto_pagina.replace("DEMONSTRATIVO DE CÁLCULO", "")
#                 texto_pagina = texto_pagina.replace("DEPRE 3.4", "")
#                 texto_pagina = texto_pagina.replace("RESUMO DO PROCESSO", "")
#                 texto_pagina = texto_pagina.replace("Liquidação", "")
                
#                 print(f"Conteúdo da página {numero_pagina}:\n{texto_pagina}")
#                 print("=" * 50)

# # Substitua 'seu_arquivo.pdf' pelo caminho real do seu arquivo
# aplicar_filtro_paginas('C:/Users/pooul/Downloads/pastaTeste/teste2.pdf')

# teste para usar tudo problema no total 

# import re
# import pandas as pd

# def extrair_informacoes(texto):
#     informacoes = {}

#     # Procurar padrões de informações específicas
#     padrao_processo = r'Processo Nº(?:\s|:)([\w\/.-]+)'
#     padrao_ep = r'E\.P\. Nº(?:\s|:)([\w\/.-]+)'
#     padrao_vara = r'Vara(?:\s|:)([^\n]+)'
#     padrao_comarca = r'Comarca(?:\s|:)([^\n]+)'
#     padrao_autor = r'Autor(?:\s|:)([^\n]+)'
#     padrao_advogado = r'Advogado(?:\s|:)([^\n]+)'
#     padrao_entidade = r'Entidade(?:\s|:)([^\n]+)'
#     padrao_acao = r'Ação(?:\s|:)([^\n]+)'
#     padrao_liquidação = r'Liquidação(?:\s|:)([^\n]+)'
#     padrao_valor_principal = r'VALOR PRINCIPAL(?:\s|:)\s*R\$\s*([\d.,]+)'
#     padrao_honorarios = r'HONORÁRIOS ADVOCATÍCIOS(?:\s|:)\s*R\$\s*([\d.,]+)'
#     padrao_custas = r'CUSTAS(?:\s|:)\s*R\$\s*([\d.,]+)'
#     padrao_embargos = r'EMBARGOS A EXECUÇÃO(?:\s|:)\s*R\$\s*([\d.,]+)'
#     padrao_despesas = r'DESPESAS(?:\s|:)\s*R\$\s*([\d.,]+)'
#     padrao_sub_total = r'SUB-TOTAL(?:\s|:)\s*R\$\s*([\d.,]+)'
#     padrao_juros_moratorios = r'JUROS MORATÓRIOS(?:\s|:)\s*R\$\s*([\d.,]+)'
#     padrao_total = r'TOTAL\s*R\$\s*([\d.,]+)'  # Novo padrão para o valor total

#     informacoes['Processo Nº'] = re.search(padrao_processo, texto, re.IGNORECASE).group(1) if re.search(padrao_processo, texto, re.IGNORECASE) else None
#     informacoes['E.P. Nº'] = re.search(padrao_ep, texto, re.IGNORECASE).group(1) if re.search(padrao_ep, texto, re.IGNORECASE) else None
#     informacoes['Vara'] = re.search(padrao_vara, texto, re.IGNORECASE).group(1) if re.search(padrao_vara, texto, re.IGNORECASE) else None
#     informacoes['Comarca'] = re.search(padrao_comarca, texto, re.IGNORECASE).group(1) if re.search(padrao_comarca, texto, re.IGNORECASE) else None
#     informacoes['Autor'] = re.search(padrao_autor, texto, re.IGNORECASE).group(1) if re.search(padrao_autor, texto, re.IGNORECASE) else None
#     informacoes['Advogado'] = re.search(padrao_advogado, texto, re.IGNORECASE).group(1) if re.search(padrao_advogado, texto, re.IGNORECASE) else None
#     informacoes['Entidade'] = re.search(padrao_entidade, texto, re.IGNORECASE).group(1) if re.search(padrao_entidade, texto, re.IGNORECASE) else None
#     informacoes['Ação'] = re.search(padrao_acao, texto, re.IGNORECASE).group(1) if re.search(padrao_acao, texto, re.IGNORECASE) else None
#     informacoes['Valor em'] = re.search(padrao_liquidação, texto, re.IGNORECASE).group(1) if re.search(padrao_liquidação, texto, re.IGNORECASE) else None
#     informacoes['VALOR PRINCIPAL'] = re.search(padrao_valor_principal, texto, re.IGNORECASE).group(1) if re.search(padrao_valor_principal, texto, re.IGNORECASE) else None
#     informacoes['SUB-TOTAL'] = re.search(padrao_sub_total, texto, re.IGNORECASE).group(1) if re.search(padrao_sub_total, texto, re.IGNORECASE) else None
#     informacoes['JUROS MORATÓRIOS'] = re.search(padrao_juros_moratorios, texto, re.IGNORECASE).group(1) if re.search(padrao_juros_moratorios, texto, re.IGNORECASE) else None
#     informacoes['HONORÁRIOS ADVOCATÍCIOS'] = re.search(padrao_honorarios, texto, re.IGNORECASE).group(1) if re.search(padrao_honorarios, texto, re.IGNORECASE) else None
#     informacoes['CUSTAS'] = re.search(padrao_custas, texto, re.IGNORECASE).group(1) if re.search(padrao_custas, texto, re.IGNORECASE) else None
#     informacoes['EMBARGOS A EXECUÇÃO'] = re.search(padrao_embargos, texto, re.IGNORECASE).group(1) if re.search(padrao_embargos, texto, re.IGNORECASE) else None
#     informacoes['DESPESAS'] = re.search(padrao_despesas, texto, re.IGNORECASE).group(1) if re.search(padrao_despesas, texto, re.IGNORECASE) else None
#     informacoes['TOTAL'] = re.search(padrao_total, texto, re.IGNORECASE).group(1) if re.search(padrao_total, texto, re.IGNORECASE) else None

#     return informacoes


# # Texto de exemplo fornecido
# texto_exemplo = """
# Proc.DEPRE Nº
# DEMONSTRATIVO DE CÁLCULO
# DEPRE 3.4
# Processo Nº 0419433-05.1996.8.26.0053
# 7001659-12.2002.8.26.0500 E.P. Nº 1659/2002
# Vara SETOR DE EXECUÇÕES CONTRA A FAZENDA PÚBLICA
# Comarca São Paulo - SP
# Autor IZALTINA TRINDADE FERREIRA E O/O
# Advogado EDIANGELI ROSSI MIGLIANO
# Entidade AE001 - CBPM - CAIXA BENEFICENTE DA POLÍCIA MILITAR
# Advogado LÉO COSTA RAMOS
# Ação ORDINÁRIA
# RESUMO DO PROCESSO
# Liquidação Valor em 29/05/2020
# VALOR PRINCIPAL R$ 2.356.458,68
# DESCONTO PREVIDENCIÁRIO: CBPM R$ 0,00
# ASSISTÊNCIA MÉDICA: CRUZ AZUL R$ 21.897,53
# SUB-TOTAL R$ 2.378.356,21
# JUROS MORATÓRIOS R$ 2.889.477,23
# HONORÁRIOS ADVOCATÍCIOS R$ 622.245,21
# CUSTAS R$ 493,01
# EMBARGOS A EXECUÇÃO R$ 0,00
# DESPESAS R$ 0,00
# TOTAL R$ 5.890.571,66
# Banco Agência Conta Judicial Data do Depósito Valor do Depósito
# 001 5905 2200131959454 29/05/2020 5.890.571,66
# RENATO CÉSAR MOREIRA
# Contador(a) Judiciário
# DEPRE 3.4
# ANTONIO CARLOS LADISLAU ALVES
# Supervisor(a) de Serviço
# """

# # Extrair todas as informações do texto fornecido
# informacoes_extraidas = extrair_informacoes(texto_exemplo)

# # Converter as informações extraídas em um DataFrame pandas
# df = pd.DataFrame([informacoes_extraidas])

# # Salvar as informações em um arquivo Excel
# df.to_excel('informacoes_extraidas.xlsx', index=False)

# print("Informações extraídas foram salvas em 'informacoes_extraidas.xlsx'")

# import re
# import pandas as pd
# from PyPDF2 import PdfReader

# def extrair_informacoes(texto):
#     informacoes = {}

#     # Procurar padrões de informações específicas
#     padrao_processo = r'(?:Processo\sNº|Processo:)\s*([\w.-]+)'
#     padrao_ep = r'E\.P\. Nº(?:\s|:)([\w\/.-]+)'
#     padrao_vara = r'Vara(?:\s|:)([^\n]+)'
#     padrao_comarca = r'Comarca(?:\s|:)([^\n]+)'
#     padrao_autor = r'Autor(?:\s|:)([^\n]+)'
#     padrao_advogado = r'Advogado(?:\s|:)([^\n]+)'
#     padrao_entidade = r'Entidade(?:\s|:)([^\n]+)'
#     padrao_acao = r'Ação(?:\s|:)([^\n]+)'
#     padrao_liquidação = r'Liquidação(?:\s|:)([^\n]+)'
#     padrao_valor_principal = r'VALOR PRINCIPAL(?:\s|:)([^\n]+)'
#     padrao_sub_total = r'SUB-TOTAL(?:\s|:)([^\n]+)'
#     padrao_juros_moratorios = r'JUROS MORATÓRIOS(?:\s|:)([^\n]+)'
#     padrao_honorarios_advocaticios = r'HONORÁRIOS ADVOCATÍCIOS(?:\s|:)([^\n]+)'
#     padrao_custas = r'CUSTAS(?:\s|:)([^\n]+)'
#     padrao_embargos = r'EMBARGOS A EXECUÇÃO(?:\s|:)([^\n]+)'
#     padrao_despesas = r'DESPESAS(?:\s|:)([^\n]+)'
#     padrao_total = r'TOTAL:?\s*(?:R\$\s*)?([\d,.]+)'









#     informacoes['Processo Nº'] = re.search(padrao_processo, texto, re.IGNORECASE).group(1) if re.search(padrao_processo, texto, re.IGNORECASE) else None
#     informacoes['E.P. Nº'] = re.search(padrao_ep, texto, re.IGNORECASE).group(1) if re.search(padrao_ep, texto, re.IGNORECASE) else None
#     informacoes['Vara'] = re.search(padrao_vara, texto, re.IGNORECASE).group(1) if re.search(padrao_vara, texto, re.IGNORECASE) else None
#     informacoes['Comarca'] = re.search(padrao_comarca, texto, re.IGNORECASE).group(1) if re.search(padrao_comarca, texto, re.IGNORECASE) else None
#     informacoes['Autor'] = re.search(padrao_autor, texto, re.IGNORECASE).group(1) if re.search(padrao_autor, texto, re.IGNORECASE) else None
#     informacoes['Advogado'] = re.search(padrao_advogado, texto, re.IGNORECASE).group(1) if re.search(padrao_advogado, texto, re.IGNORECASE) else None
#     informacoes['Entidade'] = re.search(padrao_entidade, texto, re.IGNORECASE).group(1) if re.search(padrao_entidade, texto, re.IGNORECASE) else None
#     informacoes['Ação'] = re.search(padrao_acao, texto, re.IGNORECASE).group(1) if re.search(padrao_acao, texto, re.IGNORECASE) else None
#     informacoes['Valor em'] = re.search(padrao_liquidação, texto, re.IGNORECASE).group(1) if re.search(padrao_liquidação, texto, re.IGNORECASE) else None
#     informacoes['VALOR PRINCIPAL'] = re.search(padrao_valor_principal, texto, re.IGNORECASE).group(1) if re.search(padrao_valor_principal, texto, re.IGNORECASE) else None
#     informacoes['SUB-TOTAL'] = re.search(padrao_sub_total, texto, re.IGNORECASE).group(1) if re.search(padrao_sub_total, texto, re.IGNORECASE) else None
#     informacoes['JUROS MORATÓRIOS'] = re.search(padrao_juros_moratorios, texto, re.IGNORECASE).group(1) if re.search(padrao_juros_moratorios, texto, re.IGNORECASE) else None
#     informacoes['HONORÁRIOS ADVOCATÍCIOS'] = re.search(padrao_honorarios_advocaticios, texto, re.IGNORECASE).group(1) if re.search(padrao_honorarios_advocaticios, texto, re.IGNORECASE) else None
#     informacoes['CUSTAS'] = re.search(padrao_custas, texto, re.IGNORECASE).group(1) if re.search(padrao_custas, texto, re.IGNORECASE) else None
#     informacoes['EMBARGOS A EXECUÇÃO'] = re.search(padrao_embargos, texto, re.IGNORECASE).group(1) if re.search(padrao_embargos, texto, re.IGNORECASE) else None
#     informacoes['DESPESAS'] = re.search(padrao_despesas, texto, re.IGNORECASE).group(1) if re.search(padrao_despesas, texto, re.IGNORECASE) else None
#     informacoes['TOTAL'] = re.search(padrao_total, texto, re.IGNORECASE).group(1) if re.search(padrao_total, texto, re.IGNORECASE) else None

#     return informacoes

# def extrair_texto_de_pdf(caminho_pdf):
#     texto_total = ''
#     with open(caminho_pdf, 'rb') as file:
#         reader = PdfReader(file)
#         for num_pagina, page in enumerate(reader.pages, start=1):
#             texto_pagina = page.extract_text()
#             texto_total += f"========================= Página {num_pagina} =========================\n"
#             texto_total += texto_pagina
#     return texto_total


# # Caminho para o arquivo PDF
# caminho_pdf = 'C:/Users/pooul/Downloads/pastaTeste/teste2.pdf'

# # Extrair texto do PDF
# texto_do_pdf = extrair_texto_de_pdf(caminho_pdf)

# # Extrair todas as informações do texto fornecido
# informacoes_extraidas = extrair_informacoes(texto_do_pdf)

# # Imprimir as informações extraídas no console
# for chave, valor in informacoes_extraidas.items():
#     print(f"{chave}: {valor}")

# # Converter as informações extraídas em um DataFrame pandas
# df = pd.DataFrame([informacoes_extraidas])

# # Salvar as informações em um arquivo Excel
# df.to_excel('informacoes_extraidas.xlsx', index=False)

# print("Informações extraídas foram salvas em 'informacoes_extraidas.xlsx'")

# import re
# import pandas as pd
# from PyPDF2 import PdfReader

# def extrair_informacoes(texto):
#     informacoes = {}
    
#     # Padrões de regex para extrair informações específicas
#     padrao_processo = r'(?:Processo\sNº|Processo:)\s*([\w.-]+)'
#     padrao_ep = r'E\.P\. Nº(?:\s|:)([\w\/.-]+)'
#     padrao_vara = r'Vara(?:\s|:)([^\n]+)'
#     padrao_comarca = r'Comarca(?:\s|:)([^\n]+)'
#     padrao_autor = r'Autor(?:\s|:)([^\n]+)'
#     padrao_advogado = r'Advogado(?:\s|:)([^\n]+)'
#     padrao_entidade = r'Entidade(?:\s|:)([^\n]+)'
#     padrao_acao = r'Ação(?:\s|:)([^\n]+)'
#     padrao_liquidação = r'Liquidação(?:\s|:)([^\n]+)'
#     padrao_valor_principal = r'VALOR PRINCIPAL(?:\s|:)([^\n]+)'
#     padrao_sub_total = r'SUB-TOTAL(?:\s|:)([^\n]+)'
#     padrao_juros_moratorios = r'JUROS MORATÓRIOS(?:\s|:)([^\n]+)'
#     padrao_honorarios_advocaticios = r'HONORÁRIOS ADVOCATÍCIOS(?:\s|:)([^\n]+)'
#     padrao_custas = r'CUSTAS(?:\s|:)([^\n]+)'
#     padrao_embargos = r'EMBARGOS A EXECUÇÃO(?:\s|:)([^\n]+)'
#     padrao_despesas = r'DESPESAS(?:\s|:)([^\n]+)'
#     padrao_total = r'TOTAL:?\s*(?:R\$\s*)?([\d,.]+)'
    
#     # Extrair informações usando regex
#     informacoes['Processo Nº'] = re.search(padrao_processo, texto, re.IGNORECASE).group(1) if re.search(padrao_processo, texto, re.IGNORECASE) else None
#     informacoes['E.P. Nº'] = re.search(padrao_ep, texto, re.IGNORECASE).group(1) if re.search(padrao_ep, texto, re.IGNORECASE) else None
#     informacoes['Vara'] = re.search(padrao_vara, texto, re.IGNORECASE).group(1) if re.search(padrao_vara, texto, re.IGNORECASE) else None
#     informacoes['Comarca'] = re.search(padrao_comarca, texto, re.IGNORECASE).group(1) if re.search(padrao_comarca, texto, re.IGNORECASE) else None
#     informacoes['Autor'] = re.search(padrao_autor, texto, re.IGNORECASE).group(1) if re.search(padrao_autor, texto, re.IGNORECASE) else None
#     informacoes['Advogado'] = re.search(padrao_advogado, texto, re.IGNORECASE).group(1) if re.search(padrao_advogado, texto, re.IGNORECASE) else None
#     informacoes['Entidade'] = re.search(padrao_entidade, texto, re.IGNORECASE).group(1) if re.search(padrao_entidade, texto, re.IGNORECASE) else None
#     informacoes['Ação'] = re.search(padrao_acao, texto, re.IGNORECASE).group(1) if re.search(padrao_acao, texto, re.IGNORECASE) else None
#     informacoes['Valor em'] = re.search(padrao_liquidação, texto, re.IGNORECASE).group(1) if re.search(padrao_liquidação, texto, re.IGNORECASE) else None
#     informacoes['VALOR PRINCIPAL'] = re.search(padrao_valor_principal, texto, re.IGNORECASE).group(1) if re.search(padrao_valor_principal, texto, re.IGNORECASE) else None
#     informacoes['SUB-TOTAL'] = re.search(padrao_sub_total, texto, re.IGNORECASE).group(1) if re.search(padrao_sub_total, texto, re.IGNORECASE) else None
#     informacoes['JUROS MORATÓRIOS'] = re.search(padrao_juros_moratorios, texto, re.IGNORECASE).group(1) if re.search(padrao_juros_moratorios, texto, re.IGNORECASE) else None
#     informacoes['HONORÁRIOS ADVOCATÍCIOS'] = re.search(padrao_honorarios_advocaticios, texto, re.IGNORECASE).group(1) if re.search(padrao_honorarios_advocaticios, texto, re.IGNORECASE) else None
#     informacoes['CUSTAS'] = re.search(padrao_custas, texto, re.IGNORECASE).group(1) if re.search(padrao_custas, texto, re.IGNORECASE) else None
#     informacoes['EMBARGOS A EXECUÇÃO'] = re.search(padrao_embargos, texto, re.IGNORECASE).group(1) if re.search(padrao_embargos, texto, re.IGNORECASE) else None
#     informacoes['DESPESAS'] = re.search(padrao_despesas, texto, re.IGNORECASE).group(1) if re.search(padrao_despesas, texto, re.IGNORECASE) else None
#     informacoes['TOTAL'] = re.search(padrao_total, texto, re.IGNORECASE).group(1) if re.search(padrao_total, texto, re.IGNORECASE) else None

#     return informacoes

# def extrair_texto_de_pdf(caminho_pdf):
#     texto_por_pagina = []
#     with open(caminho_pdf, 'rb') as file:
#         reader = PdfReader(file)
#         for page in reader.pages:
#             texto_pagina = page.extract_text()
#             texto_por_pagina.append(texto_pagina)

#     informacoes_paginas = []
#     for num_pagina, texto_pagina in enumerate(texto_por_pagina, start=1):
#         # Verificar se a página contém os padrões desejados
#         if re.search(r'DEMONSTRATIVO DE CÁLCULO', texto_pagina, re.IGNORECASE) and re.search(r'DEPRE 3\.4', texto_pagina, re.IGNORECASE):
#             informacoes_pagina = extrair_informacoes(texto_pagina)
#             if informacoes_pagina:
#                 informacoes_pagina['Página'] = num_pagina
#                 informacoes_paginas.append(informacoes_pagina)

#     return informacoes_paginas

# # Caminho para o arquivo PDF
# caminho_pdf = 'C:/Users/pooul/Downloads/pastaTeste/robo02.pdf'

# # Extrair informações do PDF
# informacoes_paginas = extrair_texto_de_pdf(caminho_pdf)

# # Converter as informações extraídas em um DataFrame pandas
# df = pd.DataFrame(informacoes_paginas)

# # Salvar as informações em um arquivo Excel
# df.to_excel('informacoes_extraidas.xlsx', index=False)

# print("Informações extraídas foram salvas em 'informacoes_extraidas.xlsx'")



import re
import pandas as pd
from PyPDF2 import PdfReader

def extrair_informacoes(texto):
    informacoes = {}
    
    # Padrões de regex para extrair informações específicas
    padrao_processo = r'(?:Processo\sNº|Processo:)\s*(\d{7}-\d{2}\.\d{4}\.\d{1,2}\.\d{4,})'
    padrao_vara = r'Vara(?:\s|:)([^\n]+)'
    padrao_comarca = r'Comarca(?:\s|:)([^\n]+)'
    padrao_autor = r'Autor(?:\s|:)([^\n]+)'
    padrao_advogado = r'Advogado(?:\s|:)([^\n]+)'
    padrao_entidade = r'Entidade(?:\s|:)([^\n]+)'
    padrao_acao = r'Ação(?:\s|:)([^\n]+)'
    padrao_liquidação = r'Liquidação(?:\s|:)([^\n]+)'
    padrao_valor_principal = r'VALOR PRINCIPAL(?:\s|:)([^\n]+)'
    padrao_sub_total = r'SUB-TOTAL(?:\s|:)([^\n]+)'
    padrao_juros_moratorios = r'JUROS MORATÓRIOS(?:\s|:)([^\n]+)'
    padrao_honorarios_advocaticios = r'HONORÁRIOS ADVOCATÍCIOS(?:\s|:)([^\n]+)'
    padrao_embargos = r'EMBARGOS A EXECUÇÃO(?:\s|:)([^\n]+)'
    padrao_total = r'TOTAL:?\s*(?:R\$\s*)?([\d,.]+)'
    
    # Imprimir o texto da página para depuração
    print("Texto da página:")
    print(texto)

    # Extrair informações usando regex
    informacoes['Processo Nº'] = re.search(padrao_processo, texto, re.IGNORECASE).group(1) if re.search(padrao_processo, texto, re.IGNORECASE) else None
    informacoes['Vara'] = re.search(padrao_vara, texto, re.IGNORECASE).group(1) if re.search(padrao_vara, texto, re.IGNORECASE) else None
    informacoes['Comarca'] = re.search(padrao_comarca, texto, re.IGNORECASE).group(1) if re.search(padrao_comarca, texto, re.IGNORECASE) else None
    informacoes['Autor'] = re.search(padrao_autor, texto, re.IGNORECASE).group(1) if re.search(padrao_autor, texto, re.IGNORECASE) else None
    informacoes['Advogado'] = re.search(padrao_advogado, texto, re.IGNORECASE).group(1) if re.search(padrao_advogado, texto, re.IGNORECASE) else None
    informacoes['Entidade'] = re.search(padrao_entidade, texto, re.IGNORECASE).group(1) if re.search(padrao_entidade, texto, re.IGNORECASE) else None
    informacoes['Ação'] = re.search(padrao_acao, texto, re.IGNORECASE).group(1) if re.search(padrao_acao, texto, re.IGNORECASE) else None
    informacoes['Valor em'] = re.search(padrao_liquidação, texto, re.IGNORECASE).group(1) if re.search(padrao_liquidação, texto, re.IGNORECASE) else None
    informacoes['VALOR PRINCIPAL'] = re.search(padrao_valor_principal, texto, re.IGNORECASE).group(1) if re.search(padrao_valor_principal, texto, re.IGNORECASE) else None
    informacoes['SUB-TOTAL'] = re.search(padrao_sub_total, texto, re.IGNORECASE).group(1) if re.search(padrao_sub_total, texto, re.IGNORECASE) else None
    informacoes['JUROS MORATÓRIOS'] = re.search(padrao_juros_moratorios, texto, re.IGNORECASE).group(1) if re.search(padrao_juros_moratorios, texto, re.IGNORECASE) else None
    informacoes['HONORÁRIOS ADVOCATÍCIOS'] = re.search(padrao_honorarios_advocaticios, texto, re.IGNORECASE).group(1) if re.search(padrao_honorarios_advocaticios, texto, re.IGNORECASE) else None
    informacoes['EMBARGOS A EXECUÇÃO'] = re.search(padrao_embargos, texto, re.IGNORECASE).group(1) if re.search(padrao_embargos, texto, re.IGNORECASE) else None
    informacoes['TOTAL'] = re.search(padrao_total, texto, re.IGNORECASE).group(1) if re.search(padrao_total, texto, re.IGNORECASE) else None

    return informacoes

def extrair_texto_de_pdf(caminho_pdf):
    texto_por_pagina = []
    with open(caminho_pdf, 'rb') as file:
        reader = PdfReader(file)
        for page in reader.pages:
            texto_pagina = page.extract_text()
            texto_por_pagina.append(texto_pagina)

    informacoes_paginas = []
    for num_pagina, texto_pagina in enumerate(texto_por_pagina, start=1):
        # Verificar se a página contém os padrões desejados
        if re.search(r'DEMONSTRATIVO DE CÁLCULO', texto_pagina, re.IGNORECASE) and re.search(r'DEPRE 2\.4', texto_pagina, re.IGNORECASE):
            informacoes_pagina = extrair_informacoes(texto_pagina)
            if informacoes_pagina:
                informacoes_pagina['Página'] = num_pagina
                informacoes_paginas.append(informacoes_pagina)

    return informacoes_paginas

# Caminho para o arquivo PDF
caminho_pdf = 'C:/Users/pooul/Downloads/pastaTeste/robo02.pdf'

# Extrair informações do PDF
informacoes_paginas = extrair_texto_de_pdf(caminho_pdf)

# Converter as informações extraídas em um DataFrame pandas
df = pd.DataFrame(informacoes_paginas)

# Salvar as informações em um arquivo Excel
df.to_excel('informacoes_extraidas.xlsx', index=False)

print("Informações extraídas foram salvas em 'informacoes_extraidas.xlsx'")







