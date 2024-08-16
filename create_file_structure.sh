#!/bin/bash

# Check if project name is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <project_name>"
    exit 1
fi

PROJECT_NAME=$1

mkdir -p $PROJECT_NAME
touch run.py

cd $PROJECT_NAME
touch __init__.py
touch models.py
touch config.py
touch extensions.py

mkdir templates static main users
mkdir static/css static/js

touch templates/layout.html templates/home.html templates/login.html templates/register.html
touch static/css/$PROJECT_NAME.css static/js/$PROJECT_NAME.js

# blueprints
touch main/__init__.py main/routes.py main/utils.py
touch users/__init__.py users/routes.py users/forms.py
