# Tipo comportamiento

# Patrón Memento
# Necesitas guardar un estado de un objeto y poder restaurarlo

class Memento:
    def __init__(self, state): 
        self._state = state

    @property
    def state(self):
        return self._state

class Caretaker:
    def __init__(self):
        self._history = []
    
    def save(self, memento: Memento):
        self._history.append(memento)
    
    def undo(self):
        if len(self._history) > 1:
            self._history.pop()
            return self._history[-1]
        elif len(self._history) == 1:
            self._history.pop()
        return None

class Originator:
    def __init__(self):
        self._text = ""
    
    def append(self, new_text: str):
        self._text += new_text
    
    def save(self):
        return Memento(self._text)
    
    def restore(self, memento: Memento):
        if memento:
            self._text = memento.state
        else:
            self._text = ""

    @property
    def text(self):
        return self._text

editor = Originator()
historic = Caretaker()

editor.append("Hello, world!")
historic.save(editor.save())
editor.append(" I'm a student.")
historic.save(editor.save())
editor.append("I love Python.")
historic.save(editor.save())

print(f"Editor: {editor.text}")

editor.restore(historic.undo())
print(f"Editor: {editor.text}")

editor.restore(historic.undo())
print(f"Editor: {editor.text}")

editor.restore(historic.undo())
print(f"Editor: {editor.text}")







