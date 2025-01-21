import sender_stand_request
import data

def get_kit_body(name):
    current_body=data.user_body.copy()
    current_body["name"]=name
    return current_body

def get_new_user_token():
    user_body=data.user_body
    response=sender_stand_request.post_new_user(user_body)
    return response.json()["authToken"]

def positive_assert(name):
    user_body = get_kit_body(name)
    user_response = sender_stand_request.post_new_user(user_body)

    assert user_response.status_code == 201
    assert user_response.json()["authToken"] != ""

def negative_assert(name):
    user_body = get_kit_body(name)
    user_response = sender_stand_request.post_new_user(user_body)

    assert user_response.status_code == 400
    assert user_response.json()["code"] == 400
    assert user_response.json()["message"] == "No se han aprobado todos los parámetros requeridos"\
                                              "El nombre debe contener sólo letras latino, un espacio y un guión. De 2 a 15 caracteres"

def test_create_user_1_letter_in_name_get_success_response():
    positive_assert(data.test1)

def test_create_user_511_letter_in_name_get_success_response():
    positive_assert(data.test2)

def test_create_user_empty_name_get_error_response():

def test_create_user_511_letter_in_name_get_error_response():

def test_create_user_has_special_symbol_in_name_get_success_response():

def test_create_user_english_letter_in_name_get_success_response():

def test_create_user_has_number_in_name_get_success_response():

def test_create_user_no_name_get_error_response():

def test_create_user_number_type_name_get_error_response():