class User:

    users = []

    def __init__(self, name, lastname, age, email, password):
        self.name = name
        self.lastname = lastname
        self.age = age
        self.email = email
        self.password = password

        for user in User.users:
            if user["email"] == self.email:
                raise ValueError("This email is already associated with an account.")
            
        User.users.append({"name": self.name, "lastname": self.lastname, "age": self.age, "email": self.email, "password": self.password })
        print(f"Registered users: {User.users}")

    @classmethod
    def login_user(cls, email, password):
        for user in cls.users:
            if user["email"] == email and user["password"] == password:
                return True 
        raise ValueError("Incorrect email or password.")
