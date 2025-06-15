from app import app, db
from models import Hero, Power, HeroPower

with app.app_context():
    # Clear existing data
    HeroPower.query.delete()
    Hero.query.delete()
    Power.query.delete()

    # Powers
    strength = Power(name="super strength", description="gives the wielder super-human strengths")
    flight = Power(name="flight", description="gives the wielder the ability to fly through the skies at supersonic speed")
    senses = Power(name="super human senses", description="allows the wielder to use her senses at a super-human level")
    elasticity = Power(name="elasticity", description="can stretch the human body to extreme lengths")

    db.session.add_all([strength, flight, senses, elasticity])
    db.session.commit()

    # Heroes
    h1 = Hero(name="Kamala Khan", super_name="Ms. Marvel")
    h2 = Hero(name="Doreen Green", super_name="Squirrel Girl")
    h3 = Hero(name="Gwen Stacy", super_name="Spider-Gwen")

    db.session.add_all([h1, h2, h3])
    db.session.commit()

    # Hero Powers
    hp1 = HeroPower(hero_id=h1.id, power_id=flight.id, strength="Strong")
    hp2 = HeroPower(hero_id=h3.id, power_id=strength.id, strength="Average")

    db.session.add_all([hp1, hp2])
    db.session.commit()
