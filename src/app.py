"""app.py
Entry point of the Flask application. Contains the endpoints.
Takes the port for execution from the environment (PORT)but has one by default.
"""
from os import environ
from threading import Thread
from bson.objectid import ObjectId
from flask import Flask, request
from mongodb import mongo_db
from background_tasks import update_mongo_data

app = Flask(__name__)
PORT = environ.get('PORT', default=5000)


@app.route('/new_task', methods=['POST'])
def new_task():
    """
    Function of the POST method that takes a command coming from the request, saves it in the database and in another
    execution thread, calls the function to execute the command.
    :return: the id of the task created
    """
    collection = mongo_db['tasks']
    document_id = collection.insert_one({'cmd': request.get_json().get('cmd')}).inserted_id
    thread = Thread(target=update_mongo_data, args=(document_id,))
    thread.daemon = True
    thread.start()
    return {"id": str(document_id)}


@app.route('/get_output/<id>', methods=['GET'])
def get_output(id):
    """
    Function of the GET method that receives the task id from the request,
    searches the task in the database and returns its output.
    :param id: the task id.
    :return: the comand and the result of the execution
    """
    collection = mongo_db['tasks']
    task = collection.find_one({'_id': ObjectId(id)})
    return {"cmd": task.get('cmd'), "output": task.get('output')}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT, threaded=True)
