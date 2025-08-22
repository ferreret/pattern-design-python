# 📚 Guía de Patrones de Diseño en Python 🐍

¡Bienvenido! Este repositorio es una colección práctica de patrones de diseño implementados en Python. Sirve como una guía de referencia rápida y un recurso de aprendizaje para desarrolladores que buscan aplicar soluciones probadas a problemas comunes en el diseño de software.

## 🤔 ¿Qué son los Patrones de Diseño?

Los patrones de diseño son soluciones reutilizables y estandarizadas a problemas que ocurren frecuentemente en el diseño de software. No son código final, sino plantillas o descripciones sobre cómo abordar un problema, que pueden ser adaptadas a múltiples situaciones. Utilizarlos ayuda a crear software más flexible, mantenible y robusto.

## 📋 Índice de Patrones

A continuación, se muestra una tabla con todos los patrones incluidos en este proyecto. Haz clic en el enlace para ver la implementación de ejemplo.

| # | Patrón de Diseño | Enlace al Código |
|---|---|---|
| 1 | POO (Conceptos Fundamentales) | [Ver Código](./01-poo/) |
| 2 | Singleton | [Ver Código](./02-singleton/) |
| 3 | Strategy | [Ver Código](./03-strategy/) |
| 4 | Decorator | [Ver Código](./04-decorator/) |
| 5 | Observer | [Ver Código](./05-observer/) |
| 6 | Dependency Injection | [Ver Código](./06-dependency_injection/) |
| 7 | Factory Method | [Ver Código](./07-factory/) |
| 8 | State | [Ver Código](./08-state/) |
| 9 | Builder | [Ver Código](./09-builder/) |
| 10 | Bridge | [Ver Código](./10-bridge/) |
| 11 | Iterator | [Ver Código](./11-iterator/) |
| 12 | Abstract Factory | [Ver Código](./12-abstract_factory/) |
| 13 | Prototype | [Ver Código](./13-prototype/) |
| 14 | Proxy | [Ver Código](./14-proxy/) |
| 15 | Adapter | [Ver Código](./15-adapter/) |
| 16 | Composite | [Ver Código](./16-composite/) |
| 17 | Flyweight | [Ver Código](./17-flyweight/) |
| 18 | Facade | [Ver Código](./18-facade/) |
| 19 | Chain of Responsibility | [Ver Código](./19-chain-of-responsibility/) |
| 20 | Command | [Ver Código](./20-command/) |
| 21 | Mediator | [Ver Código](./21-mediator/) |
| 22 | Memento | [Ver Código](./22-memento/) |
| 23 | Template Method | [Ver Código](./23-template_method/) |
| 24 | Visitor | [Ver Código](./24-visitor/) |

---

## 🛠️ Catálogo Detallado de Patrones

Aquí encontrarás una explicación detallada y un ejemplo de uso para cada patrón.

### 1. POO (Programación Orientada a Objetos)
*   **📜 Explicación:** Aunque no es un patrón de diseño en sí, la POO es el paradigma sobre el que se construyen muchos patrones. Se basa en conceptos como la herencia, el encapsulamiento, el polimorfismo y la abstracción para estructurar el código en objetos que interactúan entre sí.
*   **💡 Ejemplo de Uso:**
    > Se utiliza para modelar entidades del mundo real. Por ejemplo, en un sistema de gestión de una biblioteca, podrías tener clases como `Libro`, `Usuario` y `Préstamo`, cada una con sus propios datos (atributos) y comportamientos (métodos).

### 2. Singleton
*   **📜 Explicación:** Garantiza que una clase solo tenga una única instancia y proporciona un punto de acceso global a ella. Es ideal para gestionar recursos compartidos.
*   **💡 Ejemplo de Uso:**
    > En una aplicación, necesitas gestionar la configuración (tema, idioma, etc.) de forma centralizada. Un Singleton asegura que solo exista un objeto de configuración, evitando inconsistencias y permitiendo que cualquier parte del sistema acceda a los mismos ajustes.

