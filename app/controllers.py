from flask import render_template, request, redirect, url_for, Blueprint, json, Response
from sqlalchemy import exc
from app.models import Biere, Cocktail, Soft, Alcohol, Vin, BoissonChaude
import app

module_home = Blueprint('home', __name__, url_prefix='/')


# ======================================================= INDEX ========================================================


@module_home.route('/', methods=['GET'])
def index_common():
    bieres = Biere.query.all()
    cocktails = Cocktail.query.all()
    softs = Soft.query.all()
    alcohols = Alcohol.query.all()
    vins = Vin.query.all()
    boissons_chaudes = BoissonChaude.query.all()
    return render_template('index.html',
                           bieres=bieres,
                           cocktails=cocktails,
                           softs=softs,
                           alcohols=alcohols,
                           vins=vins,
                           boissons_chaudes=boissons_chaudes)


# ======================================================= BIERE ========================================================


@module_home.route('/private/biere_form')
def biere_form():
    return """
    <form method="POST" action="/private/add_biere">
    nom
    <input type="text" name="nom">
    description
    <input type="text" name="description">
    prix
    <input type="text" name="prix"><br>
    en stock
    <input type="checkbox" name="en_stock" value="1">
    <input type="hidden" name="en_stock" value="0">
    <input type="submit" value="submit">
    </form>
    """


@module_home.route('/private/add_biere', methods=['POST'])
def post_biere():
    raised = True
    try:
        nom = request.form['nom']
        description = request.form['description']
        prix = int(request.form['prix'])
        en_stock = request.form['en_stock']
        if en_stock == '1':
            en_stock = True
        elif en_stock == '0':
            en_stock = False
        if prix == "":
            raised = True
            raise ValueError
        if nom == "" or description == "":
            raised = True
            raise KeyError
        raised = False
    except (KeyError, ValueError):
        data = [
            {'code': 400, 'message': 'Bad Request'}
        ]
        code = 400
    finally:
        if raised is False:
            try:
                category = Biere(nom=nom,
                                 description=description,
                                 prix=prix,
                                 en_stock=en_stock)
                app.db.session.add(category)
                app.db.session.commit()
                db_id = category.id
                data = [
                    {'code': 200,
                     'message': 'Success'},
                    {'id': db_id,
                     'nom': nom,
                     'description': description,
                     'prix': prix,
                     'en_stock': en_stock}
                ]
                code = 200
            except exc.SQLAlchemyError:
                data = [
                    {'code': 500, 'message': 'Internal Error'}
                ]
                code = 500
        return Response(json.dumps({'data': data}), code)

        
@module_home.route('/private/get_biere', methods=['GET'])
def get_biere():
    bieres = Biere.query.all()
    data = []
    for biere in bieres:
        data.append(
            {'id': biere.id,
             'nom': biere.nom,
             'description': biere.description,
             'prix': biere.prix,
             'en_stock': biere.en_stock}
        )
    return Response(json.dumps({"code": 200, "message": "Success", "data": data}), 200)


# ===================================================== COCKTAIL =======================================================


@module_home.route('/private/cocktail_form')
def cocktail_form():
    return """
    <form method="POST" action="/private/add_cocktail">
    nom
    <input type="text" name="nom">
    description
    <input type="text" name="description">
    prix
    <input type="text" name="prix"><br>
    en_stock
    <input type="checkbox" name="en_stock" value="1">
    <input type="hidden" name="en_stock" value="0">
    <input type="submit" value="submit">
    </form>
    """


@module_home.route('/private/add_cocktail', methods=['post'])
def post_cocktail():
    raised = True
    try:
        nom = request.form['nom']
        description = request.form['description']
        prix = int(request.form['prix'])
        en_stock = request.form['en_stock']
        if en_stock == '1':
            en_stock = True
        elif en_stock == '0':
            en_stock = False
        else:
            raised = True
            raise KeyError
        if prix == "":
            raised = True
            raise ValueError
        if nom == "" or description == "":
            raised = True
            raise KeyError
        raised = False
    except (KeyError, ValueError):
        data = [
            {'code': 400, 'message': 'Bad Request'}
        ]
        code = 400
    finally:
        if raised is False:
            try:
                category = Cocktail(nom=nom,
                                    description=description,
                                    prix=prix,
                                    en_stock=en_stock)
                app.db.session.add(category)
                app.db.session.commit()
                db_id = category.id
                data = [
                    {'code': 200,
                     'message': 'Success'},
                    {'id': db_id,
                     'nom': nom,
                     'description': description,
                     'prix': prix,
                     'en_stock': en_stock}
                ]
                code = 200
            except exc.SQLAlchemyError:
                data = [
                    {'code': 500, 'message': 'Internal Error'}
                ]
                code = 500
        return Response(json.dumps({'data': data}), code)


