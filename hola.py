import tkinter as tk
from tkinter import messagebox
import re
import ping3



def validate_ip(ip):
    # Expresión regular para validar una dirección IPv4
    ip_pattern = r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"
    if re.match(ip_pattern, ip):
        return True
    else:
        return False

def check_host():
    hostname = entry_ip.get()
    #hostname = "192.168.50.151"
    if validate_ip(hostname):
        response = ping3.ping(hostname)
        #response = os.system("ping -c 1 " + str(hostname))
        print(response)
        if response is None or response == False:
            messagebox.showerror("Estado", f"{hostname} no está en línea.")
        else:
            messagebox.showinfo("Estado", f"{hostname} está en línea.")
    else:
        messagebox.showerror("Error", "Por favor, ingresa una dirección IP válida.")

    

# Crear la ventana principal
root = tk.Tk()
root.title("Verificar Conectividad")

# Crear y posicionar los elementos de la interfaz gráfica
label_ip = tk.Label(root, text="Dirección IP:")
label_ip.pack()


entry_ip = tk.Entry(root)
entry_ip.pack()




button_check = tk.Button(root, text="Verificar", command=check_host)
button_check.pack()

# Ejecutar el bucle principal de la aplicación
root.mainloop()
