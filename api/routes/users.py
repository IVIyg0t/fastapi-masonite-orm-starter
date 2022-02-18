from typing import Optional
from fastapi import APIRouter
from models.User import User

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/")
def get_users():
    return User.all().serialize()


@router.post("/")
def create_user(
    firstname: str,
    lastname: str,
    username: str,
    email: str,
    password: str,
):
    user = User.create(
        firstname=firstname,
        lastname=lastname,
        username=username,
        email=email,
        password=password,
    )

    return user.id


@router.put("/{id}")
def update_user(
    id: int,
    firstname: Optional[str] = None,
    lastname: Optional[str] = None,
    username: Optional[str] = None,
    email: Optional[str] = None,
):
    user = User.find(id)

    user.firstname = firstname or user.firstname
    user.lastname = lastname or user.lastname
    user.username = username or user.username
    user.email = email or user.email

    user.save()

    return user.serialize()


@router.get("/{id}")
def get_user(id: int):
    return User.find(id).serialize()


@router.get("/{id}/posts")
def get_user_posts(id: int):
    return User.find(id).posts.serialize()
