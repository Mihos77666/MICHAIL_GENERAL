# Version v002
import projectutils as pu # Importing our function library

class GuideData:
    def __init__(self, guidename, data_tables): # Class variables, guide name and data sheet from tables
        self.guidename = guidename
        self.datatables = data_tables

    def push_all(self, api_url, token):
        """
        The function sends all data to 3 tables: Guide, Task, Step
        Each push will return a data response and from it the function takes the unique ID of the created record. 
        This ID is used in the following table
        For Task and Step the previous ID is used to specify in the current task and step
        """
        url = api_url+"/cr22f_guidenames"   #Guide table url. Combine api_url parameter with table name
        task_url = api_url+"/cr22f_tasks"   #Task table url
        step_url = api_url+"/cr22f_steps"   #Step table url

        if len(self.datatables) > 0:    #Check the length of the task list, if len = 0 then no task in guide and skip push data
            guide_data = {
                "cr22f_guidename":self.guidename        #Data to write to the table Guide, there may be more than one data, it is important to check the correct column names 
            }
            req = pu.push_one_row(token, url, guide_data)   #Push Guide request
            guide_id = req.json()["cr22f_guidenameid"]      #Returned new guide row uniq ID
            prev_task_id = "None"
            for tab in self.datatables:     #Processing each task in a loop
                if len(tab) > 0:        #Checking the task for the count of steps
                    task_data ={
                        "cr22f_task":"Task Test",
                        "cr22f_prevtask": prev_task_id,
                        "cr22f_guideid":guide_id
                    }
                    task_req = pu.push_one_row(token,task_url,task_data)    #Push Task request
                    task_id = task_req.json()["cr22f_taskid"]       #Returned new task row uniq ID
                    prev_step_id = "None"

                    for step in tab:        #Processing each step in a loop
                        step_data = {
                            "cr22f_stepname":step[1],
                            "cr22f_prevstepid":prev_step_id,
                            "cr22f_taskid":task_id
                        }
                        step_req=pu.push_one_row(token,step_url,step_data)
                        prev_step_id = step_req.json()["cr22f_stepid"]      #Returned new step row uniq ID and updating the prev_step_id variable
                    prev_task_id = task_id      #updating the prev_task_id variable
                else:
                    print("No steps in the task")
        else:
            print("At least one task is needed")



config = pu.read_config("config.json")      #Reading an configuration from file
auth_token = pu.ms_authorization(config)        #Getting an authorization token

# Testing

api_url = config["url"]+"api/data/"+config["api_version"]       #Formating API url from base url and api version
guide, data = pu.parse_pdf("source.pdf")        #Pdf file parsing 
guide_ins = GuideData(guide,data)       #Creating a class instance 

guide_ins.push_all(api_url,auth_token)      #Use a class function to push all data to the dataverse