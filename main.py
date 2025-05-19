from users import Users as user

def main_menu():
    while True:
        print("\n🔸 MENÚ PRINCIPAL 🔸")
        print("1. Registrar nuevo usuario")
        print("2. Ver todos los usuarios")
        print("3. Eliminar usuario por ID")
        print("4. Buscar usuario por email")
        print("5. Salir")

        option = input("Elegí una opción (1-4): ").strip()

        if option == "1":
            name = input("Nombre (solo nombre, el apellido se pide despues): ").strip()
            last_name = input("Apellido: ").strip()
            email = input("Email: ").strip()
            password = input("Contraseña: ").strip()

            user.user_registration(name, last_name, email, password)

        elif option == "2":
            print(user.list_users())

        elif option == "3":
            id = input("Ingrese el user id, si no lo sabe puede volver al menu anterior escribiendo 'VOLVER' y consultar la opcion dos: ").strip()
            if id == 'VOLVER':
                continue

            else:
                user.delete_user(user_id=id)
        
        elif option == "4":
            user_email = input("Ingrese email: ").strip()
            u = user.search_user(email=user_email)

            if u is None:
                print("Usuario no encontrado")

            else:
                print(u)

        elif option == "5":
            print("¡Hasta luego!")
            break

        else:
            print("Opción inválida. Intentá de nuevo.")


if __name__ == "__main__":
    main_menu()