### 1 print: 
Es una función en Python que nos permite mostrar información en la consola. Podemos utilizarla para imprimir mensajes, valores de variables u otros datos que queramos visualizar durante la ejecución del programa.

```python
my_var = 'Esta oracion'
print(my_var+' es un string '+my_var+' tambien es un string')
```

```python
my_var = 'Esta oracion es un string'
num_oraciones = 3
print('Esta oracion es un string %s En total, tenemos %d oraciones.'%(my_var, num_oraciones))
```

```python
num_oraciones = 3
print(f'Hemos visto al menos {num_oraciones+2} formas de mostrar {num_oraciones} oraciones')
```

### 2 input: 
Es una función en Python que nos permite recibir datos de entrada desde el usuario. Al utilizarla, el programa se detiene y espera a que el usuario ingrese un valor. Luego, ese valor puede ser almacenado en una variable para su posterior uso en el programa.

```python
numero = int(input('Ingrese un numero: '))
print(type(numero))
# <class 'int'>
```

### 3 Librería: 
En Python, una librería es un conjunto de funciones, clases y variables predefinidas que se agrupan para realizar tareas específicas. Estas librerías amplían las capacidades del lenguaje y nos permiten utilizar funcionalidades adicionales sin tener que implementarlas desde cero. Podemos importar una librería en nuestro programa para acceder a sus funcionalidades y utilizarlas en nuestro código.

La libreria **sys** nos permite pasar ARGUMENTOS a un archivo .py ejecutado por linea de comandos.

al ejecutar en CMD: saludo.py Juan
```python
import sys
print(f'Buenos dias {sys.argv[1]}')
print(f'El nombre de este script es: {sys.argv[0]}')
# Buenos dias Juan
# El nombre de este script es: saludo.py
```

### 4 Extensión .py: 
En Python, la extensión de archivo .py se utiliza para identificar los archivos de código fuente escritos en Python. Estos archivos contienen el código que será interpretado y ejecutado por el intérprete de Python. Al guardar nuestros programas en archivos con extensión .py, podemos ejecutarlos y compartirlos con otros desarrolladores.


## INTERACCION CON SISTEMA DE ARCHIVOS

### 1 Crear una carpeta nueva:
Para crear una carpeta nueva en Python, utilizamos el método makedirs() de la librería os. Simplemente especificamos la ruta de la carpeta que queremos crear y este método se encarga de crearla en el sistema de archivos.

```python
import os
os.makedirs('Carpeta_nueva')
```

### 2 Lista el contenido de una carpeta:
Para listar el contenido de una carpeta en Python, utilizamos el método listdir() de la librería os. Este método nos devuelve una lista con los nombres de los archivos y subdirectorios que se encuentran en la carpeta especificada.

```python
import os
os.listdir('./')
```

### 3 Mostrar el directorio de trabajo:
Para mostrar el directorio de trabajo actual en Python, utilizamos el método getcwd() de la librería os. Este método devuelve una cadena de texto que representa la ruta absoluta del directorio actual.

```python
import os
od.getcwd()
```

### 4 Mostrar el tamaño en bytes de un archivo pasado como parámetro:
Para obtener el tamaño en bytes de un archivo en Python, utilizamos el método getsize() de la librería os.path. Simplemente especificamos la ruta del archivo y este método nos devuelve el tamaño en bytes.

```python
import os
os.path.getsize('Mi_archivo')
```

### 5 Verificar si el parámetro pasado a la función es un archivo:
Para verificar si un parámetro es un archivo en Python, utilizamos el método isfile() de la librería os.path. Este método devuelve un valor booleano (True o False) que indica si el parámetro es un archivo válido.

```python
import os
os.path.isfile('Mi_archivo')
```

### 6 Verificar si el parámetro pasado a la función es una carpeta:
Para verificar si un parámetro es una carpeta en Python, utilizamos el método isdir() de la librería os.path. Este método devuelve un valor booleano que indica si el parámetro es una carpeta válida.

