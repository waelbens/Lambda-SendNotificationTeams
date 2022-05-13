import urllib3 
import json
http = urllib3.PoolManager() 

def lambda_handler(event, context): 
    url = "https://xxxxx.webhook.office.com/webhookb2/xxxxxxxxxxxxxxxx"    
    msg = {
        "text": event['Records'][0]['Sns']['Message']
    }
    encoded_msg = json.dumps(msg).encode('utf-8')
    resp = http.request('POST',url, body=encoded_msg)
    print({
        "message": event['Records'][0]['Sns']['Message'], 
        "status_code": resp.status, 
        "response": resp.data
    })
