from fastapi import FastAPI
import uvicorn

from app.endpoints import routes


def bind_routes(app: FastAPI):
    path_prefix = "/api_v1.0"
    for router in routes:
        app.include_router(router, prefix=path_prefix)


news = FastAPI(title="First project")


bind_routes(news)


if __name__ == "__main__":
    uvicorn.run(news, port=8000)