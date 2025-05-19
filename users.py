from utils import utils

class Users:

    def user_registration(name: str, last_name: str, email: str, password: str):
        try:
            data = utils.read_json_file()

            if any(user.get("email") == email for user in data):
                print("Ya existe un usuario registrado con ese email.")
                return

            user_id = 1 if not data else data[-1].get("id", 0) + 1

            new_user = {
                "id": user_id,
                "name": name,
                "last_name": last_name,
                "email": email,
                "password": password  
            }

            utils.write_json_file(new_user, from_scratch=False)

            print(f"Usuario '{name}' registrado exitosamente con ID {user_id}.")

        except Exception as e:
            print(f'Ocurrió un error en el registro: {e}')


    def list_users():
        data = utils.read_json_file()
        return data

    def delete_user(user_id: int):
        data = utils.read_json_file()  
        index = next((i for i, user in enumerate(data) if user.get("id") == user_id), None)

        if index is not None:
            data.pop(index)
            utils.write_json_file(data=data, from_scratch=True)
            print(f"Usuario con id {user_id} eliminado.")
        
        else:
            print(f"No se encontró usuario con id {user_id}.")

    def update_user(id: int):
        pass

    def search_user(email: str):
        data = utils.read_json_file()
        user_searched = None

        for user in data:
            if user.get('email') == email:
                user_searched = user
                break

        return user_searched


