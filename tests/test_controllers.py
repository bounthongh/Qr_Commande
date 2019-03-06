import pytest
from flask import json


# ======================================================= INDEX ========================================================


def test_index(client):
    response = client.get('/')
    assert response.status_code == 200


# ======================================================= BIERE ========================================================


def test_biere_form(client):
    response = client.get('/private/biere_form')
    assert response.status_code == 200


def test_post_biere_true(client):
    response = client.post('/private/add_biere',
                           data=dict(nom='nom',
                                     description='description',
                                     prix='6',
                                     en_stock='1')
                           )
    json_data = json.loads(response.data)
    assert 'data' in json_data
    assert json_data['data'][0]['code'] == 200
    assert json_data['data'][0]['message'] == 'Success'
    assert json_data['data'][1]['id'] == 1
    assert json_data['data'][1]['nom'] == 'nom'
    assert json_data['data'][1]['description'] == 'description'
    assert json_data['data'][1]['prix'] == 6
    assert json_data['data'][1]['en_stock'] is True
    assert response.status_code == 200


def test_post_biere_none_en_stock(client):
    response = client.post('/private/add_biere',
                           data=dict(nom='nom',
                                     description='description',
                                     prix='6')
                           )
    json_data = json.loads(response.data)
    assert json_data['data'][0]['code'] == 400
    assert json_data['data'][0]['message'] == 'Bad Request'
    assert response.status_code == 400


def test_post_biere_none_prix(client):
    response = client.post('/private/add_biere',
                           data=dict(nom='nom',
                                     description='description',
                                     en_stock='1')
                           )
    json_data = json.loads(response.data)
    assert json_data['data'][0]['code'] == 400
    assert json_data['data'][0]['message'] == 'Bad Request'
    assert response.status_code == 400


def test_post_biere_none_decription(client):
    response = client.post('/private/add_biere',
                           data=dict(nom='nom',
                                     prix='6',
                                     en_stock='1')
                           )
    json_data = json.loads(response.data)
    assert json_data['data'][0]['code'] == 400
    assert json_data['data'][0]['message'] == 'Bad Request'
    assert response.status_code == 400


def test_post_biere_none_nom(client):
    response = client.post('/private/add_biere',
                           data=dict(description='description',
                                     prix='6',
                                     en_stock='1')
                           )
    json_data = json.loads(response.data)
    assert json_data['data'][0]['code'] == 400
    assert json_data['data'][0]['message'] == 'Bad Request'
    assert response.status_code == 400


def test_post_biere_empty_prix(client):
    response = client.post('/private/add_biere',
                           data=dict(nom='nom',
                                     description='description',
                                     prix='',
                                     en_stock='1')
                           )
    json_data = json.loads(response.data)
    assert json_data['data'][0]['code'] == 400
    assert json_data['data'][0]['message'] == 'Bad Request'
    assert response.status_code == 400


def test_post_biere_empty_description(client):
    response = client.post('/private/add_biere',
                           data=dict(nom='nom',
                                     description='',
                                     prix='6',
                                     en_stock='1')
                           )
    json_data = json.loads(response.data)
    assert json_data['data'][0]['code'] == 400
    assert json_data['data'][0]['message'] == 'Bad Request'
    assert response.status_code == 400


def test_post_biere_empty_nom(client):
    response = client.post('/private/add_biere',
                           data=dict(nom='',
                                     description='description',
                                     prix='6',
                                     en_stock='1')
                           )
    json_data = json.loads(response.data)
    assert json_data['data'][0]['code'] == 400
    assert json_data['data'][0]['message'] == 'Bad Request'
    assert response.status_code == 400


def test_get_biere(client):
    response = client.get('/private/get_biere')
    json_data = json.loads(response.data)
    assert 'data' in json_data
    assert json_data['code'] == 200
    assert json_data['message'] == 'Success'
    assert json_data['data'][0]['id'] == 1
    assert json_data['data'][0]['nom'] == 'nom'
    assert json_data['data'][0]['description'] == 'description'
    assert json_data['data'][0]['prix'] == 6
    assert json_data['data'][0]['en_stock'] is True
    assert response.status_code == 200


