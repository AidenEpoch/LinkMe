from fastapi import *
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
app = FastAPI()

@app.get("/")
async def index():
    return FileResponse("./static/index.html", media_type="text/html")


app.mount(
    "/static",
    StaticFiles(directory= "static"),
)