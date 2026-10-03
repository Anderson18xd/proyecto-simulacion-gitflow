def login(user, password):
    if not password:
        print("Error: La contraseña es requerida")
        return False
    print(f"Iniciando sesión para: {user}")
    return True