from fastapi import FastAPI
from api.routes import companies, posts, users

app = FastAPI()

app.include_router(users.router)
app.include_router(posts.router)
app.include_router(companies.router)


@app.get("/")
def read_root():
    return dict(msg="Hello World")
