#! /bin/sh

echo "Hello to Django Project-Maker 1.0"

echo "First of all you need to navigate to the directory where your project will be created BEFORE you start the program."
echo "Are you ready to start?"
echo "[y/n]"
read prompt

if [ $prompt == "n" ]
then
   exit
fi

echo -e "\e[1;31m Write a name for main directory of your project \e[0m"
read dirname
mkdir $dirname
echo "Directory '$dirname' was created!"
cd $dirname

echo "Creating virtual environment 'venv'..."
python -m venv venv
echo "Done"

source venv/bin/activate
echo "Venv is activated!"

echo "Upgrading pip..."
python -m pip install --upgrade pip

echo "Installing Django..."
pip install django

echo " "
echo -e "\e[1;31m Write name for your project \e[0m"
read projectname
echo "Creating $projectname Django project..."
django-admin startproject $projectname .
cd $projectname
echo "Project '$projectname' is created!"

echo " "
echo -e "\e[1;31m Write name for your first app \e[0m"
read firstapp

echo "Creating '$firstapp' app INSIDE '$projectname' directory..."
python ../manage.py startapp $firstapp

echo "Starting initial migrations..."
python ../manage.py makemigrations
python ../manage.py migrate
echo "Done"

cd ..
echo -e "\e[1;31m Creating .gitignore... \e[0m"
echo "venv" >> .gitignore
echo ".vscode" >> .gitignore
echo ".idea/" >> .gitignore
echo "__pycache__" >> .gitignore

echo -e "\e[1;31m Creating README... \e[0m"
echo "#$projectname" > README.md
echo "!!! YOU NEED TO MAKE THE FOLLOWING CHANGES:" >> README.md
echo "Open 'apps.py' located in $projectname/$firstapp and inside of the class change name to '$projectname.$firstapp'" >> README.md
echo "In settings.py you need to add '$projectname.$firstapp', to INSTALLED_APPS list." >> README.md

echo "Creating requirements.txt"
pip freeze > requirements.txt

echo "Initializing git repo..."
git init
git add .
git commit -m "initial commit"

echo " "
echo "All set!"
echo "VSCode will open."
echo " "
echo -e "\e[1;31m !!! OPEN README.md TO FINALIZE SETUP !!! \e[0m"
echo " "
echo "Hit ENTER to finish"
read start

code .
