import sqlite3
from fastapi import FastAPI, Request, HTTPException
import json
import random
from pathlib import Path


app = FastAPI()
DATABASE_PATH = "dare.db"
path = Path(DATABASE_PATH)


@app.get("/")
async def home():

    return {"message": "welcome to drunk dares"}


# Endpoint that gets all existing dares
@app.get("/drunk/dares/")
async def dares():
    connection = sqlite3.connect("dares.db")
    cursor = connection.cursor()
    select_query = "SELECT * FROM dares"
    all_dares_list = cursor.execute(select_query).fetchall()  # A list
    if len(all_dares_list) == 0:
        #  Raise status code 404 if nothing in database
        raise HTTPException(status_code=404, detail="There is nothing in the database")
    dares_dict = {item[0]: item[1] for item in all_dares_list}
    connection.close()

    return json.dumps(dares_dict)  # Serialize the returned Python Dictionary


@app.get("/drunk/random_dare/")
async def random_dare():
    connection = sqlite3.connect("dares.db")
    cursor = connection.cursor()
    select_query = "SELECT * FROM dares"
    all_dares_list = cursor.execute(select_query).fetchall()  # A list
    if len(all_dares_list) == 0:
        #  Raise status code 404 if nothing in database
        raise HTTPException(status_code=404, detail="There is nothing in the database")
    dares_dict = {item[0]: item[1] for item in all_dares_list}

    connection.close()
    # random questions --> need to implement an algorithm for
    return json.dumps(random.choice(list(dares_dict.values())))  # Serialize the returned Value


@app.post("/drunk/dares/")
async def create_dare(request: Request):
    data = await request.json()

    connection = sqlite3.connect("dares.db")
    cursor = connection.cursor()
    check_exist_query = "SELECT dares FROM dares WHERE EXISTS (SELECT dares FROM dares WHERE dares = (?))"
    dares_equal = cursor.execute(check_exist_query, (data["dares"],)).fetchall()
    if len(dares_equal) > 0:
        # 406 not acceptable
        raise HTTPException(status_code=406, detail="Dare with the same content already exist")
    else:
        create_query = "INSERT INTO dares VALUES (NULL,?)"
        cursor.execute(create_query, (data["dares"],))
    connection.commit()
    connection.close()

    return data


@app.put("/drunk/dare")
async def update_dare(request: Request):
    data = await request.json()
    connection = sqlite3.connect("dares.db")
    cursor = connection.cursor()
    check_exist_query = "SELECT dares FROM dares WHERE EXISTS (SELECT dares FROM dares WHERE dare_id = (?))"
    dares_equal = cursor.execute(check_exist_query, (data["dare_id"],)).fetchall()
    if len(dares_equal) == 0:
        raise HTTPException(status_code=406, detail="Dare with the id doesn't exist")
    else:
        update_query = "UPDATE dares SET dares=(?) where dare_id=(?)"
        cursor.execute(update_query, (data["dares"], data["dare_id"]))
    connection.commit()
    connection.close()
    return data



@app.delete("/drunk/dares/")
async def delete_dare(request: Request):
    data = await request.json()
    connection = sqlite3.connect("dares.db")
    cursor = connection.cursor()
    delete_query = "DELETE FROM dares WHERE dare_id=(?)"
    # No need to handle error, simply delete everything that is mentioned even if the id doesn't exist
    cursor.execute(delete_query, (data["dare_id"],))
    connection.commit()
    connection.close()
    return {"Success": "The data is being deleted"}