@module_home.route('/private/get_cocktail', methods=['GET'])
def get_cocktail():
    cocktails = Cocktail.query.all()
    data = []
    for cocktail in cocktails:
        data.append({
            'id': cocktail.id,
            'nom': cocktail.nom,
            'description': cocktail.description,
            'prix': cocktail.prix,
            'en_stock': cocktail.en_stock
        })
    return Response(json.dumps({"code": 200, "message": "Success", "data": data}), 200)


# ======================================================== SOFT ========================================================


@module_home.route('/private/soft_form')
def soft_form():
    return """
    <form method="POST" action="/private/add_soft">
    nom
    <input type="text" name="nom">
    description
    <input type="text" name="description">
    prix
    <input type="text" name="prix"><br>
    en stock
    <input type="checkbox" name="en_stock" value="1">
    <input type="hidden" name="en_stock" value="0">
    <input type="submit" value="submit">
    </form>
    """


@module_home.route('/private/add_soft', methods=['post'])
def post_soft():
    raised = True
    try:
        nom = request.form['nom']
        description = request.form['description']
        prix = int(request.form['prix'])
        en_stock = request.form['en_stock']
        if en_stock == '1':
            en_stock = True
        elif en_stock == '0':
            en_stock = False
        if prix == "":
            raised = True
            raise ValueError
        if nom == "" or description == "":
            raised = True
            raise KeyError
        raised = False
    except (KeyError, ValueError):
        data = [
            {'code': 400, 'message': 'Bad Request'}
        ]
        code = 400
    finally:
        if raised is False:
            try:
                category = Soft(nom=nom,
                                description=description,
                                prix=prix,
                                en_stock=en_stock)
                app.db.session.add(category)
                app.db.session.commit()
                db_id = category.id
                data = [
                    {'code': 200,
                     'message': 'Success'},
                    {'id': db_id,
                     'nom': nom,
                     'description': description,
                     'prix': prix,
                     'en_stock': en_stock}
                ]
                code = 200
            except exc.SQLAlchemyError:
                data = [
                    {'code': 500, 'message': 'Internal Error'}
                ]
                code = 500
        return Response(json.dumps({'data': data}), code)


@module_home.route('/private/get_soft', methods=['GET'])
def get_soft():
    softs = Soft.query.all()
    data = []
    for soft in softs:
        data.append({
            'id': soft.id,
            'nom': soft.nom,
            'description': soft.description,
            'prix': soft.prix,
            'en_stock': soft.en_stock
            })
    return Response(json.dumps({"code": 200, "message": "Success", "data": data}), 200)


# ====================================================== ALCOHOL =======================================================


@module_home.route('/private/alcohol_form')
def alcohol_form():
    return """
    <form method="POST" action="/private/add_alcohol">
    nom
    <input type="text" name="nom">
    description
    <input type="text" name="description">
    prix
    <input type="text" name="prix"><br>
    en stock
     <input type="checkbox" name="en_stock" value="1">
    <input type="hidden" name="en_stock" value="0">
    <input type="submit" value="submit">
    </form>
    """


@module_home.route('/private/add_alcohol', methods=['POST'])
def post_alcohol():
    raised = True
    try:
        nom = request.form['nom']
        description = request.form['description']
        prix = int(request.form['prix'])
        en_stock = request.form['en_stock']
        if en_stock == '1':
            en_stock = True
        elif en_stock == '0':
            en_stock = False
        if prix == "":
            raised = True
            raise ValueError
        if nom == "" or description == "":
            raised = True
            raise KeyError
        raised = False
    except (KeyError, ValueError):
        data = [
            {'code': 400, 'message': 'Bad Request'}
        ]
        code = 400
    finally:
        if raised is False:
            try:
                category = Alcohol(nom=nom,
                                   description=description,
                                   prix=prix,
                                   en_stock=en_stock)
                app.db.session.add(category)
                app.db.session.commit()
                db_id = category.id
                data = [
                    {'code': 200,
                     'message': 'Success'},
                    {'id': db_id,
                     'nom': nom,
                     'description': description,
                     'prix': prix,
                     'en_stock': en_stock}
                ]
                code = 200
            except exc.SQLAlchemyError:
                data = [
                    {'code': 500, 'message': 'Internal Error'}
                ]
                code = 500
        return Response(json.dumps({'data': data}), code)


@module_home.route('/private/get_alcohol', methods=['GET'])
def get_alcohol():
    alcohols = Alcohol.query.all()
    data = []
    for alcohol in alcohols:
        data.append({
            'id': alcohol.id,
            'nom': alcohol.nom,
            'description': alcohol.description,
            'prix': alcohol.prix,
            'en_stock': alcohol.en_stock
        })
    return Response(json.dumps({"code": 200, "message": "Success", "data": data}), 200)


