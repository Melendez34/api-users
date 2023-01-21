from models.user import UserTableModel
from schemas.user_schema import User


class UserService:
    def __init__(self, db) -> None:
        """User Service"""
        self.db = db

    def get_users(self):
        result = self.db.query(UserTableModel).all()
        return result

    def get_user(self, id):
        result = self.db.query(UserTableModel).filter(UserTableModel.id == id).first()
        return result

    def get_user_by_username(self, username):
        result = (
            self.db.query(UserTableModel)
            .filter(UserTableModel.username == username)
            .all()
        )
        return result

    def create_user(self, user: User):
        new_user = UserTableModel(**user.dict())
        self.db.add(new_user)
        self.db.commit()
        return

    def put_user(self, id: int, data: User):
        user = self.db.query(UserTableModel).filter(UserTableModel.id == id).first()
        user.name = data.name
        user.username = data.username
        user.email = data.email
        user.im = data.im
        user.password = data.password
        self.db.commit()
        return

    def delete_user(self, id: int):
        self.db.query(UserTableModel).filter(UserTableModel.id == id).delete()
        self.db.commit()
        return
