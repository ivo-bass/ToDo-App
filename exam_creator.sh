#! /bin/sh

echo "Hello to Django Project-Maker 1.0"

# shellcheck disable=SC2039
echo -e "\e[1;31m Write a name for main directory of your project \e[0m"
# shellcheck disable=SC2162
read dirname
mkdir "$dirname"
echo "Directory '$dirname' was created!"
# shellcheck disable=SC2164
cd "$dirname"

echo "Creating virtual environment 'venv'..."
python -m venv venv
echo "Done"

# shellcheck disable=SC2039
source venv/bin/activate
echo "Venv is activated!"

echo "Upgrading pip..."
python -m pip install --upgrade pip

echo "Installing Django..."
pip install django

echo " "
# shellcheck disable=SC2039
echo -e "\e[1;31m Write name for your project \e[0m"
# shellcheck disable=SC2162
read projectname
echo "Creating $projectname Django project..."
django-admin startproject "$projectname" .
echo "Project '$projectname' is created!"

mkdir ./templates
echo "Templates dir made."

mkdir ./static
echo "Static dir made."

cp ../exam_creator.sh ./exam_project_creator.sh

echo " "
# shellcheck disable=SC2039
echo -e "\e[1;31m Write name for your first app \e[0m"
# shellcheck disable=SC2162
read firstapp

echo "Creating '$firstapp' app INSIDE '$projectname' directory..."
python manage.py startapp $firstapp

echo "Starting initial migrations..."
python manage.py makemigrations
python manage.py migrate
echo "Done"

# shellcheck disable=SC2039
echo -e "\e[1;31m Creating .gitignore... \e[0m"
# shellcheck disable=SC2129
echo "venv" >> .gitignore
echo ".vscode" >> .gitignore
echo ".idea/" >> .gitignore
echo "__pycache__" >> .gitignore

# shellcheck disable=SC2039
echo -e "\e[1;31m Creating README... \e[0m"
echo "# $projectname" > README.md
# shellcheck disable=SC2129
echo "This project is instantiated by my shell script which:" >> README.md
echo "1. Creates venv" >> README.md
echo "2. Installs Django" >> README.md
echo "3. Starts project" >> README.md
echo "4. Creates app OUTSIDE the project" >> README.md
echo "5. Creates .gitignore" >> README.md
echo "6. Creates README" >> README.md
echo "7. Creates requirements" >> README.md
echo "8. Creates local git repo, adds all and does init commit" >> README.md
echo "9. Makes 'templates' dir" >> README.md
echo " " >> README.md
echo "!!! I NEED TO MAKE THE FOLLOWING CHANGES AFTER OPENING PYCHARM:" >> README.md
echo "1. Edit run configuration in PyCharm - set the starting point and add the venv." >> README.md
echo "2. Move the app inside the project." >> README.md
echo "3. In settings.py you need to add '$projectname.$firstapp', to INSTALLED_APPS list." >> README.md
echo "4. Add STATICFILES_DIRS to settings.py" >> README.md
echo "5. Mark templates folder as templates folder" >> README.md
echo "\n"
echo " "
echo "***Script by Ivailo Ignatov - IvoBass***" >> README.md

echo "Creating requirements.txt"
pip freeze > requirements.txt

echo "Initializing git repo..."
git init
git add .
git commit -m "initial commit"

echo " "
echo "All set!"
echo "PyCharm will open."
echo " "
# shellcheck disable=SC2039
echo -e "\e[1;31m !!! OPEN README.md TO FINALIZE SETUP !!! \e[0m"
echo " "
echo "Hit ENTER to finish"
# shellcheck disable=SC2034
# shellcheck disable=SC2162
read start

charm ../"$dirname"
