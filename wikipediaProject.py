from pydantic import Field, BaseModel
import logging
from fastapi import FastAPI, Request , HTTPException
#from dataset import Dataset
import requests
from pymongo import MongoClient
from dotenv import dotenv_values   

logging.config.fileConfig('logging.conf', disable_existing_loggers=False)

log = logging.getLogger(__name__)
config  = dotenv_values(".env")

class wiki_data(BaseModel):
    id : int
    title : str
    text : str

app = FastAPI()            

@app.get("/")
def index_page():
    return {'message':'My Fast Api Project'}

@app.post("/{title}")                
def get_title(request: Request, title : str):         
    wiki = get_wikipedia_page(title)   
    request.app.state.collection.insert_one(dict(wiki))
    return {'message':'Database Entry Done'}

@app.get("/getData/{title}")
def RetrieveDataset(request: Request, title : str):
    title = title.capitalize()
    response = request.app.state.collection.find_one({"title":title}) 
    log.info("Retrieve data successfully")
    try:
        message = wiki_data(id=response["id"],title=response["title"],text=response["text"]) 

        return dict(message)

    except TypeError:
        log.warn("exception raise TypeError")
        raise HTTPException(
            status_code = 404,
            detail= f"{title} : Does not exist in DB",
            
        )
    
@app.get("/getall")
def get_all_details(request:Request):
    response = request.app.state.collection.find()
    message = {}
    n = 0
    for i in response:
        subMessage = wiki_data(id=i["id"],title=i["title"],text=i["text"])
        message[n] = dict(subMessage)
        n = n + 1
    return message

@app.on_event("startup")
def startup_db_client():
    app.mongodb_client = MongoClient(config["MONGODB_CONNECTION_URI"])
    app.database = app.mongodb_client[config["DB_NAME"]]
    app.state.collection = app.database.get_collection(config["COLLECTION_NAME"])
    log.info("Connected with Database")

@app.on_event("shutdown")
def shut_down_db_client():
    app.mongodb_client.close()
    log.info("Disconnected with %s Database",str(config["DB_NAME"]).upper())
    

def get_wikipedia_page(title):
    log.info("created Untility successfully")
    response = requests.get(
        'https://en.wikipedia.org/w/api.php',
        params={
            'action': 'query',
            'format': 'json',
            'titles': title,
            'prop': 'extracts',
            'explaintext': True,
        }
    , verify=False).json() 
    
    page = next(iter(response['query']['pages'].values()))
    
    return {
        'id': page['pageid'],
        'title': page['title'],
        'text': page['extract'],
    }





