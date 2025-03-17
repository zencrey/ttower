from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Jinja Templates
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "title": "FastAPI Website"})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
