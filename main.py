from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/index")
def index():
    html_content = """
    <html>
        <head>
            <title>My Web Page</title>
        </head>
        <body>
            <h1>こんにちは！これは私のWebページです！</h1>
            <p>よく分からないけどうまくいった</p>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

@app.post("/present")
async def give_present(present: str = Form(...)):
    return {"response": f"メリークリスマス！{present}ありがとう！お返しはケーキです。"}
