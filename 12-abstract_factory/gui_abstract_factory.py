from abc import ABC, abstractmethod


class Control(ABC):
    @abstractmethod
    def print(self, text: str) -> str:
        pass


class TextBoxHTMLControl(Control):
    def print(self, text: str):
        return f"<input type='text' placeholder='{text}' />"


class ButtonHTMLControl(Control):
    def print(self, text: str):
        return f"<button>{text}</button>"


class TextBoxXAMLControl(Control):
    def print(self, text: str):
        return f'<TextBox PlaceHolder="{text}" />'


class ButtonXAMLControl(Control):
    def print(self, text: str):
        return f'<Button Content="{text}" />'


class ControlFactory(ABC):
    @abstractmethod
    def create_textbox(self) -> Control:
        pass

    @abstractmethod
    def create_button(self) -> Control:
        pass


class HTMLControlFactory(ControlFactory):
    def create_textbox(self) -> Control:
        return TextBoxHTMLControl()

    def create_button(self) -> Control:
        return ButtonHTMLControl()


class XAMLControlFactory(ControlFactory):
    def create_textbox(self) -> Control:
        return TextBoxXAMLControl()

    def create_button(self) -> Control:
        return ButtonXAMLControl()


class App:
    def __init__(self, factory: ControlFactory):
        self.__factory = factory

    def create_page(self):
        content = ""
        content += self.__factory.create_textbox().print("Nombre")
        content += self.__factory.create_textbox().print("Email")
        content += self.__factory.create_button().print("Enviar")
        return content


app = App(HTMLControlFactory())
print(app.create_page())

app = App(XAMLControlFactory())
print(app.create_page())