
from ai import label_pred
# Code from AI
from PIL import Image
import base64
from utils import get_engine, run_query
from flask import Blueprint, request
from sqlalchemy import (
    MetaData,
    Table,
    delete,
    insert,
    select,
)
from sqlalchemy.exc import IntegrityError

@app.route("/products/search_image", methods=["POST"])
def search_image(image):
    imagebase64 = request.json['image'] #berupa base64
    # image = base64 convert to image (kalau AI butuh mengolah dalam bentuk image)
    # imagepath = ...

    with open("image.png", "wb") as fh:
        fh.write(base64.decodebytes(imagebase64))
    # imagepath = "Archive/image.png"
    img.save('Archive/image.png.jpg', 'PNG')
    result_AI = label_pred #label_pred dari file ai
    category_db = Table("Category", MetaData(bind=get_engine()), autoload=True)
    category = run_query(select(category_db).where(category_db.c.ID == result_AI))
    
    if category:
        return {"message": "Product similiar to this image", "data": category}, 200
    else:
        return {"error": "No one product similiar to this image"}, 400

