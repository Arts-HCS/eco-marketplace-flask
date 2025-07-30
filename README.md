# Markin (Flask App)

**Markin** is a sustainable web platform inspired by sites like Mercado Libre — but with an environmental focus. It allows users to register, log in, and publish recyclable or reusable products for others to discover. While the buying functionality is still under development, the app already implements product creation and image uploading with Flask and SQLAlchemy.

---

## Features

- Environmentally focused: only reusable/recyclable products
- User registration and login system
- Product creation with images and descriptions
- Display of personal and community products
- SQLAlchemy and SQLite database integration
- Custom frontend with HTML and CSS

---

## Development Status

> **Currently in progress (~70%)**
- User login & registration complete
- Product posting and display
- Purchasing flow not yet implemented

---

## Technologies Used

| Tech         | Purpose                          |
|--------------|----------------------------------|
| Flask        | Python web framework             |
| HTML/CSS     | Frontend layout and styling      |
| SQLAlchemy   | ORM for managing database models |
| SQLite       | Lightweight local DB             |
| Flask-Migrate| Handling migrations (optional)   |

---

## Screenshots

<img width="1470" height="801" alt="Screenshot 2025-07-29 at 18 38 37" src="https://github.com/user-attachments/assets/bea1c55e-06a9-41f6-afc7-682ad6910b8a" />


---

## Getting Started

1. **Clone this repo**
```bash
git clone https://github.com/Arts-HCS/eco-marketplace-flask.git
cd eco-marketplace-flask
```

2. Install Dependencies
```bash
pip install flask flask_sqlalchemy flask_migrate
```

3. Set up the database
```bash
python main.py  # This will trigger db.create_all() on first run
```

4. Run the app
```bash
python main.py
```

5. Then visit http://127.0.0.1:5000/ in your browser.

---

## Models

### User

| Field        | Type    | Description           |
|--------------|---------|-----------------------|
| id           | int     | Primary key           |
| login        | string  |                       |
| password     | string  |                       |
| name         | string  |                       |
| age          | int     |                       |
| gender       | string  |                       |
| personal_id  | string  | Unique                |

### Product

| Field        | Type    | Description                      |
|--------------|---------|----------------------------------|
| id           | int     | Primary key                      |
| name         | string  |                                  |
| category     | string  |                                  |
| price        | int     |                                  |
| currency     | string  |                                  |
| quantity     | int     |                                  |
| image        | string  | File name                        |
| description  | string  |                                  |
| personal_id  | string  | Foreign key to user (personal_id) |


## License

MIT License — free to use, modify, and expand.
