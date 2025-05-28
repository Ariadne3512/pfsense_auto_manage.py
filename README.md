# pfsense_auto_manage.py

📘 Documentação Técnica
Automação de Adição de Máquina e Remoção de IPs Bloqueados no pfSense

## 📌 Visão Geral
Este script em Python 3 realiza a automação de duas tarefas principais no firewall pfSense utilizando sua API RESTful:

Adição de uma nova máquina (IP + hostname) ao alias "trusted_hosts".

Remoção de IPs bloqueados detectados nos logs de firewall.

Aplicação automática das configurações.

## 🏗️ Estrutura do Projeto

bash
Copy
Edit

pfsense_auto_manage/

│

├── pfsense_auto_manage.py   # Script principal

├── README.md                # Instruções básicas

└── requirements.txt         # Dependências do projeto
📥 Requisitos
Python 3.6+

Biblioteca Requests

pfSense com API ativa

Recomendado: pfSense API não oficial

## 📦 Instalação
Clone o repositório (opcional):

bash

Copy

Edit

git clone https://github.com/seuusuario/pfsense_auto_manage.git

cd pfsense_auto_manage

Instale as dependências:

bash

Copy

Edit

pip install -r requirements.txt

Conteúdo do requirements.txt:

nginx
Copy
Edit
requests
⚙️ Configuração
Abra o arquivo pfsense_auto_manage.py e configure as variáveis:

python

Copy

Edit

PFSENSE_HOST = "https://192.168.1.1"

API_TOKEN = "seu_token_aqui"

VERIFY_SSL = False  # use True em produção

##🚀 Como Usar
Execute o script com:

bash

Copy

Edit

python3 pfsense_auto_manage.py


Funcionalidades:

✅ Adiciona nova máquina ao alias "trusted_hosts".

❌ Remove IPs com status "blocked" do alias "blocked_ips".

🔄 Aplica configurações imediatamente.

## 🔍 Explicação das Funções

Função	Descrição

adicionar_maquina()	Adiciona IP/hostname ao alias

listar_bloqueios()	Lê os logs do firewall e retorna IPs bloqueados

remover_bloqueio()	Remove IP de um alias de bloqueio

aplicar_configuracoes()	Aplica as mudanças no pfSense

🔐 Segurança

Use HTTPS com certificado válido (defina VERIFY_SSL=True).

Não exponha o token da API.

Execute o script em ambiente seguro e controlado.

🛠️ Possíveis Extensões Futuras

Interface gráfica (Tkinter/WxPython)

Logs detalhados (arquivo .log)

Integração com sistema de tickets (Zabbix, GLPI)

Agendamento via cron (Linux) ou Agendador de Tarefas (Windows)

Classificação dos IPs bloqueados antes da remoção

❓ Suporte
Caso você enfrente problemas ou deseje adicionar recursos, sinta-se à vontade para abrir uma issue no repositório ou entrar em contato com o administrador do sistema.
