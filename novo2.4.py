# import PyPDF2
# import pandas as pd
# import re

# def extract_information(pdf_path):
#     with open(pdf_path, "rb") as f:
#         reader = PyPDF2.PdfFileReader(f)
        
#         # Inicializar lista para armazenar os dados
#         data = []
        
#         # Percorrer cada página do PDF
#         for page_num in range(reader.numPages):
#             page = reader.getPage(page_num)
#             text = page.extractText()
#             lines = text.split('\n')
            
#             # Verificar se a página contém os marcadores
#             if "DEMONSTRATIVO DE CÁLCULO" in text and "DEPRE 3.4" in text:
            
#                 # Inicializar dicionário para armazenar os dados desta página
#                 page_data = {
#                     "Página": page_num + 1,
#                     "Processo Nº": None,
#                     "E.P. Nº": None,
#                     "Vara": None,
#                     "Comarca": None,
#                     "Autor(es)": None,
#                     "Advogado(s)": None,
#                     "Entidade": None,
#                     "Ação": None,
#                     "VALOR PRINCIPAL": None,
#                     "DESCONTO PREVIDENCIÁRIO": None,
#                     "ASSISTÊNCIA MÉDICA": None,
#                     "SUB-TOTAL": None,
#                     "JUROS MORATÓRIOS": None,
#                     "TOTAL": None,
#                     "Banco": None,
#                     "Agência": None,
#                     "Conta Judicial": None,
#                     "Data do Depósito": None,
#                     "Valor do Depósito": None
#                 }
                
#                 # Procurar as informações desejadas em cada linha
#                 for line in lines:
#                     if "Processo Nº" in line:
#                         match = re.search(r'\d{10}\-\d{2}\.\d{4}\.\d\.\d{2}\.\d{4}', line)
#                         if match:
#                             page_data["Processo Nº"] = match.group()
#                     elif "E.P. Nº" in line:
#                         match = re.search(r'\d{3}\/\d{4}', line)
#                         if match:
#                             page_data["E.P. Nº"] = match.group()
#                     elif "Vara" in line:
#                         page_data["Vara"] = line.replace("Vara ", "")
#                     elif "Comarca" in line:
#                         page_data["Comarca"] = line.replace("Comarca ", "")
#                     elif "Autor(es)" in line:
#                         page_data["Autor(es)"] = line.replace("Autor(es) ", "")
#                     elif "Advogado(s)" in line:
#                         page_data["Advogado(s)"] = line.replace("Advogado(s) ", "")
#                     elif "Entidade" in line:
#                         page_data["Entidade"] = line.replace("Entidade ", "")
#                     elif "Ação" in line:
#                         page_data["Ação"] = line.replace("Ação ", "")
#                     elif "VALOR PRINCIPAL" in line:
#                         match = re.search(r'R\$ [\d\,\.]+', line)
#                         if match:
#                             page_data["VALOR PRINCIPAL"] = match.group()
#                     elif "DESCONTO PREVIDENCIÁRIO" in line:
#                         match = re.search(r'R\$ [\d\,\.]+', line)
#                         if match:
#                             page_data["DESCONTO PREVIDENCIÁRIO"] = match.group()
#                     elif "ASSISTÊNCIA MÉDICA" in line:
#                         match = re.search(r'R\$ [\d\,\.]+', line)
#                         if match:
#                             page_data["ASSISTÊNCIA MÉDICA"] = match.group()
#                     elif "SUB-TOTAL" in line:
#                         match = re.search(r'R\$ [\d\,\.]+', line)
#                         if match:
#                             page_data["SUB-TOTAL"] = match.group()
#                     elif "JUROS MORATÓRIOS" in line:
#                         match = re.search(r'R\$ [\d\,\.]+', line)
#                         if match:
#                             page_data["JUROS MORATÓRIOS"] = match.group()
#                     elif "TOTAL" in line:
#                         match = re.search(r'R\$ [\d\,\.]+', line)
#                         if match:
#                             page_data["TOTAL"] = match.group()
#                     elif "Banco" in line:
#                         parts = line.split()
#                         if len(parts) >= 6:
#                             page_data["Banco"] = parts[1]
#                             page_data["Agência"] = parts[2]
#                             page_data["Conta Judicial"] = parts[3]
#                             page_data["Data do Depósito"] = parts[4]
#                             page_data["Valor do Depósito"] = parts[5]
                
#                 # Adicionar os dados desta página à lista
#                 data.append(page_data)

#         return data

# pdf_path = "C:/Users/pooul/Downloads/pastaTeste/teste2.pdf"
# result_data = extract_information(pdf_path)

# # Criar DataFrame a partir dos dados extraídos
# df = pd.DataFrame(result_data)

# # Salvar o DataFrame em um arquivo Excel
# excel_path = "output.xlsx"
# df.to_excel(excel_path, index=False)

# print(f"Os dados foram exportados para o arquivo Excel: {excel_path}")

import pdfplumber
import pandas as pd
import re

