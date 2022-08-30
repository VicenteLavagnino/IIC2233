Autor: [Vicente Lavagnino](https://github.com/VicenteLavagnino)

# Tarea 0: Star Advanced 🚀🌌 


Un buen ```README.md``` puede marcar una gran diferencia en la facilidad con la que corregimos una tarea, y consecuentemente cómo funciona su programa, por lo en general, entre más ordenado y limpio sea éste, mejor será 

Para nuestra suerte, GitHub soporta el formato [MarkDown](https://es.wikipedia.org/wiki/Markdown), el cual permite utilizar una amplia variedad de estilos de texto, tanto para resaltar cosas importantes como para separar ideas o poner código de manera ordenada ([pueden ver casi todas las funcionalidades que incluye aquí](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet))

Un buen ```README.md``` no tiene por que ser muy extenso tampoco, hay que ser **concisos** (a menos que lo consideren necesario) pero **tampoco pueden** faltar cosas. Lo importante es que sea claro y limpio 

**Dejar claro lo que NO pudieron implementar y lo que no funciona a la perfección. Esto puede sonar innecesario pero permite que el ayudante se enfoque en lo que sí podría subir su puntaje.**

## Consideraciones generales :octocat:

<Descripción de lo que hace y que **_no_** hace la tarea que entregaron junto
con detalles de último minuto y consideraciones como por ejemplo cambiar algo
en cierta línea del código o comentar una función>

### Cosas implementadas y no implementadas :white_check_mark: :x:

Explicación: mantén el emoji correspondiente, de manera honesta, para cada item. Si quieres, también puedes agregarlos a los títulos:
- ❌ si **NO** completaste lo pedido
- ✅ si completaste **correctamente** lo pedido
- 🟠 si el item está **incompleto** o tiene algunos errores
#### Programación Orientada a Objetos (18pts) (22%%)
##### ✅ Menú de Inicio
##### ✅ Funcionalidades		
##### ✅ Puntajes
#### Flujo del Juego (30pts) (36%) 
##### ✅ Menú de Juego
##### ✅ Tablero		
##### ✅ Bestias	
##### ✅ Guardado de partida		
#### Término del Juego 14pts (17%)
##### ✅ Fin del juego	
##### ✅ Puntajes	
#### Genera: 15 pts (15%)
##### ✅ Menús
##### ✅ Parámetros
##### ✅ PEP-8

#### Bonus: 3 décimas
##### ❌

## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py```. Además se debe crear los siguientes archivos y directorios adicionales, de todos modos esto fueron incluidos en el último ```push``` para un correcto funcionamiento y comprensión del código :

1. ```ranking_T0-IIC2233.txt``` en ```ubicación```
2. carpeta ```partidas``` en carpeta ```T0```



## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```curses.ascii```: Contiene a ```isdigit()```
2. ```genericpath```: Contiene a ```isfile()```
3. ```os```: Hecha para navegar de mejor manera entre directorios y manejar archivos
4. ```random```: Contiene a ```randint()``` para aleatorizar la ubicación del las bestias
5. ```math```: Contiene a ```ceil()```

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```menus.py```: Contiene a ```menu_de_inicio()``` y las funciones para actualizar y visualizar el ranking.
2. ```juego.py```: Contiene a la clase ```Juego```, donde están todos los atributos y métodos necesarios para el operar el juego.


## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. <Utilicé el sistema de coordenadas como [X,Y] siendo ambos números enteros, declarando un print para orientar al usuario y facilitar la operación del código en lugar de utiliar el sistema [Letra, Número] > 
2. <El sistema de ranking presenta el orden en formato descendente según puntaje de la forma: ```nombre jugador```, ```puntaje obtenido```>



-------


## Referencias de código externo :book:

Para realizar mi tarea no saqué código de ningun sitio en específico, sin embargo utilicé ciertos códigos para inspirar la estructura:
1. \<https://stackoverflow.com/questions/23051062/open-files-in-rt-and-wt-modes>: este hace \<que pueda sobreescribir archivos.txt> y está implementado en el archivo <menus.py> en las líneas <121> y hace <que pueda sobre escribir>
2. \<https://class.mimir.io/my_grades/bb859e31-9c35-4d52-ab74-866efe3f2308>: esta es mi cuenta de Mimir que usé para Introducción a la programación y recurrí en algunas ocasiones a ella para \<recordar conceptos aprendidos>.



## Descuentos
La guía de descuentos se encuentra [link](https://github.com/IIC2233/Syllabus/blob/master/Tareas/Descuentos.md).
