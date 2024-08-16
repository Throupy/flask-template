# flask-template

This is a template flask app. I made this because I always seem to find myself creating the same file structure.

There is also a script `create_file_structure.sh` which will create the bare file structure with nothing in the files.

## Features
- Flask-SQLAlchemy with 1 User model with password hashing
- Functioning Login / Register / Logout routes
- Example route requiring authentication
- Login and Registration forms using WTForms

## Usage
There is a virtual environment and a requirements file, so using this should be pretty easy.

```
git clone https://github.com/Throupy/flask-template.git
cd flask-template
source venv/bin/activate
pip install -r requirements.txt
flask run (--debug --host 0.0.0.0)
```

The `config.py` file holds middleware / extension configuration options and fetches some environment variables. You may wish to use a `.env` file for this, but this is not included. 
