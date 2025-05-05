# FastAPI: A Python web framework for building APIs.
  from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

print(read_root())

# Flask: A lightweight Python web framework.
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Home Page"

if __name__ == "__main__":
    app.run()

# Transforms: Hugging Face library for NLP tasks.
from transformers import pipeline

classifier = pipeline("sentiment-analysis")
result = classifier("I love this course") 
print(result)

# Onyx: ML model server for high-performance inferencing.

import onnxruntime as rt

sess = rt.InferenceSession("model.onnx")
input_name = sess.get_inputs()[0].name
res = sess.run(None, {input_name: x})

# OpenAPI: Specification for API documentation.
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

app = FastAPI()

def custom_openapi():
    return get_openapi(
        title="Custom title",
        version="2.5.0",
        description="Custom description",
    )
    
app.openapi = custom_openapi
