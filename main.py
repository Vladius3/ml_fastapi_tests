rom fastapi import FastAPI

from transformers import pipeline

from pydantic import BaseModel





class Item(BaseModel):

    text: str





app = FastAPI()

classifier = pipeline("sentiment-analysis")





@app.get("/")

def root():

    """

    Обработчик для запроса GET на корневой URL.



    Returns:

        dict: Словарь с сообщением "Hello World".

    """

    return {"message": "Hello World"}





@app.post("/predict/")

def predict(item: Item):

    """

    Обработчик для запроса POST на /predict/.



    Args:

        item (Item): Объект Item, содержащий текст для анализа настроения.



    Returns:

        dict: Словарь с предсказанным настроением текста.

    """

    return classifier(item.text)[0]