# ===================================================== COCKTAIL =======================================================


def test_form_cocktail(client):
    response = client.get('/private/cocktail_form')
    assert response.status_code == 200


def test_post_cocktail_true(client):
    response = client.post('/private/add_cocktail',
                           data=dict(nom='nom',
                                     description='description',
                                     prix='6',
                                     en_stock='1')
                           )
    json_data = json.loads(response.data)
    assert 'data' in json_data
    assert json_data['data'][0]['code'] == 200
    assert json_data['data'][0]['message'] == 'Success'
    assert json_data['data'][1]['id'] == 1
    assert json_data['data'][1]['nom'] == 'nom'
    assert json_data['data'][1]['description'] == 'description'
    assert json_data['data'][1]['prix'] == 6
    assert json_data['data'][1]['en_stock'] is True
    assert response.status_code == 200


def test_post_cocktail_none_en_stock(client):
    response = client.post('/private/add_cocktail',
                           data=dict(nom='nom',
                                     description='description',
                                     prix='6')
                           )
    json_data = json.loads(response.data)
    assert json_data['data'][0]['code'] == 400
    assert json_data['data'][0]['message'] == 'Bad Request'
    assert response.status_code == 400


def test_post_cocktail_none_prix(client):
    response = client.post('/private/add_cocktail',
                           data=dict(nom='nom',
                                     description='description',
                                     en_stock='1')
                           )
    json_data = json.loads(response.data)
    assert json_data['data'][0]['code'] == 400
    assert json_data['data'][0]['message'] == 'Bad Request'
    assert response.status_code == 400


def test_post_cocktail_none_decription(client):
    response = client.post('/private/add_cocktail',
                           data=dict(nom='nom',
                                     prix='6',
                                     en_stock='1')
                           )
    json_data = json.loads(response.data)
    assert json_data['data'][0]['code'] == 400
    assert json_data['data'][0]['message'] == 'Bad Request'
    assert response.status_code == 400


def test_post_cocktail_none_nom(client):
    response = client.post('/private/add_cocktail',
                           data=dict(description='description',
                                     prix='6',
                                     en_stock='1')
                           )
    json_data = json.loads(response.data)
    assert json_data['data'][0]['code'] == 400
    assert json_data['data'][0]['message'] == 'Bad Request'
    assert response.status_code == 400


def test_post_cocktail_empty_prix(client):
    response = client.post('/private/add_cocktail',
                           data=dict(nom='nom',
                                     description='description',
                                     prix='',
                                     en_stock='1')
                           )
    json_data = json.loads(response.data)
    assert json_data['data'][0]['code'] == 400
    assert json_data['data'][0]['message'] == 'Bad Request'
    assert response.status_code == 400


def test_post_cocktail_empty_description(client):
    response = client.post('/private/add_cocktail',
                           data=dict(nom='nom',
                                     description='',
                                     prix='6',
                                     en_stock='1')
                           )
    json_data = json.loads(response.data)
    assert json_data['data'][0]['code'] == 400
    assert json_data['data'][0]['message'] == 'Bad Request'
    assert response.status_code == 400


def test_post_cocktail_empty_nom(client):
    response = client.post('/private/add_cocktail',
                           data=dict(nom='',
                                     description='description',
                                     prix='6',
                                     en_stock='1')
                           )
    json_data = json.loads(response.data)
    assert json_data['data'][0]['code'] == 400
    assert json_data['data'][0]['message'] == 'Bad Request'
    assert response.status_code == 400


def test_get_cocktail(client):
    response = client.get('/private/get_cocktail')
    json_data = json.loads(response.data)
    assert 'data' in json_data
    assert json_data['code'] == 200
    assert json_data['message'] == 'Success'
    assert json_data['data'][0]['id'] == 1
    assert json_data['data'][0]['nom'] == 'nom'
    assert json_data['data'][0]['description'] == 'description'
    assert json_data['data'][0]['prix'] == 6
    assert json_data['data'][0]['en_stock'] is True
    assert response.status_code == 200


