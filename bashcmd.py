import subprocess, json
from json_crud import read_json

def get(command):
    #makes bash requests with subprocess
    print(command)
    command_parse = subprocess.run(command, shell=True, capture_output=True)
    output_dct = json.loads(command_parse.stdout.decode())

    return output_dct

def get_access_token(curl):
    #defines the command and request access token
    access_token = get('curl -d '+curl)
    return access_token

def get_id(curl):
    #defines the command and request user id
    id = get('curl -H '+curl)['id']
    return id
