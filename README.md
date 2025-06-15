
 Superheroes API

A RESTful Flask API for managing superheroes, their powers, and hero-power relationships. Built using Python, Flask, SQLAlchemy, and SQLite.

Features

- View all heroes
- View a specific hero and their powers
- Update a power's description
- Assign a power to a hero with strength level

Endpoints

 GET /heroes
Returns a list of all heroes.

GET /heroes/<id>
Returns details of a specific hero including their powers.

PATCH /powers/<id>
Updates a power's description.

Request body (JSON):
```json
{
  "description": "Updated description here"
}
POST /hero_powers
Assigns a power to a hero.

Request body (JSON):

json
Copy
Edit
{
  "hero_id": 1,
  "power_id": 2,
  "strength": "Strong"
}
Tech Stack
Python 3

Flask

Flask-SQLAlchemy

Flask-Migrate

SQLite

Installation
Clone the repository:

bash
Copy
Edit
git clone git@github.com:ali-b-cell/phase_4_superheroes_api.git
cd phase_4_superheroes_api
Install dependencies:

bash
Copy
Edit
pipenv install
Set up the database:

bash
Copy
Edit
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
(Optional) Seed the database:

bash
Copy
Edit
python seed.py
Start the server:

bash
Copy
Edit
python app.py
Testing
You can test the endpoints using Postman or curl.

License
MIT License

Author
Alice Nthenge

yaml
Copy
Edit

---

You can now paste this entire content into a file named `README.md` in your project root, then commit and push it:

```bash
git add README.md
git commit -m "Add README"
git push