### 3. Strategy
*   **📜 Explicación:** Permite definir una familia de algoritmos, encapsular cada uno de ellos y hacerlos intercambiables. El algoritmo que se usa puede variar independientemente de los clientes que lo utilizan.
*   **💡 Ejemplo de Uso:**
    > Un sistema de comercio electrónico necesita calcular los impuestos de una venta según el país. En lugar de usar un `if/else` gigante, se crea una estrategia para cada país (`TaxStrategyUSA`, `TaxStrategySpain`, etc.). El sistema elige y utiliza la estrategia correcta en tiempo de ejecución sin cambiar el código principal de la venta.

### 4. Decorator
*   **📜 Explicación:** Permite añadir nuevas funcionalidades a un objeto de forma dinámica sin alterar su clase. Envuelve el objeto original en otro que le añade la nueva responsabilidad.
*   **💡 Ejemplo de Uso:**
    > Tienes una cafetería virtual. Un café simple es el objeto base. Puedes "decorarlo" con `LecheDecorator`, luego con `AzucarDecorator` y finalmente con `CremaDecorator`. Cada decorador añade coste y modifica la descripción del producto final sin necesidad de crear una clase para cada combinación posible.

### 5. Observer
*   **📜 Explicación:** Define una dependencia uno-a-muchos entre objetos. Cuando un objeto (el "sujeto") cambia de estado, todos sus dependientes (los "observadores") son notificados y actualizados automáticamente.
*   **💡 Ejemplo de Uso:**
    > En una hoja de cálculo, una celda es el "sujeto" y varias gráficas son los "observadores". Cuando el valor de la celda cambia, todas las gráficas que dependen de ella se actualizan automáticamente para reflejar el nuevo dato.

### 6. Dependency Injection
*   **📜 Explicación:** Es un patrón en el que un objeto recibe sus dependencias (otros objetos con los que trabaja) desde una fuente externa, en lugar de crearlas internamente. Esto promueve el bajo acoplamiento y facilita las pruebas.
*   **💡 Ejemplo de Uso:**
    > Un `ServicioDeEmail` necesita un `ProveedorDeEmail` (como Gmail o Outlook) para enviar correos. En lugar de que el servicio cree una instancia de `GmailProvider` dentro de sí mismo, se la "inyectas" desde fuera. Así, puedes cambiar fácilmente a `OutlookProvider` o usar un proveedor falso para las pruebas.

### 7. Factory Method
*   **📜 Explicación:** Define una interfaz para crear un objeto, pero deja que sean las subclases quienes decidan qué clase concreta instanciar. Permite que una clase delegue la instanciación a sus subclases.
*   **💡 Ejemplo de Uso:**
    > Una aplicación de logística necesita crear objetos de transporte. La clase principal `Logistica` tiene un método `crearTransporte()`. Las subclases `LogisticaMaritima` y `LogisticaTerrestre` implementan este método para devolver un objeto `Barco` o `Camion`, respectivamente.

### 8. State
*   **📜 Explicación:** Permite que un objeto altere su comportamiento cuando su estado interno cambia. El objeto parece cambiar de clase.
*   **💡 Ejemplo de Uso:**
    > El estado de un pedido en un e-commerce (`Procesando`, `Enviado`, `Entregado`). El objeto `Pedido` se comporta de manera diferente en cada estado. Por ejemplo, la acción `cancelar()` solo es posible en el estado `Procesando`, pero no en `Entregado`.

### 9. Builder
*   **📜 Explicación:** Separa la construcción de un objeto complejo de su representación, de modo que el mismo proceso de construcción pueda crear diferentes representaciones. Es ideal para objetos con muchos parámetros de configuración.
*   **💡 Ejemplo de Uso:**
    > Para crear un formulario de registro de usuario con muchos campos opcionales (nombre, email, teléfono, dirección, foto...). Un `FormBuilder` permite añadir cada campo paso a paso (`.conNombre("Juan").conEmail("...")`) y al final llamar a `.construir()` para obtener el objeto `Formulario` completo y validado.

