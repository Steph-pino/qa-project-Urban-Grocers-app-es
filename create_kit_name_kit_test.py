import sender_stand_request
import data

def get_kit_body(name):
    current_body=data.user_body.copy()
    current_body["name"]=name
    return current_body

def get_new_user_token():
    user_body=data.user_body
    user_response=sender_stand_request.post_create_new_user(user_body)
    return user_response

def positive_assert(kit_body):
    create_kit_response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert create_kit_response.status_code == 201
    assert create_kit_response.json()["name"] == kit_body["name"]

def negative_assert(kit_body):
    create_kit_response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert create_kit_response.status_code == 400
    #assert user_response.json()["message"] == "El nombre debe contener sólo letras latino, un espacio y un guión. De 2 a 15 caracteres"

def negative_assert_no_params(kit_body):
    create_kit_response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert create_kit_response.status_code == 400
    #assert user_response.json()["message"] == "No se han aprobado todos los parámetros requeridos"

def test_create_user_1_letter_in_name_get_success_response():
    kit_body = get_kit_body(data.test1)
    positive_assert(kit_body)

def test_create_user_511_letter_in_name_get_success_response():
    kit_body = get_kit_body(data.test2)
    positive_assert(kit_body)

def test_create_user_empty_name_get_error_response():
    kit_body = get_kit_body(data.test3)
    negative_assert(kit_body)

def test_create_user_512_letter_in_name_get_error_response():
    kit_body = get_kit_body(data.test4)
    negative_assert(kit_body)

def test_create_user_has_special_symbol_in_name_get_success_response():
    kit_body = get_kit_body(data.test5)
    positive_assert(kit_body)

def test_create_user_blank_space_in_name_get_success_response():
    kit_body = get_kit_body(data.test6)
    positive_assert(kit_body)

def test_create_user_has_number_in_name_get_success_response():
    kit_body = get_kit_body(data.test7)
    positive_assert(kit_body)

def test_create_user_has_no_name_get_error_response():
    kit_body = data.user_body.copy()
    kit_body.pop("firstName")
    negative_assert_no_params(kit_body)

def test_create_user_number_type_name_get_error_response():
    kit_body = get_kit_body(data.test9)
    negative_assert(kit_body)
