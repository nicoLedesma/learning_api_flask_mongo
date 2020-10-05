"""background_tasks.py
Contains the functions that are executed in an asynchronous way.
"""

import shlex
import subprocess
from bson.objectid import ObjectId
from mongodb import mongo_db


def update_mongo_data(task_id):
    """
    Receives an id of a task, finds this task in the database, takes the respective command and calls the function that
    executes it. Then, this function updates the task in the data base with the result of that execution.
    :param task_id:
    :return:string: Success
    """
    collection = mongo_db['tasks']
    task = collection.find_one({'_id': ObjectId(task_id)})
    result = execute_cmd(task.get('cmd'))
    collection.update_one({"_id": task_id}, {"$set": {"output": result}})
    return "Successfully updated document"


def execute_cmd(cmd):
    """
    Execute the command received by parameter and return a string with the result of that execution.
    :param cmd: command to execute
    :return:result: result of the execution of the command
    """
    try:
        result = subprocess.Popen(shlex.split(str(cmd)),
                                  stdout=subprocess.PIPE,
                                  stderr=subprocess.PIPE).stdout.read()
        if not result:
            result = "Command not executed."
    except Exception as exception:
        result = f'Command not recognize. Error: {exception}'

    if isinstance(result, bytes):
        result = result.decode("utf-8") #byte to string
    return result
