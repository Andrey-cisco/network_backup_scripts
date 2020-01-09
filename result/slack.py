#!/usr/bin/env python3.6


f=open('/home/user/scripts/result/brief', 'r', encoding="utf-8")

def send_message_to_slack(text):
    from urllib import request, parse
    import json
 
    post = {"text": "{0}".format(text)}
 
    try:
        json_data = json.dumps(post)
        req = request.Request("https://hooks.slack.com/services/xxx",
                              data=json_data.encode('ascii'),
                              headers={'Content-Type': 'application/json'}) 
        resp = request.urlopen(req)
    except Exception as em:
        print("EXCEPTION: " + str(em))
 
send_message_to_slack(f.read())

#print(f.read())
