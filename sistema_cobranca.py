import pandas as pd
import pywhatkit
import time
import pyautogui

print("Iniciando o robô...")
print("IMPORTANTE: Abra o WhatsApp Web manualmente e deixe a aba parada.")

# 1. Carregar a planilha
try:
    tabela = pd.read_excel("clientes_cobranca_atualizado.xlsx")
except FileNotFoundError:
    print("Erro: Arquivo da planilha não encontrado!")
    exit()


# 2. Processar envios
for i, linha in tabela.iterrows():
    if linha["Status"] == "Pendente":
        nome = linha["Nome"]
        valor = linha["Valor"]
        
        telefone = str(linha["Telefone"]) 
        if telefone.endswith(".0"):
            telefone = telefone.replace(".0", "")
        if not telefone.startswith("+"):
            telefone = "+" + telefone

        mensagem = f"Olá {nome}, tudo bem? Lembrete amigável: sua fatura de R$ {valor} venceu. Se já pagou, desconsidere."

        print(f"Enviando para {nome} no número {telefone}...")

        try:
            # NÃO FECHAR A ABA — ESSENCIAL
            pywhatkit.sendwhatmsg_instantly(
                phone_no=telefone,
                message=mensagem,
                wait_time=12,  # tempo mais rápido mas estável
                tab_close=False
            )

            # dar ENTER para garantir envio
            time.sleep(2)
            pyautogui.press("enter")

            # Atualizar status
            tabela.loc[i, "Status"] = "Enviado"
            print("Mensagem enviada!")

            # pausa mínima entre envios
            time.sleep(4)

        except Exception as e:
            print(f"Falha ao enviar para {nome}: {e}")
            tabela.loc[i, "Status"] = "Erro"

# 3. Salvar relatório
tabela.to_excel("clientes_cobranca_atualizado.xlsx", index=False)
print("Fim do processo. Planilha atualizada salva.")