# ======================================================== SOFT ========================================================


def test_form_soft(client):
    response = client.get('/private/soft_form')
    assert response.status_code == 200


def test_post_soft_true(client):
    response = client.post('/private/add_soft',
                           data=dict(nom='nom',
                                     description='description',
                                     prix='6',
                                     en_stock='1')
                           )
    json_data = json.loads(response.data)
    assert 'data' in json_data
    assert json_data['data'][0]['code'] == 200
    assert json_data['data'][0]['message'] == 'Success'
    assert json_data['data'][1]['id'] == 1
    assert json_data['data'][1]['nom'] == 'nom'
    assert json_data['data'][1]['description'] == 'description'
    assert json_data['data'][1]['prix'] == 6
    assert json_data['data'][1]['en_stock'] is True
    assert response.status_code == 200


def test_post_soft_none_en_stock(client):
    response = client.post('/private/add_soft',
                           data=dict(nom='nom',
                                     description='description',
                                     prix='6')
                           )
    json_data = json.loads(response.data)
    assert json_data['data'][0]['code'] == 400
    assert json_data['data'][0]['message'] == 'Bad Request'
    assert response.status_code == 400


def test_post_soft_none_prix(client):
    response = client.post('/private/add_soft',
                           data=dict(nom='nom',
                                     description='description',
                                     en_stock='1')
                           )
    json_data = json.loads(response.data)
    assert json_data['data'][0]['code'] == 400
    assert json_data['data'][0]['message'] == 'Bad Request'
    assert response.status_code == 400


def test_post_soft_none_decription(client):
    response = client.post('/private/add_soft',
                           data=dict(nom='nom',
                                     prix='6',
                                     en_stock='1')
                           )
    json_data = json.loads(response.data)
    assert json_data['data'][0]['code'] == 400
    assert json_data['data'][0]['message'] == 'Bad Request'
    assert response.status_code == 400


def test_post_soft_none_nom(client):
    response = client.post('/private/add_soft',
                           data=dict(description='description',
                                     prix='6',
                                     en_stock='1')
                           )
    json_data = json.loads(response.data)
    assert json_data['data'][0]['code'] == 400
    assert json_data['data'][0]['message'] == 'Bad Request'
    assert response.status_code == 400


def test_post_soft_empty_prix(client):
    response = client.post('/private/add_soft',
                           data=dict(nom='nom',
                                     description='description',
                                     prix='',
                                     en_stock='1')
                           )
    json_data = json.loads(response.data)
    assert json_data['data'][0]['code'] == 400
    assert json_data['data'][0]['message'] == 'Bad Request'
    assert response.status_code == 400


def test_post_soft_empty_description(client):
    response = client.post('/private/add_soft',
                           data=dict(nom='nom',
                                     description='',
                                     prix='6',
                                     en_stock='1')
                           )
    json_data = json.loads(response.data)
    assert json_data['data'][0]['code'] == 400
    assert json_data['data'][0]['message'] == 'Bad Request'
    assert response.status_code == 400


def test_post_soft_empty_nom(client):
    response = client.post('/private/add_soft',
                           data=dict(nom='',
                                     description='description',
                                     prix='6',
                                     en_stock='1')
                           )
    json_data = json.loads(response.data)
    assert json_data['data'][0]['code'] == 400
    assert json_data['data'][0]['message'] == 'Bad Request'
    assert response.status_code == 400


def test_get_soft(client):
    response = client.get('/private/get_soft')
    json_data = json.loads(response.data)
    assert 'data' in json_data
    assert json_data['code'] == 200
    assert json_data['message'] == 'Success'
    assert json_data['data'][0]['id'] == 1
    assert json_data['data'][0]['nom'] == 'nom'
    assert json_data['data'][0]['description'] == 'description'
    assert json_data['data'][0]['prix'] == 6
    assert json_data['data'][0]['en_stock'] is True
    assert response.status_code == 200


