
<!-- PROJECT LOGO -->
<br />
<div align="center">

  <h3 align="center">Potenciando la seguridad: desarrollo y entrenamiento de un sistema de analítica de video para la detección automática de personas en imágenes de videovigilancia</h3>

  <p align="center">
    Cursos de C1b3rwall Academy 2024
    <br />
    <br />
    <br />

  </p>
</div>

<!-- ABOUT THE PROJECT -->
## Introducción

El propósito de este taller es proporcionar a personal sin experiencia previa en inteligencia artificial un enfoque sobre lo que supondría un sistema de análisis de video. La perspectiva se centra en lo que sería iedas
una solución que pueda integrarse con facilidad, sin requerir recursos técnicos considerables, en un sistema. Dadas las restricciones temporales y legales se aplicaría únicamente a la detección de personas en casos
avalados por la legislación vigente, para que sean los participantes en el taller los que puedan dirigir esta herramienta a ese tipo de escenarios y situaciones, amparados en todo caso en el correspondiente marco legal.

Contenidos del taller:
* Introducción
* Machine Learning
* Concepto de dataset
* Datasets más conocidos
* Herramientas de etiquetado: Roboflow
* Yolo
* Experimentación
* Conclusiones


<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

Este proyecto se ha llevado a cabo sobre un sistema operativo Ubuntu 22.04

### Prerequisites

#### Instalación Python 3.11 en el sistema operativo

1. Abre una terminal en tu sistema Ubuntu.
2. Asegúrate de tener todas las actualizaciones más recientes instaladas en tu sistema Ubuntu. Puedes hacerlo ejecutando los siguientes comandos:
  ```sh
    sudo apt update
    sudo apt upgrade
  ```
3. Importa el repositorio Python con las últimas versiones estables:
  ```sh
  sudo add-apt-repository ppa:deadsnakes/ppa -y
  ```
4. Ejecuta de nuevo APT update para asegurar que el repositorio se ha importado correctamente:
  ```sh
    sudo apt update
  ```
5. Instala Python 3.11:
  ```sh
    sudo apt install python3.11
  ```
6. Comprueba que se ha instalador correctamente:
  ```sh
    python3.11 --version
  ```

#### Instalación CUDA 12.2 en Ubuntu 22.04

1. Abre una terminal en tu sistema Ubuntu.
2. Asegúrate de tener todas las actualizaciones más recientes instaladas en tu sistema Ubuntu. Puedes hacerlo ejecutando los siguientes comandos:
  ```sh
    sudo apt update
    sudo apt upgrade
  ```
3. Listar los drivers recomendados de NVIDIA.
  ```sh
    sudo apt install ubuntu-drivers-common
    sudo ubuntu-drivers devices
  ```
4. Instalar el driver recomendado en el apartado anterior, en nuestro caso nvidia-driver-535
  ```sh
    sudo apt install nvidia-driver-535
  ```
5. Reiniciar el sistema:
  ```sh
    sudo reboot now
  ```
6. Comprobar que el driver se ha instalado correctamente:
  ```sh
    nvidia-smi
  ```

#### Instalación de CUDA toolkit en Ubuntu 22.04
1. Necesitaremos instalar el compilador gcc ya que se utilizará al instalar el kit de herramientas CUDA. Asegúrate de tener gcc instalado con el siguiente comando:
  ```sh
    sudo apt install gcc
  ```
2. Verificar la correcta instalación de GCC.
  ```sh
    gcc -v
  ```
4. Instalar CUDA toolkit
  ```sh
    wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-keyring_1.1-1_all.deb
    sudo dpkg -i cuda-keyring_1.1-1_all.deb
    sudo apt-get update
    sudo apt-get -y install cuda
  ```
5. Reiniciar el sistema:
  ```sh
    sudo reboot now
  ```
6. Configuración del entorno, añadir la siguientes líneas a bashrc mediante `nano ~ /.bashrc`:
  ```sh
  . ~/.bashrc
  ```
7. Comprobar que CUDA toolkit se ha instalado correctamente:
  ```sh
    nvcc -V
  ```

### Uso del sistema de detección para entrenamiento y clasificación

A continuación se muestran los comandos a ejecutar para usar el sistema de entrenamiento y clasificación con Yolo.

1. Clonar el repositorio
```sh
  git clone https://github.com/jmsecilla/yolo-c1b3rwall-people-detector.git
```
2. Instalar las dependencias de Python
```sh
  pip install requirements.txt
```
3. A partir de aquí, se recomienda hacer uso de un IDE de desarrollo para trabajar, aunque no es obligatorio.

#### Entrenamiento
```sh
  python train.py
```
#### Clasificación
```sh
  yolo detect predict imgsz=640 model=/home/jmcastillo/PycharmProjects/peopleDetector/src/runs/detect/train5/weights/best.pt source=/home/jmcastillo/Downloads/gun_chile.mp4 show=True
```

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Jose María Castillo Secilla - [@your_twitter](https://twitter.com/your_username) - jmsecilla@gmail.com

Project Link: [https://github.com/your_username/repo_name](https://github.com/your_username/repo_name)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
<!-- ## Acknowledgments -->



<p align="right">(<a href="#readme-top">back to top</a>)</p>