def extract_information(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        data = []
        for page_num in range(len(pdf.pages)):
            page = pdf.pages[page_num]
            text = page.extract_text()
            lines = text.split('\n')
            
            if "DEMONSTRATIVO DE CÁLCULO" in text:
                version = "DEPRE 2.4" if "DEPRE 2.4" in text else "DEPRE 3.4"
                
                page_data = {
                    "Página": page_num + 1,
                    "Processo Nº": None,
                    "E.P. Nº": None,
                    "Vara": None,
                    "Comarca": None,
                    "Autor(es)": None,
                    "Advogado(s)": None,
                    "Entidade": None,
                    "Ação": None,
                    "Referente a": None,
                    "CPF/CNPJ": None,
                    "VALOR PRINCIPAL": None,
                    "DESCONTO PREVIDENCIÁRIO": None,
                    "ASSISTÊNCIA MÉDICA": None,
                    "SUB-TOTAL": None,
                    "JUROS MORATÓRIOS": None,
                    "TOTAL": None,
                    "Banco": None,
                    "Agência": None,
                    "Conta Judicial": None,
                    "Data do Depósito": None,
                    "Valor do Depósito": None,
                    "OBS.:":None,

                    "Versão": version
                }
                
                for line in lines:
                    if "Processo Nº" in line:
                        match_processo = re.search(r'Processo Nº\s*([\d\.-]+)', line)
                        if match_processo:
                            page_data["Processo Nº"] = match_processo.group(1).strip()
                    elif "E.P. Nº" in line:
                        match_ep = re.search(r'\d{3}\/\d{4}', line)
                        if match_ep:
                            page_data["E.P. Nº"] = match_ep.group()
                    elif "Vara" in line:
                        match_vara = re.search(r'Vara\s*(.+)', text)
                        if match_vara:
                            page_data["Vara"] = match_vara.group(1).strip()




                    elif "Comarca" in line:
                        page_data["Comarca"] = line.replace("Comarca ", "")
                    elif "Autor" in line:
                        match_autor = re.search(r'Autor(?:\(es\))?\s*(.+)', line)
                        if match_autor and match_autor.group(1):
                            page_data["Autor(es)"] = match_autor.group(1).strip()
                    elif "Advogado" in line:
                        match_advogados = re.findall(r'Advogado(?:\(s\))?\s*([^,]+)', line)
                        if match_advogados:
                            advogados = ", ".join(match_advogados)
                            advogados = advogados.replace("s ", "", 1)
                            page_data["Advogado(s)"] = advogados.strip()
                    elif "Entidade" in line:
                        page_data["Entidade"] = line.replace("Entidade ", "")
                    elif "Ação" in line:
                        page_data["Ação"] = line.replace("Ação ", "")
                    elif "CPF/CNPJ" in line:
                        match_cpf_cnpj = re.search(r'CPF/CNPJ (\d{3}\.\d{3}\.\d{3}\-\d{2}|\d{2}\.\d{3}\.\d{3}\/\d{4}\-\d{2})', line)
                        if match_cpf_cnpj:
                            page_data["CPF/CNPJ"] = match_cpf_cnpj.group(1)
                    elif "Referente a" in line or "Calculo referente a" in line:
                        match_referente = re.search(r'(?:Referente|Calculo referente) a (.+)', line)
                        if match_referente and match_referente.group(1):
                            page_data["Referente a"] = match_referente.group(1).strip()
                    elif "VALOR PRINCIPAL" in line:
                        match_valor_principal = re.search(r'R\$ [\d\,\.]+', line)
                        if match_valor_principal:
                            page_data["VALOR PRINCIPAL"] = match_valor_principal.group()
                    elif "DESCONTO PREVIDENCIÁRIO" in line:
                        match_desconto_prev = re.search(r'R\$ [\d\,\.]+', line)
                        if match_desconto_prev:
                            page_data["DESCONTO PREVIDENCIÁRIO"] = match_desconto_prev.group()
                    elif "ASSISTÊNCIA MÉDICA" in line:
                        match_assistencia_medica = re.search(r'R\$ [\d\,\.]+', line)
                        if match_assistencia_medica:
                            page_data["ASSISTÊNCIA MÉDICA"] = match_assistencia_medica.group()
                    elif "SUB-TOTAL" in line:
                        match_sub_total = re.search(r'R\$ [\d\,\.]+', line)
                        if match_sub_total:
                            page_data["SUB-TOTAL"] = match_sub_total.group()
                    elif "JUROS MORATÓRIOS" in line:
                        match_juros_moratorios = re.search(r'R\$ [\d\,\.]+', line)
                        if match_juros_moratorios:
                            page_data["JUROS MORATÓRIOS"] = match_juros_moratorios.group()
                    elif "TOTAL" in line:
                        match_total = re.search(r'R\$ [\d\,\.]+', line)
                        if match_total:
                            page_data["TOTAL"] = match_total.group()
                    elif "Banco" in line:
                        next_line_index = lines.index(line) + 1
                        if next_line_index < len(lines):
                            next_line = lines[next_line_index]
                            parts = next_line.split()

                            # Verifica se há espaços em branco no início de cada parte
                            parts = [part.strip() for part in parts if part.strip()]

                            if len(parts) >= 5:
                                page_data["Banco"] = parts[0]
                                page_data["Agência"] = parts[1]
                                page_data["Conta Judicial"] = parts[2]
                                page_data["Data do Depósito"] = parts[3]
                                page_data["Valor do Depósito"] = parts[4]

                    elif "OBS.:" in line:
                        page_data["OBS.:"] = line.replace("OBS.: ", "")
                            



                            
                data.append(page_data)

        return data

def save_to_text(result_data, output_path):
    with open(output_path, "w", encoding="utf-8") as f:
        for page_data in result_data:
            f.write(f"Página {page_data['Página']}:\n")
            f.write("---------------------------------------\n")
            for key, value in page_data.items():
                f.write(f"{key}: {value}\n")
            f.write("---------------------------------------\n\n")

def save_to_excel(result_data, output_path):
    df = pd.DataFrame(result_data)
    df.to_excel(output_path, index=False)

pdf_path = "C:/Users/pooul/Downloads/pastaTeste/robo02.pdf"
result_data = extract_information(pdf_path)

txt_path = "output.txt"
excel_path = "output.xlsx"

save_to_text(result_data, txt_path)
save_to_excel(result_data, excel_path)

print(f"Os dados foram exportados para os arquivos: {txt_path} e {excel_path}")
