import requests
import json
from wsgiref.simple_server import make_server

#enconding: utf-8
# if __name__ == '__main__':
#     url = 'http://localhost:3000/api/alumnos'
#     response = requests.get(url)

#     if response.status_code == 200:

#         # crea un archivo txt con toda la informacion 
#         content = response.content

#         file = open('alumnos.txt', 'wb')
#         file.write(content)
#         file.close()

#         # trae los datos y los concatena
#         response_json = response.json()

#         for entry in response_json:
#             entry['id']
#             entry['nombre']
#             entry['apellido']
#             print(entry)

#             print(entry['nombre'] + entry['apellido'])

# if __name__ == '__main__':
#     url = 'http://localhost:3000/api/alumnos/post'
#     payload = {'nombre': 'Agustin'}

#     if response.status_code == 200:

#         response_json = response.json()

#         for entry in response_json:
#             entry['id']
#             entry['nombre']
#             entry['apellido']
#             print(entry)


def creaTXT():
    url = 'http://localhost:3000/api/alumnos'
    response = requests.get(url)

    if response.status_code == 200:

        # crea un archivo txt con toda la informacion 
        content = response.content

        file = open('alumnos.txt', 'wb')
        file.write(content)
        file.close()


def application (environ, start_response):

    headers = [ ('Content-type', 'application/json') ]

    start_response('200 OK', headers)
    creaTXT()
    response = {
        'mensaje': 'Se creo el TXT con exito :)!!!'
    }
    # if response.status_code == 200:
        
    # }
    # else:
    #     response = {
    #     'mensaje': 'Error al crear el TXT :('
    # }

    return [ bytes(json.dumps(response), 'utf-8') ]

with make_server('localhost', 8000, application) as http:
    print("Server on port 8000")

    http.serve_forever()