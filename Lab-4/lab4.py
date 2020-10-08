import http.client
import urllib.parse

key ='AT68QYQ94MQEWXL3'

def lab4():
    while True:
        proj = "L3-T-7"
        cmail = "michaelslokar@cmail.carleton.ca"
        ID = "c"
        params = urllib.parse.urlencode({'field1': proj,'field2': cmail, 'field3': ID, 'key':key }) 
        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = http.client.HTTPConnection("api.thingspeak.com:80")
        try:
            conn.request("POST", "/update", params, headers)
            response = conn.getresponse()
            print (proj, cmail, ID)
            print (response.status, response.reason)
            data = response.read()
            conn.close()
        except:
            print ("connection failed")
        break
if __name__ == "__main__":
        while True:
                lab4()