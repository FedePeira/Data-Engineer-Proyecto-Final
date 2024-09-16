# Data-Engineer-Docker-Airflow
### Entorno Virtual
python -m venv venv
source venv/Scripts/activate  

********************************

### Requirements
pip install -r dependencies/requirements.txt  
python.exe -m pip install --upgrade pip

********************************

### Mover a carpeta de Directorio en Ubuntu
cd /mnt/d/Fede\ Ort/a.\ Portafolio/Coderhouse\ -\ Data\ Engineer/Docker-Airflow  

********************************

### Definición de variables Airflow
export AIRFLOW_VERSION=2.10.0  
export PYTHON_VERSION="$(python -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')"  
export CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"  

********************************

### Instalación de Airflow  
pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"  

********************************

### Correr Airflow
airflow standalone

********************************

### Instalar Docker
-- Abrir Terminal de Ubuntu en WSL
docker --version  

sudo apt update  
sudo apt upgrade  

sudo apt install apt-transport-https ca-certificates curl software-properties-common  

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -  

sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"  

sudo apt update  

sudo apt install docker-ce  

sudo service docker start  

sudo usermod -aG docker $USER 

********************************

### Correr Docker
docker-compose up

docker-compose up -d  

docker ps  

docker-compose logs airflow-webserver

docker-compose down  

docker-compose run --rm airflow-webserver airflow db init  

********************************

### Error Airflow
--> airflow.api.auth.backend.basic is not found

********************************

### Docker File
docker build -t my-airflow-image .

********************************

### Creando carpetas y descargando YML
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.9.2/docker-compose.yaml'

mkdir -p ./docker_airflow/{logs,dags,config,plugins}

echo -e "AIRFLOW_UID=$(id -u)" > ./.env

### Comenzamos el Proyecto
docker compose up airflow-init -d

docker compose up -d

docker build -t my-airflow-image .

********************************

### Error con la RAM
Uso Ubuntu para correr Linux y no se porque cuando abro Ubuntu, entro al administrador de Tareas y automaticamente, el procentaje de uso de mi RAM pasa a 95%, logre correr bastantes cosas pero ya ahora se hizo imposible, en 10 minutos tuve que reiniciar 3 veces porque se me trababa la computadora, de todas formas creo que logre que funcione.

********************************

### Detener el Contenedor Docker
docker compose -f ./etl/docker-compose.yaml down  
