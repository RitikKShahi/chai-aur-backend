from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app= FastAPI()

class Pokemon(BaseModel):
    id: int
    name: str
    type: str

deck: List[Pokemon]=[]

@app.get("/")
def read_root():
    return {"message":"Welcome to Santos City"}

@app.get("/deck")
def get_deck():
    return deck

@app.post("/deck")
def add_pokemon(pokemon: Pokemon):
    deck.append(pokemon)
    return pokemon

@app.put("/deck/{mon_id}")
def edit_pokemon(mon_id:int,pokemon: Pokemon):
    for index,poke in enumerate(deck):
        if mon_id==poke.id:
            pokemon.id = mon_id
            deck[index]=pokemon
            return pokemon
    return {"error":"You ran into an issue"}

@app.delete("/deck/{mon_id}")
def delete_pokemon(mon_id:int):
    for index,pokemon in enumerate(deck):
        if pokemon.id==mon_id:
            deck.pop(index)
            return pokemon
    return {"error":"You ran into an issue"}
