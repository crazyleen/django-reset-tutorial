import json
import requests

"""
http --json POST http://127.0.0.1:8000/stamp/ title="goodluck"
http http://127.0.0.1:8000/stamp/1/
http --json PUT http://127.0.0.1:8000/stamp/1/ title="goodluck"
http DELETE http://127.0.0.1:8000/stamp/1/
"""

basicURL = "http://localhost:8000"

def post():
    """
    POST /stamp/
    H1, S1, T1 (ISSUER|ENCRYTED_TIME_AND_H1)
    H0, S0
    stamped_by (ESeal ID <—> ESeal.pubkey)
    accepters (ESeal ID list，需要盖章的法人，1. 可以正式验章，一旦正式验章，需要征得其同意才能撤章；2. 一旦盖章，视为已正式验章）
    receivers（不能继续盖章，但是可以正式验章，并且正式验章后，撤章时需要征得其同意）
    observers (可以非正式验章，撤章时无需征得其同意)f
    """

    url = "/stamp/"
    data = {
        "H1" : "h1",
        "S1" : "s1",
        "T1" : "T1",
        "H0" : "H0",
        "S0" : "S0",
        "stamped_by" : "user0",
        "accepters" : ("user1", "user2", "user3"),
        "receivers" : ("user11", "user12", "user13"),
        "observers" : ("user21", "user22", "user23"),
        "title" : "your title",
    }
    req = requests.post(basicURL + url, data=json.dumps(data), headers={'Content-Type': 'application/json'})
    if req.status_code != 201:   
        print(req.status_code)
    print(req.text)


post()

