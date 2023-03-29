from hashlib import sha256


class AuthenticException(Exception):
    pass


class IncorrectPassword(AuthenticException):
    pass


class IncorrectUsername(AuthenticException):
    pass


class NotLoggedError(AuthenticException):
    pass


class PasswordTooShort(AuthenticException):
    pass


class UsernameAlreadyExists(AuthenticException):
    pass


class NotPermittedError(AuthenticException):
    pass


class PermissionError(Exception):
    pass


class User:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = self._encrypt_password(username, password)
        self.is_logged = False

    def _encrypt_password(self, username: str, password: str) -> str:
        hashed = sha256(username.encode("utf-8") + password.encode("utf-8")).hexdigest()
        return hashed
    
    def check_password(self, password):
        return sha256(self.username.encode("utf-8") + password.encode("utf-8")).hexdigest() == self.password
        

class Authenticator:
    def __init__(self):
        self.users = {"ADMIN":User("ADMIN", "admin123")}

    def add_user(self, username, password):
        
        if username in list(self.users.keys()):
            raise UsernameAlreadyExists
        
        if len(password) < 7:
            raise PasswordTooShort
        
        self.users[username] = User(username, password)
        
    def login(self, username, password):
        if username not in list(self.users.keys()):
            raise IncorrectUsername

        if not self.users[username].check_password(password):
            raise IncorrectPassword
        
        self.users[username].is_logged = True

    def is_logged(self, username):
        return self.users[username].is_logged
    

class Authorizor:
    
    def __init__(self):
        self.permissions = {"admin":["ADMIN"]}
        self.authenticator = Authenticator()

    def add_permission(self, permission):
        if permission in list(self.permissions.keys()):
            raise PermissionError
        self.permissions[permission] = []
        
    def permit_user(self, username, permission):
        if username not in self.authenticator.users.keys():
            raise IncorrectUsername
        if permission not in list(self.permissions.keys()):
            raise PermissionError
        
        self.permissions[permission].append(username)

    def check_permission(self, username, permission):
        if not self.authenticator.users[username].is_logged:
            raise NotLoggedError
        
        if permission not in list(self.permissions.keys()):
            raise PermissionError
        
        if username not in self.permissions[permission]:
            raise NotPermittedError
        
    
class Editor:
    
    def __init__(self):
        self.username = None
        self.options = {"a":self.login, "b":self.test, "c":self.change, "d":self.quit}

    def login(self, authorizor):
        try:
            login_ = input("Enter a login: ")
            password_ = input("Enter a password: ")
            authorizor.authenticator.login(login_, password_)
            self.username = login_
        except IncorrectUsername:
            print("This user doesn't exist.")
        except IncorrectPassword:
            print("Incorrect password. Try again.")

    def is_permitted(self, authorizor, perm):
        try:
            if self.username is None:
                raise NotLoggedError
            authorizor.check_permission(self.username, perm)
            print(f"You have {perm} permission(s)")
            return True

        except NotLoggedError:
            print("You are not logged into any account.")
            return False
        except PermissionError:
            print(f"There is no permission named {perm}.")
            return False
        except NotPermittedError:
            print("You don't have that permission.")
            return False

        
    def test(self, authorizor):
        perm = input("Input the name of the permission you want to test\n> ")
        self.is_permitted(authorizor, perm)

    def change(self, authorizor):
        choice = input("What do you want to do?\n1. Add a new permission.\n2. Grant a permission to a user\n3. Add a new user\n\n> ")
        match(choice):
            case "1":
                try:
                    if self.is_permitted(authorizor, "admin"):
                        perm = input("Input the name of the permission you want to add\n> ")
                        authorizor.add_permission(perm)
                except PermissionError:
                    print("This permission already exists.")
            case "2":
                try:
                    if self.is_permitted(authorizor, "admin"):
                        perm = input("Input the name of the permission you want to grant\n> ")
                        user = input("Input the name of the user you want to give permission to\n> ")
                        authorizor.permit_user(user, perm)
                except PermissionError:
                    print(f"There is no permission named {perm}")
                except IncorrectUsername:
                    print(f"There is no user named {user}")
            case "3":
                try:
                    if self.is_permitted(authorizor, "admin"):
                        user = input("Input the name of the user you want to add\n> ")
                        password = input("Input the password for the new user\n> ")
                        authorizor.authenticator.add_user(user, password)
                except UsernameAlreadyExists:
                    print("This user already exists")
                except PasswordTooShort:
                    print("The password is too short (min. 7 characters)")
            case _:
                print("Unknown command.")


    def quit(self, authorizor):
        exit()

    def run(self, authorizor):
        while True:
            try:
                print("Available options\na. login\nb. test\nc. change\nd. quit")
                choice = input("------------\nChoose\n> ")
                self.options[choice](authorizor)
            except KeyError:
                print("There is no such option.\n\n")


if __name__ == "__main__":
    auth = Authorizor()
    editor = Editor()
    editor.run(auth)