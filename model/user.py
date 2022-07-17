class User:
    def __init__(self, username,  first_name, last_name, role):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.role = role

    def to_dict(self):
        return{
            "username": self.username,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "role": self.role
        }