# ======================================================== VIN =========================================================


@module_home.route('/private/vin_form')
def vin_form():
    return """
    <form method="POST" action="/private/add_vin">
    nom
    <input type="text" name="nom">
    description
    <input type="text" name="description">
    prix
    <input type="text" name="prix"><br>
    en stock
     <input type="checkbox" name="en_stock" value="1">
    <input type="hidden" name="en_stock" value="0">
    <input type="submit" value="submit">
    </form>
    """


@module_home.route('/private/add_vin', methods=['POST'])
def post_vin():
    raised = True
    try:
        nom = request.form['nom']
        description = request.form['description']
        prix = int(request.form['prix'])
        en_stock = request.form['en_stock']
        if en_stock == '1':
            en_stock = True
        elif en_stock == '0':
            en_stock = False
        if prix == "":
            raised = True
            raise ValueError
        if nom == "" or description == "":
            raised = True
            raise KeyError
        raised = False
    except (KeyError, ValueError):
        data = [
            {'code': 400, 'message': 'Bad Request'}
        ]
        code = 400
    finally:
        if raised is False:
            try:
                category = Vin(nom=nom,
                               description=description,
                               prix=prix,
                               en_stock=en_stock)
                app.db.session.add(category)
                app.db.session.commit()
                db_id = category.id
                data = [
                    {'code': 200,
                     'message': 'Success'},
                    {'id': db_id,
                     'nom': nom,
                     'description': description,
                     'prix': prix,
                     'en_stock': en_stock}
                ]
                code = 200
            except exc.SQLAlchemyError:
                data = [
                    {'code': 500, 'message': 'Internal Error'}
                ]
                code = 500
        return Response(json.dumps({'data': data}), code)


@module_home.route('/private/get_vin', methods=['GET'])
def get_vin():
    vins = Vin.query.all()
    data = []
    for vin in vins:
        data.append({
            'id': vin.id,
            'nom': vin.nom,
            'description': vin.description,
            'prix': vin.prix,
            'en_stock': vin.en_stock
        })
    return Response(json.dumps({"code": 200, "message": "Success", "data": data}), 200)


# ================================================== BOISSON CHAUDE ====================================================



@module_home.route('/private/boisson_chaude_form')
def boisson_chaude_form():
    return """
    <form method="POST" action="/private/add_boisson_chaude">
    nom
    <input type="text" name="nom">
    description
    <input type="text" name="description">
    prix
    <input type="text" name="prix"><br>
    en stock
     <input type="checkbox" name="en_stock" value="1">
    <input type="hidden" name="en_stock" value="0">
    <input type="submit" value="submit">
    </form>
    """


@module_home.route('/private/add_boisson_chaude', methods=['POST'])
def post_boisson_chaude():
    raised = True
    try:
        nom = request.form['nom']
        description = request.form['description']
        prix = int(request.form['prix'])
        en_stock = request.form['en_stock']
        if en_stock == '1':
            en_stock = True
        elif en_stock == '0':
            en_stock = False
        if prix == "":
            raised = True
            raise ValueError
        if nom == "" or description == "":
            raised = True
            raise KeyError
        raised = False
    except (KeyError, ValueError):
        data = [
            {'code': 400, 'message': 'Bad Request'}
        ]
        code = 400
    finally:
        if raised is False:
            try:
                category = BoissonChaude(nom=nom,
                                         description=description,
                                         prix=prix,
                                         en_stock=en_stock)
                app.db.session.add(category)
                app.db.session.commit()
                db_id = category.id
                data = [
                    {'code': 200,
                     'message': 'Success'},
                    {'id': db_id,
                     'nom': nom,
                     'description': description,
                     'prix': prix,
                     'en_stock': en_stock}
                ]
                code = 200
            except exc.SQLAlchemyError:
                data = [
                    {'code': 500, 'message': 'Internal Error'}
                ]
                code = 500
        return Response(json.dumps({'data': data}), code)


@module_home.route('/private/get_boisson_chaude', methods=['GET'])
def get_boisson_chaude():
    boissons_chaudes = BoissonChaude.query.all()
    data = []
    for boisson_chaude in boissons_chaudes:
        data.append({
            'id': boisson_chaude.id,
            'nom': boisson_chaude.nom,
            'description': boisson_chaude.description,
            'prix': boisson_chaude.prix,
            'en_stock': boisson_chaude.en_stock
        })
    return Response(json.dumps({"code": 200, "message": "Success", "data": data}), 200)
