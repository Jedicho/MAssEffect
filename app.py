from fastapi import FastAPI
from starlette.responses import FileResponse


html_path="./assets/html/index.html"
css_path="./assets/html/style.css"
app = FastAPI()


@app.get('/', response_class=FileResponse)
async def read_root() :
    return FileResponse(html_path)

@app.get("/index_css", response_class=FileResponse)
async def read_css():
    return FileResponse(css_path)

