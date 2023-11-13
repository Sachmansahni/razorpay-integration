from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import razorpay

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def app_create():
    return templates.TemplateResponse("app.html", {"request": None})

@app.post("/pay", response_class=HTMLResponse)
async def pay(username: str = Form(...)):
    global payment, name
    name = username
    client = razorpay.Client(auth=("YOUR_ID", "YOUR_SECRET"))

    data = {"amount": 500, "currency": "INR", "receipt": "order_rcptid_11"}
    payment = client.order.create(data=data)
    return templates.TemplateResponse("pay.html", {"request": None, "payment": payment})

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
