from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from chatgpt import send_message

app = FastAPI(title="Madliani API")


@app.get("/{value}", response_class=HTMLResponse)
async def root(value: str):
    response = await send_message(value)
    return (f"<html><body>"
            f"\n{response}\n"
            f"</body></html>")
