from fastapi import FastAPI

from app import __version__

app = FastAPI(version=__version__)


@app.get("/")
def read_root() -> dict[str, str]:
    return {"msg": "Hello World"}
