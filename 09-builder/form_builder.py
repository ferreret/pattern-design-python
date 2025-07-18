from abc import ABC, abstractmethod


class HtmlForm:
    def __init__(self, action, method, fields):
        self.action = action
        self.method = method
        self.fields = fields

    def __str__(self):
        fields_html = "\n".join(self.fields)
        return f"""
        <form action="{self.action}" method="{self.method}">
            {fields_html}
        </form>
        """


class builder(ABC):
    @abstractmethod
    def set_action(self, action: str) -> "builder":
        pass

    @abstractmethod
    def set_method(self, method: str) -> "builder":
        pass

    @abstractmethod
    def add_text_input(self, name: str, placeholder: str) -> "builder":
        pass

    @abstractmethod
    def add_password_input(self, name: str, placeholder: str) -> "builder":
        pass

    @abstractmethod
    def add_submit_button(self, value: str) -> "builder":
        pass

    @abstractmethod
    def add_email_input(self, name: str, placeholder: str) -> "builder":
        pass

    @abstractmethod
    def build(self) -> HtmlForm:
        pass


class HtmlFormBuilder(builder):
    def __init__(self):
        self.reset()

    def reset(self):
        self.action = ""
        self.method = "POST"
        self.fields = []
        return self

    def set_action(self, action: str) -> "HtmlFormBuilder":
        self.action = action
        return self

    def set_method(self, method: str) -> "HtmlFormBuilder":
        self.method = method
        return self

    def add_text_input(self, name: str, placeholder: str) -> "HtmlFormBuilder":
        field = f'<input type="text" name="{name}" placeholder="{placeholder}">'
        self.fields.append(field)
        return self

    def add_password_input(self, name: str, placeholder: str) -> "HtmlFormBuilder":
        field = f'<input type="password" name="{name}" placeholder="{placeholder}">'
        self.fields.append(field)
        return self

    def add_submit_button(self, value: str) -> "HtmlFormBuilder":
        field = f'<input type="submit" value="{value}">'
        self.fields.append(field)
        return self

    def add_email_input(self, name: str, placeholder: str) -> "HtmlFormBuilder":
        field = f'<input type="email" name="{name}" placeholder="{placeholder}">'
        self.fields.append(field)
        return self

    def build(self) -> HtmlForm:
        form = HtmlForm(self.action, self.method, self.fields)
        self.reset()  # Reset the builder for future use
        return form


html_form_builder = HtmlFormBuilder()

login_form = (
    html_form_builder.set_action("/login")
    .set_method("POST")
    .add_text_input("username", "Enter your username")
    .add_password_input("password", "Enter your password")
    .add_submit_button("Login")
    .build()
)

print(login_form)
