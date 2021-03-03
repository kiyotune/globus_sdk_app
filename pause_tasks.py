#!/usr/bin/python3

import globus_sdk
import app_auth as aa
import pprint

auth = globus_sdk.AccessTokenAuthorizer(aa.TRANSFER_TOKEN)
tc = globus_sdk.TransferClient(authorizer=auth)
#for task in tc.task_list():
#    if task["status"] == "ACTIVE":
#        print(">>> {} ({})".format(task["label"], task["task_id"]))
#        pprint.pprint(vars(task))
task_id = ["55cc043e-7b24-11eb-80c0-bd6c7ce89613"]
message = "[EMPIAR-10591] globus_sdk のテスト"
res = tc.endpoint_manager_pause_tasks(task_ids=task_id, message=message)
pprint.pprint(vars(res))
