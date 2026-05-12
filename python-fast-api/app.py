import json
from fastapi import FastAPI

app = FastAPI()

def read_json_file():
    with open("server.json", "r") as file:
        data = json.load(file)
    return data

@app.get("/")
def home():
    return { "message" : "FastAPI is Working!!" }

@app.get("/data")
def get_data():
    data = read_json_file()
    return data

@app.get("/data/serverlist")
def get_serverlist():
    data = read_json_file()
    return list(data.keys())    # Return a list of server names as a JSON response

@app.get("/data/{servername}")
def get_server(servername: str):
    data = read_json_file()
    return { "server" : data.get(servername, {"error": "Server Not Found"}) }