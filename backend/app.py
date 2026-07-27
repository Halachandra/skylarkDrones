from fastapi import FastAPI

from monday import get_deals
from monday import get_work_orders
from analyzer import dashboard
from llm import generate_answer
from models import ChatRequest
from router import detect_intent
from tools import execute_tool
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173","https://skylark-drones-brxv.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/deals")

def deals():

    df = get_deals()

    return df.to_dict(orient="records")

@app.get("/workorders")

def workorders():

    df = get_work_orders()

    return df.to_dict(orient="records")

@app.get("/test-clean")
def test_clean():

    df = get_deals()

    return {
        "rows": len(df),
        "columns": list(df.columns),
        "nulls": df.isna().sum().to_dict()
    }

@app.get("/dashboard")
def dashboard_data():

    deals = get_deals()

    workorders = get_work_orders()

    return dashboard(deals, workorders)

@app.get("/columns-workorders")
def columns_workorders():
    df = get_work_orders()
    return list(df.columns)

@app.post("/chat")
def chat(request: ChatRequest):

    deals = get_deals()
    workorders = get_work_orders()

    # Complete business data
    full_dashboard = dashboard(deals, workorders)

    # Detect intent
    intent = detect_intent(request.question)

    # Tool output (optional)
    tool_data = execute_tool(
        intent,
        deals,
        workorders
    )

    # Send both
    context = {
        "dashboard": full_dashboard,
        "tool_result": tool_data
    }

    answer = generate_answer(
        request.question,
        context
    )

    return {
        "intent": intent,
        "answer": answer
    }

