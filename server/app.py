from flask import Flask, jsonify, abort, request
from flask_migrate import Migrate
from models import db, Hero, Power, HeroPower  

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///superheroes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)


@app.route("/")
def home():
    return "Superheroes API is running!"

@app.route("/heroes")
def get_heroes():
    heroes = Hero.query.all()
    return jsonify([
        {
            "id": hero.id,
            "name": hero.name,
            "super_name": hero.super_name
        } for hero in heroes
    ])


@app.route("/heroes/<int:id>")
def get_hero_by_id(id):
    hero = Hero.query.get(id)
    if not hero:
        abort(404, description="Hero not found")
    
    return jsonify({
        "id": hero.id,
        "name": hero.name,
        "super_name": hero.super_name,
        "powers": [
            {
                "id": hp.power.id,
                "name": hp.power.name,
                "description": hp.power.description
            } for hp in hero.hero_powers
        ]
    })


@app.route("/powers/<int:id>", methods=["GET", "PATCH"])
def power_detail(id):
    power = Power.query.get(id)
    if not power:
        abort(404, description="Power not found")

    if request.method == "GET":
        return jsonify({
            "id": power.id,
            "name": power.name,
            "description": power.description
        }), 200

    if request.method == "PATCH":
        data = request.get_json()
        new_description = data.get("description")

    if not new_description or len(new_description) < 20:
            return jsonify({"errors": ["description must be at least 20 characters"]}), 400
    power.description = new_description
    db.session.commit()

    return jsonify({
            "id": power.id,
            "name": power.name,
            "description": power.description
        }), 20
    
@app.route("/hero_powers", methods=["POST"])
def create_hero_power():
    data = request.get_json()

    valid_strengths = ["Strong", "Weak", "Average"]
    if data.get("strength") not in valid_strengths:
        return {"errors": ["Strength must be Strong, Weak, or Average"]}, 400

    hero = db.session.get(Hero, data.get("hero_id"))
    power = db.session.get(Power, data.get("power_id"))


    if not hero or not power:
        return {"errors": ["Invalid hero_id or power_id"]}, 400

    hero_power = HeroPower(
        strength=data["strength"],
        hero_id=hero.id,
        power_id=power.id
    )

    db.session.add(hero_power)
    db.session.commit()

    return jsonify({
        "id": hero.id,
        "name": hero.name,
        "super_name": hero.super_name,
        "powers": [
            {
                "id": hp.power.id,
                "name": hp.power.name,
                "description": hp.power.description
            } for hp in hero.hero_powers
        ]
    }), 201

if __name__ == "__main__":
    app.run(debug=True)



