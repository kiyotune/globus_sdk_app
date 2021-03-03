#!/usr/bin/python3

import globus_sdk
import app_auth as aa
import pprint

auth = globus_sdk.AccessTokenAuthorizer(aa.TRANSFER_TOKEN)
tc = globus_sdk.TransferClient(authorizer=auth)
for task in tc.task_list():
    if task["status"] == "ACTIVE":
        print(">>> {} ({})".format(task["label"], task["task_id"]))
        pprint.pprint(vars(task))