```python
import os
os.path.isdir('Mi_carpeta')
```

### 7 Cambiar directorio/carpeta:
Para cambiar el directorio o carpeta actual en Python, utilizamos el método chdir() de la librería os. Simplemente especificamos la ruta de la nueva carpeta a la que queremos cambiar y este método actualiza el directorio actual.

```python
import os
os.chdir('Mi_otra_carpeta')
```

### 8 Renombrar un archivo:
Para renombrar un archivo en Python, utilizamos el método rename() de la librería os. Especificamos la ruta y el nombre actual del archivo, junto con el nuevo nombre que queremos asignarle.

```python
import os
os.rename('Mi_archivo', 'Nombre_nuevo')
```

### 9 Eliminar un archivo:
Para eliminar un archivo en Python, utilizamos el método remove() de la librería os. Simplemente especificamos la ruta del archivo que queremos eliminar y este método se encarga de borrarlo del sistema de archivos.

```python
import os
os.remove(os.getcwd()+'/datos.txt')
```

### 10 Eliminar una carpeta (vacia):
Para eliminar una carpeta en Python, utilizamos el método rmdir() de la librería os. Especificamos la ruta de la carpeta que queremos eliminar y este método se encarga de borrarla, siempre y cuando esté vacía.

```python
import os
os.rmdir(os.getcwd()+'/Mi_carpeta')
```


## Manejo de archivos y Web Scrapping

La función open() tiene una sintaxis sencilla:

open(<archivo>,<modo>)

Donde <archivo> es la ubicación del archivo con el que queremos trabajar y <modo> es uno de los siguientes modos de trabajo con ese archivo:

    'r': read
    'w': write
    'a': anexado (agrega, lo crea si no existe)
    'x': create

Escritura
```python
import os

ingredientes = ["Cebolla","Tomate", "Aceite"]

archivo = open('datos.txt','w')

for elemento in ingredientes:
    archivo.write(elemento+'\n')

archivo.close()
```

Lectura
```python
import os

archivo = open('datos.txt','r')

for linea in archivo:
    print(linea)

archivo.close()

# Cebolla
# Tomate
# Aceite
```

### Beautiful Soup (Web Scrapping)

Beautiful Soup es una biblioteca de Python utilizada para extraer datos de documentos HTML y XML. Permite analizar el código fuente de una página web y extraer información específica de manera sencilla y eficiente. Beautiful Soup proporciona métodos y funciones para buscar, navegar y manipular la estructura del documento, facilitando la extracción de datos de manera programática.

Con Beautiful Soup, podemos buscar elementos HTML por etiquetas, clases, identificadores, atributos y más. También podemos acceder al contenido de los elementos, extraer atributos, realizar búsquedas más complejas y recorrer la estructura del documento de manera intuitiva. Es una herramienta muy útil para realizar tareas de Web Scraping, ya que nos permite obtener los datos que necesitamos de forma precisa y flexible.

Instalar libreria:

    pip install beautifulsoup4

```python
from bs4 import BeautifulSoup
import urllib.request

response = urllib.request.urlopen('https://es.wikipedia.org/wiki/Python')
html = response.read()  # hasta aqui solo leimos el contenido del texto plano

soup = BeautifulSoup(html, 'html.parser')
text = soup.get_text()

# Si solo queremos obtener los tags <a> o hipervinculos de la pagina:
links = soup.find_all('a')
```

## CREACION DE ENTORNOS VIRUALES

En adelante, veremos que es muy común trabajar con diferentes librerías ó módulos y uno de los problemas que se puede tener a la hora de manejar la instalaciones de paquetes es que si queremos tener varias versiones de la misma librería, para lo que deberíamos usar lo que se conoce como entornos virtuales.
Por ejemplo tenemos un proyecto en el que estamos trabajando con la versión de Python 2.2 y tenemos otro con la versión 3. Para este tipo de cosas es necesario tener dos entornos virtuales y es donde librerías como virtualenv.

