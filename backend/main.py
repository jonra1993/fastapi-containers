import struct, random, string
from typing import Optional
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.sql import text
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
engine = create_engine('postgresql://unicorn_user:magical_password@postgres_container/testDB')

class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None


@app.get("/", status_code=200)
def read_root():
    r = random.randint(0, 10)
    try:
        with engine.connect() as con:
            rs = con.execute('SELECT *, point(-85.3078294, 35.0609500) <@> point(longitude, latitude)::point as distance FROM location WHERE (point(-85.3078294, 35.0609500) <@> point(longitude, latitude)) < 10 ORDER BY distance')
            my_list = []
            str1 = " "
            for row in rs:
                print(row)
                my_list.append(str(row))
                
            return {str1.join(my_list)}
    except:
        return {"Hello": "World" + str(r)}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}
