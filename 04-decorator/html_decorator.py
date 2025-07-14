"""
Este módulo demuestra el patrón de diseño Decorator.

El patrón Decorator permite añadir dinámicamente nuevas funcionalidades a los objetos
envolviéndolos en objetos "decoradores" especiales. En este ejemplo, comenzamos con un
objeto `SimpleText` y le añadimos dinámicamente formatos (negrita, cursiva, subrayado)
envolviéndolo con diferentes decoradores de formato.
"""

from abc import ABC, abstractmethod

# --- 1. La Interfaz del Componente ---
# Define la interfaz común tanto para los objetos que envolvemos como para los decoradores.

class Text(ABC):
    """
    La interfaz `Text` (Componente) declara un método común para todos los objetos,
    tanto los simples como los decorados. Esto asegura que el cliente pueda tratar
    a todos los objetos de la misma manera.
    """
    @abstractmethod
    def print(self) -> str:
        """
        Método abstracto que las clases concretas deben implementar para devolver el
        contenido del texto con su formato correspondiente.
        """
        pass

# --- 2. El Componente Concreto ---
# Es la clase base que vamos a decorar.

class SimpleText(Text):
    """
    `SimpleText` (Componente Concreto) es la clase de un objeto al que se le pueden
    añadir responsabilidades extra. Es el objeto núcleo o inicial.
    """
    def __init__(self, content: str):
        """Inicializa el texto simple con un contenido base."""
        self._content = content

    def print(self) -> str:
        """Devuelve el contenido de texto sin ningún formato."""
        return self._content

# --- 3. El Decorador Base ---
# Mantiene una referencia al objeto Componente y delega las llamadas a él.

class TextDecorator(Text):
    """
    El `TextDecorator` (Decorador Base) sigue la misma interfaz que los otros
    componentes. Su propósito es definir la interfaz de envoltura para todos
    los decoradores concretos. Mantiene una referencia al objeto que envuelve.
    """
    def __init__(self, text: Text):
        """Almacena una referencia al objeto de tipo Text que va a envolver."""
        self._text = text

    def print(self) -> str:
        """
        El decorador base simplemente delega la llamada al método print del objeto
        envuelto. El comportamiento extra se añade en los decoradores concretos.
        """
        return self._text.print()

# --- 4. Los Decoradores Concretos ---
# Estas clases añaden la funcionalidad extra (el "decorado").

class BoldTextDecorator(TextDecorator):
    """Añade formato de negrita (<b>) al texto envuelto."""
    def print(self) -> str:
        """
        Ejecuta el método `print` del objeto envuelto y añade las etiquetas <b>
        alrededor del resultado.
        """
        return f"<b>{self._text.print()}</b>"


class ItalicTextDecorator(TextDecorator):
    """Añade formato de cursiva (<i>) al texto envuelto."""
    def print(self) -> str:
        """
        Ejecuta el método `print` del objeto envuelto y añade las etiquetas <i>
        alrededor del resultado.
        """
        return f"<i>{self._text.print()}</i>"


class UnderlineTextDecorator(TextDecorator):
    """Añade formato de subrayado (<u>) al texto envuelto."""
    def print(self) -> str:
        """
        Ejecuta el método `print` del objeto envuelto y añade las etiquetas <u>
        alrededor del resultado.
        """
        return f"<u>{self._text.print()}</u>"


# --- Ejemplo de uso del Patrón Decorator ---
# Así es como se combinan los decoradores para añadir funcionalidades de forma flexible.

# 1. Creamos el objeto base, un texto simple.
simple_text = SimpleText("Hola, Mundo!")
print(f"Texto simple: {simple_text.print()}")

# 2. Lo envolvemos con el decorador de negrita.
#    BoldTextDecorator ahora contiene el objeto simple_text.
bold_text = BoldTextDecorator(simple_text)
print(f"Texto en negrita: {bold_text.print()}")

# 3. Podemos envolver un objeto ya decorado con otro decorador.
#    Aquí envolvemos el texto ya en negrita (`bold_text`) con el decorador de cursiva.
italic_bold_text = ItalicTextDecorator(bold_text)
print(f"Texto en negrita y cursiva: {italic_bold_text.print()}")

# 4. Y podemos seguir apilando decoradores en cualquier orden.
#    Ahora envolvemos el texto en negrita y cursiva con el de subrayado.
final_text = UnderlineTextDecorator(italic_bold_text)
print(f"Texto final (subrayado, cursiva y negrita): {final_text.print()}")

# Ejemplo de otra combinación
bold_underlined_text = UnderlineTextDecorator(BoldTextDecorator(SimpleText("Otro texto")))
print(f"Otra combinación: {bold_underlined_text.print()}")