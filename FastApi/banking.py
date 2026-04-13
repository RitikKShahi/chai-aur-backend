from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app=FastAPI()

class Account(BaseModel):
    id: int
    AccountNo: int
    Balance: int
    DOB: str
    Type: str

accounts: List[Account]=[]

@app.get("/")
def root():
    return {"Greeting":"Welcome to the transaction department"}

@app.get("/accounts")
def path():
    return accounts

@app.get("/account/{uuid}")
def privacy(uuid:int):
    for index,acc in enumerate(accounts):
        if uuid==acc.id:
            return acc
    return {"error":"This account does'nt exist"}

@app.post("/accounts")
def add_account(acc:Account):
    accounts.append(acc)