### 10. Bridge
*   **📜 Explicación:** Desacopla una abstracción de su implementación, de modo que ambas puedan evolucionar de forma independiente. Es como construir un puente entre dos jerarquías de clases.
*   **💡 Ejemplo de Uso:**
    > Tienes diferentes formas (`Circulo`, `Cuadrado`) y diferentes formas de dibujarlas (`DibujoVectorial`, `DibujoRasterizado`). Con Bridge, evitas crear `CirculoVectorial`, `CirculoRasterizado`, etc. En su lugar, una `Forma` tiene una referencia a un `Dibujo`, y puedes combinar cualquier forma con cualquier tipo de dibujo.

### 11. Iterator
*   **📜 Explicación:** Proporciona una forma de acceder a los elementos de una colección de objetos secuencialmente sin necesidad de exponer su representación interna.
*   **💡 Ejemplo de Uso:**
    > Quieres recorrer una lista de tareas pendientes. El iterador te da los métodos `siguiente()` y `tieneSiguiente()`, permitiéndote procesar cada tarea una por una, sin importar si la colección subyacente es una lista, un array o una estructura de datos personalizada.

### 12. Abstract Factory
*   **📜 Explicación:** Proporciona una interfaz para crear familias de objetos relacionados o dependientes sin especificar sus clases concretas. Es una "fábrica de fábricas".
*   **💡 Ejemplo de Uso:**
    > Una aplicación que puede cambiar de tema (Claro/Oscuro). Una `GUIFactory` abstracta define métodos como `crearBoton()` y `crearVentana()`. Tienes dos fábricas concretas: `TemaClaroFactory` y `TemaOscuroFactory`. Al elegir un tema, usas la fábrica correspondiente para crear todos los componentes de la UI, asegurando que todos tengan un estilo consistente.

### 13. Prototype
*   **📜 Explicación:** Permite crear nuevos objetos duplicando una instancia existente (un "prototipo"). Es útil cuando la creación de un objeto es costosa.
*   **💡 Ejemplo de Uso:**
    > En un juego, tienes un enemigo base con mucha configuración (vida, ataque, modelo 3D). En lugar de crear cada nuevo enemigo desde cero, clonas el prototipo del enemigo y solo modificas las pequeñas diferencias (por ejemplo, su posición en el mapa).

### 14. Proxy
*   **📜 Explicación:** Proporciona un sustituto o intermediario para otro objeto, con el fin de controlar el acceso a este.
*   **💡 Ejemplo de Uso:**
    > Un proxy de imagen. Tienes una imagen de alta resolución que tarda en cargar. El proxy muestra inicialmente una imagen de baja calidad o un icono de carga. Mientras tanto, carga la imagen real en segundo plano y solo la muestra cuando está completamente disponible, mejorando la experiencia del usuario.

### 15. Adapter
*   **📜 Explicación:** Permite que interfaces incompatibles trabajen juntas. Actúa como un traductor entre dos objetos.
*   **💡 Ejemplo de Uso:**
    > Tu aplicación usa un sistema de notificaciones que espera un método `enviarMensaje()`. Contratas un nuevo proveedor de notificaciones cuya clase tiene un método llamado `mandarNotificacionUrgente()`. Creas un `Adaptador` que envuelve al nuevo proveedor y expone el método `enviarMensaje()`, traduciendo la llamada internamente.

### 16. Composite
*   **📜 Explicación:** Compone objetos en estructuras de árbol para representar jerarquías de parte-todo. Permite a los clientes tratar a los objetos individuales y a las composiciones de objetos de manera uniforme.
*   **💡 Ejemplo de Uso:**
    > Un sistema de archivos. Tanto un `Archivo` (objeto individual) como una `Carpeta` (composición de archivos y otras carpetas) pueden ser tratados de la misma forma. Puedes ejecutar la operación `calcularTamaño()` sobre un archivo o sobre una carpeta entera, y funcionará de manera transparente.

### 17. Flyweight
*   **📜 Explicación:** Minimiza el uso de memoria al compartir la mayor cantidad de datos posible con otros objetos similares. Es ideal para sistemas con una gran cantidad de objetos.
*   **💡 Ejemplo de Uso:**
    > En un videojuego de estrategia, tienes miles de árboles en el mapa. En lugar de que cada objeto `Arbol` almacene su modelo 3D, textura y tipo (estado intrínseco), estos datos se guardan en un objeto `TipoDeArbol` compartido (el Flyweight). Cada instancia de `Arbol` solo almacena su posición y tamaño (estado extrínseco).

