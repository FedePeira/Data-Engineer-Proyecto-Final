# Data-Engineer-ProyectoFinal
********************************

### Uso
Tuve que usar codespace porque no me dejaba instalar Docker por problemas con mi Windows y en Ubuntu pasa el problema de RAM que cuento mas abajo

********************************

### Creacion del TaskFile
sh -c "$(curl --location https://taskfile.dev/install.sh)" -- -d
Crea carpeta Bin con el archivo task.exec

********************************

### Corrida del TaskFile
1 --> ./bin/task pre_project
2 --> ./bin/task start_project
3 --> ./bin/task down_project
4 --> ./bin/task cleanup

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

### Detener el Contenedor Docker
docker compose -f ./etl/docker-compose.yaml down  

********************************

### Error con la RAM
Uso Ubuntu para correr Linux y no se porque cuando abro Ubuntu, entro al administrador de Tareas y automaticamente, el procentaje de uso de mi RAM pasa a 95%, logre correr bastantes cosas pero ya ahora se hizo imposible, en 10 minutos tuve que reiniciar 3 veces porque se me trababa la computadora, de todas formas creo que logre que funcione.