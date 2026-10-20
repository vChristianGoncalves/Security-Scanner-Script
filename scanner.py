import datetime
import socket
import sys
from urllib.request import Request, urlopen


def banner():
    print("=" * 60)
    print("   ESCANER DE SEGURIDAD Y PUERTOS - PYTHON JUNIOR")
    print("=" * 60)


def scan_ports(host, ports):
    print(f"\n[*] Iniciando escaneo de puertos en: {host}")
    print(f"[*] Hora de inicio: {str(datetime.datetime.now())}\n")

    try:
        target_ip = socket.gethostbyname(host)
        print(f"[*] IP resuelta: {target_ip}\n")
    except socket.gaierror:
        print("[-] Error: No se pudo resolver el nombre de host.")
        return

    open_ports = []
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1.0)  # Tiempo de espera por puerto (1 segundo)

        result = s.connect_ex((target_ip, port))
        if result == 0:
            print(f"[+] Puerto {port}: ABIERTO")
            open_ports.append(port)
        s.close()

    if not open_ports:
        print("[-] No se encontraron puertos abiertos en el rango evaluado.")


def analyze_http_headers(url):
    print(f"\n[*] Analizando cabeceras de seguridad HTTP en: {url}\n")

    # Cabeceras de seguridad recomendadas por OWASP
    security_headers = [
        "Strict-Transport-Security",
        "Content-Security-Policy",
        "X-Frame-Options",
        "X-Content-Type-Options",
        "Referrer-Policy",
    ]

    try:
        req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
        response = urlopen(req)
        headers = response.info()

        print("[+] Cabeceras encontradas:")
        for header, value in headers.items():
            print(f"    - {header}: {value}")

        print("\n[*] Evaluacion de cabeceras de seguridad (OWASP):")
        for header in security_headers:
            if header in headers:
                print(f"    [OK] {header} esta presente.")
            else:
                print(
                    f"    [ALERTA] {header} NO esta presente (Posible riesgo de seguridad)."
                )

    except Exception as e:
        print(f"[-] Error al realizar la peticion HTTP: {e}")


if __name__ == "__main__":
    banner()

    # Define el objetivo (Usa 'scanme.nmap.org' o 'localhost' para pruebas seguras)
    target_host = input(
        "Ingresa el dominio o IP a escanear (Ej: scanme.nmap.org): "
    ).strip()

    if not target_host:
        target_host = "scanme.nmap.org"  # Objetivo de prueba oficial de Nmap

    # Puertos comunes a evaluar
    common_ports = [21, 22, 80, 443, 8080, 3306]

    # Ejecucion de escaneo
    scan_ports(target_host, common_ports)

    # Analisis HTTP si aplica
    target_url = f"https://{target_host}"
    analyze_http_headers(target_url)