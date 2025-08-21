class CharacterMemento:
    def __init__(self, health, position):
        self._health = health
        self._position = position
    
    @property
    def state(self):
        return {
            "health": self._health,
            "position": self._position
        }

class Game:
    def __init__(self, name):
        self._name = name
        self._health = 100
        self._position = (0, 0)
    
    def move(self, x, y):
        self._position = (x, y)

    def receive_damage(self, damage):
        self._health -= damage

    def save(self):
        return CharacterMemento(self._health, self._position)

    def restore(self, memento: CharacterMemento):
        if memento:
            self._health = memento.state["health"]
            self._position = memento.state["position"]
        else:
            self._health = 100
            self._position = (0, 0)

    def __str__(self) -> str:
        return f"Game {self._name} has {self._health} health and is at position {self._position}"

class CharacterHistory:
    def __init__(self):
        self._history = []

    def save(self, memento: CharacterMemento):
        self._history.append(memento)
    
    def undo(self):
        if len(self._history) > 1:
            self._history.pop()
            return self._history[-1]
        elif len(self._history) == 1:
            self._history.pop()
        return None


character = Game("hero")
history = CharacterHistory()

print(f"Initial state: {character}")

history.save(character.save())
character.move(1, 1)
print(f"After move: {character}")
history.save(character.save())
character.receive_damage(20)
print(f"After damage: {character}")
history.save(character.save())
character.move(2, 2)
print(f"After move: {character}")
character.restore(history.undo())
print(f"After undo: {character}")


