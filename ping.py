import ping3

def check_host(hostname):
    response = ping3.ping(hostname)
    if response is None or response == False:
        print(f"{hostname} no está en línea.",response)
    else:
        print(f"{hostname} está en línea.",response)
        
        

# Ejemplo de uso
hostname = "192.168.50.150"  # Reemplaza con la dirección IP de la PC que quieres verificar
hostname1 = "192.168.50.1"
hostname2 = "192.168.50.151"

check_host(hostname)

check_host(hostname1)

check_host(hostname2)