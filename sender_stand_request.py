import configuration
import requests
import data

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

def post_new_client_kit(kit_body, auth_token):
    headers_dict=data.headers.copy()
    headers_dict["Authorization"] = "Bearer " + auth_token
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=kit_body,
                         headers=headers_dict)



    # Si utilizas el diccionario de datos del archivo data.py una vez más, aplícale la función copy().
    # Es mejor no hacer ningún cambio en el diccionario de origen, ya que esto puede generar errores.
