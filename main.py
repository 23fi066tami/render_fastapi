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
            <p>好きなようにHTMLを書き換えてOK！</p>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)
