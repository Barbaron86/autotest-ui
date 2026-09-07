from pydantic import BaseModel


class User(BaseModel):
    id: int
    username: str
    email: str
    is_active: bool = True


user_data = {"id": 1, "username": "user", "email": "test@gmail.com", "is_active": True}
invalid_user_data = {"id": "one", "username": "user", "email": "test@mail.com", "is_active": "true"}

user = User(**user_data)
print(user)
print(user.is_active)
try:
    invalid_user = User(**invalid_user_data)
except Exception as error:
    print("Ошибка валидации", error)
