import uvicorn

from app.main import app


def run() -> None:
    uvicorn.run(app, host="0.0.0.0", port=8000)  # nosec


if __name__ == "__main__":
    run()
