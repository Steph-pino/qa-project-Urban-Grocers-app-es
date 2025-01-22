import configuration
import requests
import data

def post_create_new_user(body):
    user_response = requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)
    authorization_token = user_response.json()["authToken"]
    return authorization_token

def post_new_client_kit(kit_body, auth_token):
    headers_dict=data.headers.copy()
    headers_dict["Authorization"] = "Bearer " + auth_token
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=kit_body,
                         headers=headers_dict)

