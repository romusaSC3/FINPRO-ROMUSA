
import AI_model from AI_file 
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
    imagepath = ...
    # dataset --> diolah AI
    result_AI = AI_model(parameter=image_path)
    category_db = Table("books", MetaData(bind=get_engine()), autoload=True)
    category = run_query(select(category_db).where(category_db.c.ID == result_AI))
    
    if category:
        return {"message": "Product similiar to this image", "data": category}, 200
    else:
        return {"error": "No one product similiar to this image"}, 400