
from faker import Faker

from models.user import User

fake = Faker()

def create_user(name =None, last_name=None, email=None, password=None):
    return User(
        name if name is not None else fake.name(),
        last_name if last_name is not None else fake.last_name(),
        email if email is not None else fake.email(),
        password if password is not None else fake.password(
            length=10,special_chars=True,digits=True,upper_case=True,lower_case=True
        )
    )

def existing_user():
    return create_user(
        name = "Chuchu",
        last_name = "Yoyo",
        email = "yakubdmitriy@gmail.com",
        password = "Yakub123*"
    )