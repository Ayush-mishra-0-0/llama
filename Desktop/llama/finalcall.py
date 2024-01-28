import requests

print("----------------------------------------hello---------------------------------")
url_scarcity = 'http://127.0.0.1:8080/api/hello'
url_sp = 'http://127.0.0.1:8081/api/hello'
url_o = 'http://127.0.0.1:8090/api/hello'
url_md = 'http://127.0.0.1:5001/api/hello'
url_fa = 'http://127.0.0.1:8888/api/hello'

for i in range(10):
    t=input("give your text :")
    data = {'input_string': t}
    
    response = requests.post(url_scarcity, json=data)
    data2 = response.json()  # Corrected
    print("1"+str(data2))
    
    response = requests.post(url_sp, json=data)
    data2 = response.json()  # Corrected
    print("2"+str(data2))

    response = requests.post(url_o, json=data)
    data2 = response.json()  # Corrected
    print("3"+str(data2))


    response = requests.post(url_md, json=data)
    data2 = response.json()  # Corrected
    print("4"+str(data2))


    response = requests.post(url_fa, json=data)
    data2 = response.json()  # Corrected
    print("5"+str(data2))   



    
