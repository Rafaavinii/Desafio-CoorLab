#!/bin/bash

echo "Iniciando o frontend Vue.js..."
cd frontend/cb-viagens
npm install
npm run serve &
echo "Frontend Vue.js iniciado."



# Iniciar o backend Django
echo "Iniciando o backend Django..."
cd ../../backend

python3 -m venv venv

source venv/bin/activate

cd cbviagens

pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate

python manage.py runserver 3000 &

echo "Backend Django iniciado."

# Mantém o script em execução
wait
