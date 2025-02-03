class Create_User:

    created_users = []

    def __init__(self, name, lastname, age, email, password):
        self.name = name
        self.lastname = lastname
        self.age = age
        self.email = email
        self.password = password

        for user in Create_User.created_users:
            if user["email"] == self.email:
                raise ValueError("This email is already associated with an account.")
            
        Create_User.created_users.append({"name": self.name, "lastname": self.lastname, "age": self.age, "email": self.email, "password": self.password })
        print(f"Registered users: {Create_User.created_users}")

    @classmethod
    def login_users(cls, email, password):
        for user in cls.created_users:
            if user["email"] == email and user["password"] == password:
                return True 
        raise ValueError("Incorrect email or password.")