Si se desea una versión especifica de Python, ésta debe estar instalada en la PC. Descargar desde la pagina oficial.
Se recomienda crear una carpeta de fácil acceso donde almacenaremos nuestros ambientes. Nos paramos en esta carpeta para ejecutar lo siguiente en la terminal.

1) Instalar virtualenv: pip install virtualenv
2) Verificamos la version: virtualenv --version
Opcional: podemos hacer un update de pip: python -m pip install --upgrade pip
3) Creamos el entorno: virtualenv env_name
Para especificar Python: virtualenv env_name --python=python=3.x
si esto da error, directamente hay que pasarle la ruta del ejecutable de python:
virtualenv --python="C:\Users\...\PythonXX\python.exe" env_name
4) Iniciamos el entorno virtual: .\env_name\Scripts\activate
5) Instalamos paquetes necesarios. Chequear que en la direccion en la terminal nos tiene que aparecer: (env_name) PS C:...
Esto nos asegura que estamos dentro del ambiente creado.
6) Instalamos todos los paquetes necesarios para nuestro entorno: pip install paquetes
- Al iniciar seguramente pida instalar ipykernel: pip install ipykernel
- Para chequear lista de paquetes instalados: pip freeze
- Para exportar los "requirements" o nombres de paquetes instalados: pip freeze > requirements.txt
- Para instalar requirements.txt: pip install -r requirements.txt
7) Finalmente desactivamos entorno virtual: deactivate


Recuerda que toda PC es diferente y puedes tener distintos errores, estos son solo algunos que pueden pasar...

1) Si al cargar una libreria: OSError:  Windows requires Developer Mode to be activated, or to run Python as an administrator, in order to create symlinks. In order to activate Developer Mode go to https://learn.microsoft.com/en-us/windows/apps/get-started/enable-your-device-for-development

Solución: Coloque Windows en modo desarrollador: Configuración → Actualizaciones y seguridad → Para desarrolladores → Usar funciones de desarrollador: seleccione “Modo desarrollador”

2) Al activar el entorno. Error: “La ejecución de scripts está deshabilitada en este sistema”

Solución: Para poder ver la política actual de ejecución abriremos PowerShell a nivel administrador. Para ello deberemos hacer clic en Inicio, escribir “Windows PowerShell”, hacer clic con el botón derecho encima de la aplicación y finalmente hacer clic en “Ejecutar como administrador”.

Una vez abierta la aplicación ejecutaremos el siguiente comando: Get-ExecutionPolicy -List

Esto nos muestra que la política de ejecución no está definida. Para poder corregir esto deberemos ejecutar el siguiente comando: Set-ExecutionPolicy RemoteSigned -Scope CurrentUser


## Pipenv

Pipenv es otro administrador de ambientes virtuales para Python. 

Veamos sus pasos de instalación:

1) Abrimos la consola/terminal/bash. 
En Windows podemos buscarla en el buscador de programas o utilizar la tecla de windows + R, donde escribiremos cmd y le daremos ejecutar.

2) Escribimos la instrucción ‘pip install pipenv’ en la consola, lo que hace que se installen pipenv y las dependencias necesarias en el directorio donde tenemos Python. IMPORTANTE: Recuerden que deben tener Python instalado y agregado al PATH. Esto se hace descargando el instalador de python.org y siguiendo las instrucciones (recurden chequear la opción Agregar Python al PATH)

3) Una vez instalado pipenv, nos dirigimos al directorio donde queremos crear el ambiente e utilizamos el comando pipenv shell. Este comando inicializa el ambiente contenido en ese directorio y, sino existe ninguno, lo crea.

Algunos comandos útiles son:

pipenv -h
pipenv install
pipenv lock
pipenv install --ignore-pipfile
pipenv graph
pipenv uninstall
pipenv uninstall --all