import requests
import base64
import os

BASE_URL = "http://localhost:8000/pokemon"

def test_post_valid_ids():
    payload = {
        "json": [1, 4, 7],
        "filename": "test_output.xlsx"
    }
    response = requests.post(BASE_URL, json=payload)
    assert response.status_code == 200

    data = response.json()
    assert "excel_base64" in data

    # Verifica se o base64 pode ser convertido em arquivo válido
    decoded = base64.b64decode(data["excel_base64"])
    assert decoded[:4] == b'PK\x03\x04'  # Assinatura de arquivos .xlsx (ZIP)

def test_post_invalid_id():
    payload = {
        "json": [999999],  # ID inexistente
        "filename": "invalid_test.xlsx"
    }
    response = requests.post(BASE_URL, json=payload)
    assert response.status_code == 500  # Espera-se que a PokeAPI retorne um erro 404 no caso de IDs incorretos, o que irá gerar um erro 500 no Flask
    data = response.json()
    assert "error" in data

def test_post_empty_list():
    payload = {
        "json": [],
        "filename": "empty_test.xlsx"
    }
    response = requests.post(BASE_URL, json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "excel_base64" in data

def test_post_negative_id():
    payload = {
        "json": [-1,-2,-3],  # IDs negativos
        "filename": "negative_test.xlsx"
    }
    response = requests.post(BASE_URL, json=payload)
    assert response.status_code == 500 # Espera-se que a PokeAPI retorne um erro 404 no caso de IDs incorretos, o que irá gerar um erro 500 no Flask
    data = response.json()
    assert "error" in data

def test_post_not_all_valid_ids():
    payload = {
        "json": [1, 4, 7, 0, 150], # Nem todos os IDs são válidos
        "filename": "test_Not_All_Right.xlsx"
    }
    response = requests.post(BASE_URL, json=payload)
    assert response.status_code == 500

    data = response.json()
    assert "excel_base64" in data #Espera-se que mesmo com um erro da API, um excel seja gerado utilizando dos IDs válidos
 
    decoded = base64.b64decode(data["excel_base64"])
    assert decoded[:4] == b'PK\x03\x04'  # Assinatura de arquivos .xlsx (ZIP)

def test_post_decimal_id():
    payload = {
        "json": [1.0,2.2],  # IDs decimais
        "filename": "decimal_test.xlsx"
    }
    response = requests.post(BASE_URL, json=payload)
    assert response.status_code == 500 # Espera-se erro 500 por falha ao iterar tipos difernetes de dados
    data = response.json()
    assert "error" in data    

def test_post_invalid_type():
    payload = {
        "json": "not_a_list",
        "filename": "invalid_type.xlsx"
    }
    response = requests.post(BASE_URL, json=payload)
    
    # Espera-se erro 500 por falha ao iterar string como lista de IDs
    assert response.status_code == 500
    data = response.json()
    assert "error" in data