### 18. Facade
*   **📜 Explicación:** Proporciona una interfaz unificada y simplificada para un conjunto de interfaces en un subsistema. Oculta la complejidad del sistema y facilita su uso.
*   **💡 Ejemplo de Uso:**
    > Para realizar una copia de seguridad de un archivo, necesitas leerlo, comprimirlo, encriptarlo y enviarlo a un servidor. Una `BackupFacade` ofrece un único método `hacerBackup("mi_archivo.txt")` que orquesta todas esas operaciones complejas internamente.

### 19. Chain of Responsibility
*   **📜 Explicación:** Pasa una solicitud a lo largo de una cadena de manejadores. Al recibir una solicitud, cada manejador decide si la procesa o si la pasa al siguiente manejador en la cadena.
*   **💡 Ejemplo de Uso:**
    > Un sistema de soporte técnico. Un ticket de cliente pasa primero por el Nivel 1 (preguntas frecuentes). Si no pueden resolverlo, lo pasan al Nivel 2 (soporte técnico general). Si sigue sin resolverse, pasa al Nivel 3 (ingenieros especializados).

### 20. Command
*   **📜 Explicación:** Encapsula una solicitud como un objeto, permitiendo parametrizar clientes con diferentes solicitudes, encolar o registrar solicitudes y soportar operaciones que se pueden deshacer.
*   **💡 Ejemplo de Uso:**
    > En un editor de texto, las acciones "Copiar", "Pegar" y "Cortar" se implementan como objetos `Command`. Cuando el usuario hace clic en un botón, se ejecuta el comando correspondiente. Esto permite añadir fácilmente las acciones a menús, barras de herramientas y guardar un historial para la funcionalidad "Deshacer".

### 21. Mediator
*   **📜 Explicación:** Define un objeto que encapsula cómo un conjunto de objetos interactúan. Promueve un bajo acoplamiento al evitar que los objetos se refieran entre sí explícitamente.
*   **💡 Ejemplo de Uso:**
    > En una sala de chat, los `Usuario`s no se envían mensajes directamente entre sí. Envían su mensaje al `ChatMediator` (la sala de chat), y este se encarga de reenviarlo a todos los demás usuarios. Ningún usuario necesita conocer a los demás.

### 22. Memento
*   **📜 Explicación:** Permite capturar y externalizar el estado interno de un objeto para que pueda ser restaurado más tarde, sin violar el encapsulamiento.
*   **💡 Ejemplo de Uso:**
    > La funcionalidad de "Guardar Partida" en un videojuego. Al guardar, el objeto `Juego` crea un `Memento` que contiene su estado actual (vida del jugador, posición, inventario). Para cargar la partida, el objeto `Juego` restaura su estado a partir del `Memento`.

### 23. Template Method
*   **📜 Explicación:** Define el esqueleto de un algoritmo en una operación, delegando algunos pasos a las subclases. Permite que las subclases redefinan ciertos pasos de un algoritmo sin cambiar su estructura.
*   **💡 Ejemplo de Uso:**
    > Un proceso para generar un informe. La clase base `GeneradorDeInforme` define los pasos: `recopilarDatos()`, `procesarDatos()` y `formatearSalida()`. Los pasos de recopilación y formato son abstractos y deben ser implementados por subclases como `InformePDF` o `InformeCSV`, pero el esqueleto del algoritmo permanece igual.

### 24. Visitor
*   **📜 Explicación:** Permite añadir nuevas operaciones a una jerarquía de clases sin modificar las clases. La nueva lógica se encapsula en un objeto "visitante".
*   **💡 Ejemplo de Uso:**
    > Tienes una estructura de productos (`Libro`, `Disco`, `Electronica`). Quieres calcular el coste de envío, que depende del tipo de producto. Creas un `VisitorDeEnvio` que tiene un método para cada tipo (`visitarLibro`, `visitarDisco`). Al "aceptar" al visitante, cada producto llama al método correspondiente del visitante, permitiendo calcular el total sin modificar las clases de los productos.