# ====================================================== ALCOHOL =======================================================


def test_form_alcohol(client):
    response = client.get('/private/alcohol_form')
    assert response.status_code == 200


def test_post_alcohol_true(client):
    response = client.post('/private/add_alcohol',
                           data=dict(nom='nom',
                                     description='description',
                                     prix='6',
                                     en_stock='1')
                           )
    json_data = json.loads(response.data)
    assert 'data' in json_data
    assert json_data['data'][0]['code'] == 200
    assert json_data['data'][0]['message'] == 'Success'
    assert json_data['data'][1]['id'] == 1
    assert json_data['data'][1]['nom'] == 'nom'
    assert json_data['data'][1]['description'] == 'description'
    assert json_data['data'][1]['prix'] == 6
    assert json_data['data'][1]['en_stock'] is True
    assert response.status_code == 200


def test_post_alcohol_none_en_stock(client):
    response = client.post('/private/add_alcohol',
                           data=dict(nom='nom',
                                     description='description',
                                     prix='6')
                           )
    json_data = json.loads(response.data)
    assert json_data['data'][0]['code'] == 400
    assert json_data['data'][0]['message'] == 'Bad Request'
    assert response.status_code == 400


def test_post_alcohol_none_prix(client):
    response = client.post('/private/add_alcohol',
                           data=dict(nom='nom',
                                     description='description',
                                     en_stock='1')
                           )
    json_data = json.loads(response.data)
    assert json_data['data'][0]['code'] == 400
    assert json_data['data'][0]['message'] == 'Bad Request'
    assert response.status_code == 400


def test_post_alcohol_none_decription(client):
    response = client.post('/private/add_alcohol',
                           data=dict(nom='nom',
                                     prix='6',
                                     en_stock='1')
                           )
    json_data = json.loads(response.data)
    assert json_data['data'][0]['code'] == 400
    assert json_data['data'][0]['message'] == 'Bad Request'
    assert response.status_code == 400


def test_post_alcohol_none_nom(client):
    response = client.post('/private/add_alcohol',
                           data=dict(description='description',
                                     prix='6',
                                     en_stock='1')
                           )
    json_data = json.loads(response.data)
    assert json_data['data'][0]['code'] == 400
    assert json_data['data'][0]['message'] == 'Bad Request'
    assert response.status_code == 400


def test_post_alcohol_empty_prix(client):
    response = client.post('/private/add_alcohol',
                           data=dict(nom='nom',
                                     description='description',
                                     prix='',
                                     en_stock='1')
                           )
    json_data = json.loads(response.data)
    assert json_data['data'][0]['code'] == 400
    assert json_data['data'][0]['message'] == 'Bad Request'
    assert response.status_code == 400


def test_post_alcohol_empty_description(client):
    response = client.post('/private/add_alcohol',
                           data=dict(nom='nom',
                                     description='',
                                     prix='6',
                                     en_stock='1')
                           )
    json_data = json.loads(response.data)
    assert json_data['data'][0]['code'] == 400
    assert json_data['data'][0]['message'] == 'Bad Request'
    assert response.status_code == 400


def test_post_alcohol_empty_nom(client):
    response = client.post('/private/add_alcohol',
                           data=dict(nom='',
                                     description='description',
                                     prix='6',
                                     en_stock='1')
                           )
    json_data = json.loads(response.data)
    assert json_data['data'][0]['code'] == 400
    assert json_data['data'][0]['message'] == 'Bad Request'
    assert response.status_code == 400


def test_get_alcohol(client):
    response = client.get('/private/get_alcohol')
    json_data = json.loads(response.data)
    assert 'data' in json_data
    assert json_data['code'] == 200
    assert json_data['message'] == 'Success'
    assert json_data['data'][0]['id'] == 1
    assert json_data['data'][0]['nom'] == 'nom'
    assert json_data['data'][0]['description'] == 'description'
    assert json_data['data'][0]['prix'] == 6
    assert json_data['data'][0]['en_stock'] is True
    assert response.status_code == 200


# ======================================================== VIN ========================================================


