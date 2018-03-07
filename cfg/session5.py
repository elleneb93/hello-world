import requests

id = "84600bca7507293656495e8972aec659"
payload = {'q':'Sheffield, UK', 'units':'metric', 'appid':id} #info being communicated

def query_weather(payload):
    endpoint = "http://api.openweathermap.org/data/2.5/weather" #link to source. not just online, can be data
    #endpoint is the front end part, where api communicating with
    response = requests.get(endpoint, params=payload) #get request
    return response

response = query_weather(payload)
#print(response.status_code)  #200 = successful
print(response.text)
def jsonify(response):
    json_response = response.json()
    return json_response

json_response = jsonify(response)
print("\n")
print(json_response)
print(json_response['main']['temp'])
