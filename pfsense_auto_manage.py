import requests

# Configurações
PFSENSE_HOST = "https://192.168.1.1"
API_TOKEN = "seu_token_aqui"  # ou user/password
VERIFY_SSL = False  # cuidado com certificados inválidos

# Cabeçalhos de autenticação
HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}

# 1. Adicionar nova máquina
def adicionar_maquina(ip, hostname):
    url = f"{PFSENSE_HOST}/api/v1/firewall/alias"
    payload = {
        "name": "trusted_hosts",
        "type": "host",
        "address": ip,
        "description": hostname
    }
    response = requests.post(url, headers=HEADERS, json=payload, verify=VERIFY_SSL)
    print(f"[+] Adição: {response.status_code} - {response.text}")

# 2. Listar IPs bloqueados
def listar_bloqueios():
    url = f"{PFSENSE_HOST}/api/v1/log/firewall"
    response = requests.get(url, headers=HEADERS, verify=VERIFY_SSL)
    logs = response.json().get("data", [])
    bloqueados = [log["src_ip"] for log in logs if "block" in log["action"]]
    return list(set(bloqueados))  # IPs únicos

# 3. Remover IPs bloqueados (exemplo via alias)
def remover_bloqueio(ip):
    url = f"{PFSENSE_HOST}/api/v1/firewall/alias"
    # Aqui estamos simulando a remoção via exclusão do alias
    # Em casos reais, pode ser necessário editar ou excluir a regra
    payload = {
        "name": "blocked_ips",
        "address": ip
    }
    response = requests.delete(url, headers=HEADERS, json=payload, verify=VERIFY_SSL)
    print(f"[-] Remoção: {ip} - {response.status_code}")

# 4. Aplicar alterações
def aplicar_configuracoes():
    url = f"{PFSENSE_HOST}/api/v1/system/apply"
    response = requests.post(url, headers=HEADERS, verify=VERIFY_SSL)
    print(f"[✓] Aplicar: {response.status_code} - {response.text}")

# Execução principal
if __name__ == "__main__":
    nova_maquina_ip = "192.168.1.50"
    nova_maquina_nome = "servidor-web"

    adicionar_maquina(nova_maquina_ip, nova_maquina_nome)

    bloqueados = listar_bloqueios()
    print(f"IPs bloqueados encontrados: {bloqueados}")

    for ip in bloqueados:
        remover_bloqueio(ip)

    aplicar_configuracoes()