def test_form_vin(client):
    response = client.get('/private/vin_form')
    assert response.status_code == 200


def test_post_vin_true(client):
    response = client.post('/private/add_vin',
                           data=dict(nom='nom',
                                     description='description',
                                     prix='6',
                                     en_stock='1')
                           )
    json_data = json.loads(response.data)
    assert 'data' in json_data
    assert json_data['data'][0]['code'] == 200
    assert json_data['data'][0]['message'] == 'Success'
    assert json_data['data'][1]['id'] == 1
    assert json_data['data'][1]['nom'] == 'nom'
    assert json_data['data'][1]['description'] == 'description'
    assert json_data['data'][1]['prix'] == 6
    assert json_data['data'][1]['en_stock'] is True
    assert response.status_code == 200


def test_post_vin_none_en_stock(client):
    response = client.post('/private/add_vin',
                           data=dict(nom='nom',
                                     description='description',
                                     prix='6')
                           )
    json_data = json.loads(response.data)
    assert json_data['data'][0]['code'] == 400
    assert json_data['data'][0]['message'] == 'Bad Request'
    assert response.status_code == 400


def test_post_vin_none_prix(client):
    response = client.post('/private/add_vin',
                           data=dict(nom='nom',
                                     description='description',
                                     en_stock='1')
                           )
    json_data = json.loads(response.data)
    assert json_data['data'][0]['code'] == 400
    assert json_data['data'][0]['message'] == 'Bad Request'
    assert response.status_code == 400


def test_post_vin_none_decription(client):
    response = client.post('/private/add_vin',
                           data=dict(nom='nom',
                                     prix='6',
                                     en_stock='1')
                           )
    json_data = json.loads(response.data)
    assert json_data['data'][0]['code'] == 400
    assert json_data['data'][0]['message'] == 'Bad Request'
    assert response.status_code == 400


def test_post_vin_none_nom(client):
    response = client.post('/private/add_vin',
                           data=dict(description='description',
                                     prix='6',
                                     en_stock='1')
                           )
    json_data = json.loads(response.data)
    assert json_data['data'][0]['code'] == 400
    assert json_data['data'][0]['message'] == 'Bad Request'
    assert response.status_code == 400


def test_post_vin_empty_prix(client):
    response = client.post('/private/add_vin',
                           data=dict(nom='nom',
                                     description='description',
                                     prix='',
                                     en_stock='1')
                           )
    json_data = json.loads(response.data)
    assert json_data['data'][0]['code'] == 400
    assert json_data['data'][0]['message'] == 'Bad Request'
    assert response.status_code == 400


def test_post_vin_empty_description(client):
    response = client.post('/private/add_vin',
                           data=dict(nom='nom',
                                     description='',
                                     prix='6',
                                     en_stock='1')
                           )
    json_data = json.loads(response.data)
    assert json_data['data'][0]['code'] == 400
    assert json_data['data'][0]['message'] == 'Bad Request'
    assert response.status_code == 400


def test_post_vin_empty_nom(client):
    response = client.post('/private/add_vin',
                           data=dict(nom='',
                                     description='description',
                                     prix='6',
                                     en_stock='1')
                           )
    json_data = json.loads(response.data)
    assert json_data['data'][0]['code'] == 400
    assert json_data['data'][0]['message'] == 'Bad Request'
    assert response.status_code == 400


def test_get_vin(client):
    response = client.get('/private/get_vin')
    json_data = json.loads(response.data)
    assert 'data' in json_data
    assert json_data['code'] == 200
    assert json_data['message'] == 'Success'
    assert json_data['data'][0]['id'] == 1
    assert json_data['data'][0]['nom'] == 'nom'
    assert json_data['data'][0]['description'] == 'description'
    assert json_data['data'][0]['prix'] == 6
    assert json_data['data'][0]['en_stock'] is True
    assert response.status_code == 200


# =================================================== BOISSON CHAUDE ===================================================


def test_form_boisson_chaude(client):
    response = client.get('/private/boisson_chaude_form')
    assert response.status_code == 200


