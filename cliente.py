import requests

BASE_URL = 'http://localhost:5000'

def registrar():
    usuario = input("Usuario: ")
    contrasena = input("Contraseña: ")
    r = requests.post(f'{BASE_URL}/registro', json={"usuario": usuario, "contraseña": contrasena})
    print(r.json())

def login():
    usuario = input("Usuario: ")
    contrasena = input("Contraseña: ")
    r = requests.post(f'{BASE_URL}/login', json={"usuario": usuario, "contraseña": contrasena})
    print(r.json())

def ver_tareas():
    r = requests.get(f'{BASE_URL}/tareas')
    print(r.text)

if __name__ == "__main__":
    while True:
        print("\n1. Registrarse\n2. Login\n3. Ver tareas\n4. Salir")
        op = input("Opción: ")
        if op == '1':
            registrar()
        elif op == '2':
            login()
        elif op == '3':
            ver_tareas()
        else:
            break