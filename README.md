📤 Bot de Cobrança Automática via WhatsApp

Automatize o envio de mensagens de cobrança para seus clientes usando Python, Selenium e uma planilha Excel.
Ideal para pequenos negócios, freelancers e qualquer pessoa que precisa enviar lembretes de pagamento de forma simples, rápida e 100% automática.

🚀 Funcionalidades

✔️ Envia mensagens personalizadas via WhatsApp Web

✔️ Lê automaticamente uma planilha Excel com nome, telefone e status

✔️ Permite editar a mensagem para cada cliente

✔️ Evita envio duplicado

✔️ Sistema fácil de usar, mesmo para iniciantes

✔️ Código leve e organizado

🔧 Tecnologias usadas

Python 3

Selenium WebDriver

Pandas

ChromeDriver

Excel (.xlsx)

📁 Estrutura do projeto
cobranca-bot/
│── sistema_cobranca.py      # Código principal
│── clientes_cobranca.xlsx   # Planilha com contatos
│── PyWhatKit_DB.txt         # Arquivo auxiliar
│── venv/                    # Ambiente virtual (ignorado no Git)
│── README.md                # Este arquivo

📝 Como usar
1️⃣ Instalar dependências

Ative seu ambiente virtual:

source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows


Instale os pacotes:

pip install -r requirements.txt

2️⃣ Prepare a planilha Excel

Sua planilha deve seguir este formato:

Nome	Telefone	Status
João	11999998888	Pendente
Maria	21988887777	Pago

O telefone deve estar no formato: DDD + número, sem +55.

3️⃣ Execute o bot
python sistema_cobranca.py


O WhatsApp Web abrirá automaticamente. Escaneie o QR Code e o robô fará o resto.

⚠️ Avisos importantes

O WhatsApp bloqueia automações agressivas — este bot envia de forma segura.

Apenas use para mensagens autorizadas por seus clientes.

O envio depende do WhatsApp Web estar conectado.

📌 Próximos passos (opcionais)

Gerar executável .exe para vender

Criar interface gráfica (GUI)

Adicionar logs e relatórios

Integrar com Google Sheets

Posso te ajudar a fazer tudo isso também! 😁

💬 Contato

Se você quiser suporte, melhorias ou versão comercial, fale comigo!
