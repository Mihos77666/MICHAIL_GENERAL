# Version v002
from tabula import read_pdf
import requests
import msal
import json

def parse_pdf(filepath):
    """
    PDF parsing

    """
    table_list = read_pdf(filepath, pages="all")
    guide_name = table_list[0].columns[2]       #Get guide name
    obj_index = 1
    step_id = 0
    out_table_list=[]

    for pdf_tab_num in table_list:

        current_table=[]
        if pdf_tab_num.columns[0] == 'Unnamed: 0':      #Check if the first column is blank, if true then it's a header table (0-2351-333 OMS ESC) and need to skip it
            continue
        step_id += 1
        for row in pdf_tab_num.itertuples():
            data = [obj_index, row[2], row[3], "INNACTIVE", step_id]
            current_table.append(data)
            obj_index += 1
        out_table_list.append(current_table)
        obj_index = 1
    return guide_name, out_table_list

def read_config(filepath):
    """ 
    Read JSON file with config data
    """
    with open(filepath, "r", encoding="utf-8") as file:
        config_data = json.load(file)
    return config_data

def ms_authorization(config):
    """
    Receiving an autorization token from the MS service
    The function returns the authentication token
    """
    db_app = msal.ConfidentialClientApplication(
        config["client_id"],
        authority=config["authority"],
        client_credential=config["client_secret"])

    print("----Token Acquiring----")
    result = db_app.acquire_token_silent(config["scope"], account=None)
    if not result:
        result = db_app.acquire_token_for_client(scopes=config["scope"])
    token = result['access_token']
    print("----Auth Token----")
    print(token)
    return token

def push_one_row(token, url, data, id_name=None):
    """
    Function for send data to the dataverse
    with return data (return=representation header)
    id_name is a optional parameter, If it is specified, the function will print the value of this field in the response (e.g. check the unique ID received)
    The function return the response from POST request
    """
    headers = {     #Forming headers for a request
        "Accept": "application/json",
        "Content-type": "application/json",
        "Prefer": "return=representation",
        "Authorization": "Bearer "+ token
    }
    json_data = json.dumps(data)
    print("Push data to {}".format(url))
    response = requests.request("POST", url, json=json_data, headers=headers)       #Push the data and get response
    if not id_name==None:       #If define id_name parameter, then print value of that field
        id = response.json()[id_name]
        if not id == None:
            print("Id is {}".format(id))
        else:
            print("ID not found")
    return response
