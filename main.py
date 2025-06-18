from fastapi import FastAPI
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
async def give_present(present):
    return {"response": f"サーバです。課題をしなさい！ {present}うるさい。"}  # f文字列というPythonの機能を使っている