def test_post_boisson_chaude_true(client):
    response = client.post('/private/add_boisson_chaude',
                           data=dict(nom='nom',
                                     description='description',
                                     prix='6',
                                     en_stock='1')
                           )
    json_data = json.loads(response.data)
    assert 'data' in json_data
    assert json_data['data'][0]['code'] == 200
    assert json_data['data'][0]['message'] == 'Success'
    assert json_data['data'][1]['id'] == 1
    assert json_data['data'][1]['nom'] == 'nom'
    assert json_data['data'][1]['description'] == 'description'
    assert json_data['data'][1]['prix'] == 6
    assert json_data['data'][1]['en_stock'] is True
    assert response.status_code == 200


def test_post_boisson_chaude_none_en_stock(client):
    response = client.post('/private/add_boisson_chaude',
                           data=dict(nom='nom',
                                     description='description',
                                     prix='6')
                           )
    json_data = json.loads(response.data)
    assert json_data['data'][0]['code'] == 400
    assert json_data['data'][0]['message'] == 'Bad Request'
    assert response.status_code == 400


def test_post_boisson_chaude_none_prix(client):
    response = client.post('/private/add_boisson_chaude',
                           data=dict(nom='nom',
                                     description='description',
                                     en_stock='1')
                           )
    json_data = json.loads(response.data)
    assert json_data['data'][0]['code'] == 400
    assert json_data['data'][0]['message'] == 'Bad Request'
    assert response.status_code == 400


def test_post_boisson_chaude_none_decription(client):
    response = client.post('/private/add_boisson_chaude',
                           data=dict(nom='nom',
                                     prix='6',
                                     en_stock='1')
                           )
    json_data = json.loads(response.data)
    assert json_data['data'][0]['code'] == 400
    assert json_data['data'][0]['message'] == 'Bad Request'
    assert response.status_code == 400


def test_post_boisson_chaude_none_nom(client):
    response = client.post('/private/add_boisson_chaude',
                           data=dict(description='description',
                                     prix='6',
                                     en_stock='1')
                           )
    json_data = json.loads(response.data)
    assert json_data['data'][0]['code'] == 400
    assert json_data['data'][0]['message'] == 'Bad Request'
    assert response.status_code == 400


def test_post_boisson_chaude_empty_prix(client):
    response = client.post('/private/add_boisson_chaude',
                           data=dict(nom='nom',
                                     description='description',
                                     prix='',
                                     en_stock='1')
                           )
    json_data = json.loads(response.data)
    assert json_data['data'][0]['code'] == 400
    assert json_data['data'][0]['message'] == 'Bad Request'
    assert response.status_code == 400


def test_post_boisson_chaude_empty_description(client):
    response = client.post('/private/add_boisson_chaude',
                           data=dict(nom='nom',
                                     description='',
                                     prix='6',
                                     en_stock='1')
                           )
    json_data = json.loads(response.data)
    assert json_data['data'][0]['code'] == 400
    assert json_data['data'][0]['message'] == 'Bad Request'
    assert response.status_code == 400


def test_post_boisson_chaude_empty_nom(client):
    response = client.post('/private/add_boisson_chaude',
                           data=dict(nom='',
                                     description='description',
                                     prix='6',
                                     en_stock='1')
                           )
    json_data = json.loads(response.data)
    assert json_data['data'][0]['code'] == 400
    assert json_data['data'][0]['message'] == 'Bad Request'
    assert response.status_code == 400


def test_get_boisson_chaude(client):
    response = client.get('/private/get_boisson_chaude')
    json_data = json.loads(response.data)
    assert 'data' in json_data
    assert json_data['code'] == 200
    assert json_data['message'] == 'Success'
    assert json_data['data'][0]['id'] == 1
    assert json_data['data'][0]['nom'] == 'nom'
    assert json_data['data'][0]['description'] == 'description'
    assert json_data['data'][0]['prix'] == 6
    assert json_data['data'][0]['en_stock'] is True
    assert response.status_code == 200

# ======================================================================================================================
