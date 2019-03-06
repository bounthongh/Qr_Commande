from app import db


class Biere(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(50))
    description = db.Column(db.String(200))
    prix = db.Column(db.Integer)
    en_stock = db.Column(db.Boolean)
    

class Cocktail(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(50))
    description = db.Column(db.String(200))
    prix = db.Column(db.Integer)
    en_stock = db.Column(db.Boolean)
    
    
class Soft(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(50))
    description = db.Column(db.String(200))
    prix = db.Column(db.Integer)
    en_stock = db.Column(db.Boolean)
    

class Alcohol(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(50))
    description = db.Column(db.String(200))
    prix = db.Column(db.Integer)
    en_stock = db.Column(db.Boolean)


class Vin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(50))
    description = db.Column(db.String(200))
    prix = db.Column(db.Integer)
    en_stock = db.Column(db.Boolean)
    
    
class BoissonChaude(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(50))
    description = db.Column(db.String(200))
    prix = db.Column(db.Integer)
    en_stock = db.Column(db.Boolean)
