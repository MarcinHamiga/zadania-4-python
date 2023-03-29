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
        hashed = sha256(username+password)
        return hashed
    
    def check_password(self, password):
        hashed = sha256(self.username + password)
        if hashed == self.password:
            return True
        else:
            return False
        

class Authenticator:
    def __init__(self):
        self.users = {}

    def add_user(self):
        
        username = input("Enter a login for the new user\n> ")
        if username in self.users.keys:
            raise UsernameAlreadyExists
        
        password = input("Enter a password for the new user: ")
        if len(password) < 7:
            raise PasswordTooShort
        
        self.users[username] = User(username, password)
        
    def login(self, username, password):
        if username not in self.users.keys:
            raise IncorrectUsername

        password = input("Password: ")
        if self.users[username].check_password(password):
            return True

    def is_logged(self, username):
        return self.users[username].is_logged
    

class Authorizor:
    
    def __init__(self):
        self.permissions = {}
        self.authenticator = Authenticator()

    def add_permission(self, permission):
        if permission in self.permissions.keys:
            raise PermissionError
        self.permissions[permission] = []
        
    def permit_user(self, username, permission):
        if username not in self.authenticator.users.keys:
            raise IncorrectUsername
        if permission not in self.permissions.keys:
            raise PermissionError
        
        self.permissions[permission].append(username)

    def check_permission(self, username, permission):
        if not self.authenticator.users[username].is_logged:
            raise NotLoggedError
        
        if permission not in self.permissions.keys:
            raise PermissionError
        
        if username not in self.permissions[permission]:
            raise NotPermittedError
        
    
class Editor:
    
    def __init__(self):
        self.username = None
        self.options = {"a":self.login, "b":self.test, "c":self.change, "d":self.quit}

    def login(self, authenticator):
        login_ = authenticator.
        

