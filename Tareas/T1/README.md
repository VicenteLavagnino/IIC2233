# Tarea 1: DCCampeonato 🏃‍♂️🏆


Un buen ```README.md``` puede marcar una gran diferencia en la facilidad con la que corregimos una tarea, y consecuentemente cómo funciona su programa, por lo en general, entre más ordenado y limpio sea éste, mejor será 

Para nuestra suerte, GitHub soporta el formato [MarkDown](https://es.wikipedia.org/wiki/Markdown), el cual permite utilizar una amplia variedad de estilos de texto, tanto para resaltar cosas importantes como para separar ideas o poner código de manera ordenada ([pueden ver casi todas las funcionalidades que incluye aquí](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet))

Un buen ```README.md``` no tiene por que ser muy extenso tampoco, hay que ser **concisos** (a menos que lo consideren necesario) pero **tampoco pueden** faltar cosas. Lo importante es que sea claro y limpio 

**Dejar claro lo que NO pudieron implementar y lo que no funciona a la perfección. Esto puede sonar innecesario pero permite que el ayudante se enfoque en lo que sí podría subir su puntaje.**

## Consideraciones generales :octocat:

<Descripción de lo que hace y que **_no_** hace la tarea que entregaron junto
con detalles de último minuto y consideraciones como por ejemplo cambiar algo
en cierta línea del código o comentar una función>

### Cosas implementadas y no implementadas :white_check_mark: :x:

#### Programación Orientada a Objetos (18pts) (22%%)
##### ✅ Diagrama
##### ✅ Definición de clases, atributos, métodos y properties		
##### ✅ Relaciones entre clases
#### Preparación programa: 11 pts (7%)			
##### ✅ Creación de partidas
#### Entidades: 28 pts (19%)
##### ✅ Programón
##### ✅ Entrenador		
##### ✅ Liga	
##### ✅ Objetos		
#### Interacción Usuario-Programa 57 pts (38%)
#####  General	
#####  Menú de Inicio
##### ✅ Menú Entrenador
##### ✅ Menu Entrenamiento
##### 🟠 Simulación ronda campeonato
##### ✅ Ver estado del campeonato
##### 🟠 Menú crear objeto
##### 🟠 Menú utilizar objeto
##### ✅ Ver estado del entrenador
##### ✅ Robustez
#### Manejo de archivos: 12 pts (8%)
##### ✅ Archivos CSV
##### ✅ Parámetros
#### Bonus: 5 décimas
##### ❌ Mega Evolución
##### ❌ CSV dinámico

## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py```. 
Además se debe crear la carpeta ```datasets``` en ```T1``` la cual debe contener todos los archivos .csv

## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```random```: ```randint(), choice(), random()```
2. ```os```: ```path\```
3. ...

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1.```file_liga```: Contiene a ```Clase LigaProgramon```
2.```file_objeto```: Contiene a ```Clase Objeto```
3.```file_entrenador_programon```: Contiene a ```Clase Programon``` y ```Clase Entrenador```   
4.```menus principales``` Hecha para <correr los menus recurrentes del juego>
.```menus secundarios``` Hecha para <correr los menus derivados del menu entrenador>
6.```data``` Hecha para <abrir los archivos e instanciar su contenido>


## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. <para una mejor organización de archivos, guardé todos los archivos de tipo csv entregados en una carpeta llamada datasets >
2. <para una mayor comidad en el código, se definió la opción "Salir" con el número 0 para todo caso>
3. <Existe una carpeta llamada ```diagrama_de_clases``` donde se muestra el diagrama y su explicación correspondiente >


-------

## Descuentos
La guía de descuentos se encuentra [link](https://github.com/IIC2233/Syllabus/blob/master/Tareas/Descuentos.md).
