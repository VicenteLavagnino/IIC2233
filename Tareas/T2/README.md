# Tarea 2: DCCruz vs Zombies :zombie::seedling::sunflower:


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
#### Ventanas: 39 pts (40%)
##### ✅ Ventana de Inicio
##### ✅ Ventana de Ranking	
##### ✅ Ventana principal
##### 🟠 Ventana de juego	
##### ✅ Ventana post-ronda
#### Mecánicas de juego: 46 pts (47%)			
##### ❌ Plantas
##### ❌ Zombies
##### ✅ Escenarios		
##### ✅ Fin de ronda	
##### ✅ Fin de juego	
#### Interacción con el usuario: 22 pts (23%)
##### 🟠 Clicks	
##### ❌ Animaciones
#### Cheatcodes: 8 pts (8%)
##### ❌✅🟠 Pausa
##### ❌✅🟠 S + U + N
##### ❌✅🟠 K + I + L
#### Archivos: 4 pts (4%)
##### ✅ Sprites
##### ✅ Parametros.py
##### ❌✅🟠 K + I + L
#### Bonus: 9 décimas máximo
##### ❌✅🟠 Crazy Cruz Dinámico
##### ❌✅🟠 Pala
##### ❌✅🟠 Drag and Drop Tienda
##### ❌✅🟠 Música juego

## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py```. Además se debe crear los siguientes archivos y directorios adicionales:
1. ```puntajes.txt``` en ```T2\```
2. ```sprites\``` en ```frontend\```
3. ```sonidos\``` en ```frontend\```
4. ```aparicion_zombies.py``` en ```T2\```


## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```PyQt5```: con sus distintos módulos para el funcionamiento de PyQt y QtDesigner
2. ```time```: para los intervalos de tiempo
3. ```random```: para aleatorizar factores
4. ```os```: para las rutas
5. ```sys```: para el cierre del programa

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```elementos_juego```: Contiene a todas las clases de objetos que interactuan en el juego
2. ```helpers```: contiene funciones que se usan durante el codigo reiteradas veces
3. ```parametros```: Para definir elementos del juego de manera ordenada
4. ```dccruz```: donde se conectan las señales e interacciones del juego
5. Además dentro de la carpeta ```backend``` está la los archivos de lógica para las distintas etapas del programa.
6. En la misma línea del punto anterior, existe ```frontend``` con todos los archivos ```.py``` para las ventanas del programa. 

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

hasta ahora no hay supuestos.


-------



**EXTRA:** si van a explicar qué hace específicamente un método, no lo coloquen en el README mismo. Pueden hacerlo directamente comentando el método en su archivo. Por ejemplo:

```python
class Corrector:

    def __init__(self):
          pass

    # Este método coloca un 6 en las tareas que recibe
    def corregir(self, tarea):
        tarea.nota  = 6
        return tarea
```

Si quieren ser más formales, pueden usar alguna convención de documentación. Google tiene la suya, Python tiene otra y hay muchas más. La de Python es la [PEP287, conocida como reST](https://www.python.org/dev/peps/pep-0287/). Lo más básico es documentar así:

```python
def funcion(argumento):
    """
    Mi función hace X con el argumento
    """
    return argumento_modificado
```
Lo importante es que expliquen qué hace la función y que si saben que alguna parte puede quedar complicada de entender o tienen alguna función mágica usen los comentarios/documentación para que el ayudante entienda sus intenciones.

## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1. \<https://github.com/IIC2233/VicenteLavagnino-iic2233-2022-2/tree/main/Actividades/AS3>: este hace \<distintas funciones de frontend> y está implementado en distintas partes del código, siendo previamente comentado en el mismo archivo.

2.\<https://pythonbasics.org/pyqt-qmessagebox/>: este hace \<un pop de una ventanilla de error en el caso de que el nombre no pueda ser utilizado> y está implementado en el archivo ```helpers```en la función pop_error().



## Descuentos
La guía de descuentos se encuentra [link](https://github.com/IIC2233/Syllabus/blob/master/Tareas/Descuentos.md).
