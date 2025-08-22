from abc import ABC, abstractmethod

class DocumentTemplate(ABC):
    @abstractmethod
    def add_header(self):
        pass

    @abstractmethod
    def add_content(self):
        pass    

    @abstractmethod
    def add_footer(self):
        pass

    def generate(self, file_name):
        with open(file_name, "w") as f:
            f.write(self.add_header())
            f.write("\n")
            f.write(self.add_content())
            f.write("\n")
            f.write(self.add_footer())
            f.write("\n")

        print(f"Documento {file_name} generado")

        
class SimpleDocument(DocumentTemplate):
    def add_header(self):
        return "Encabezado"
    
    def add_content(self):
        return "Contenido"
    
    def add_footer(self):
        return "Pie de página"

class MarkdownDocument(DocumentTemplate):
    def add_header(self):
        return "# Encabezado"
    
    def add_content(self):
        return "Contenido del **documento**"
    
    def add_footer(self):
        return "Pie de página"

class HTMLDocument(DocumentTemplate):
    def add_header(self):
        return "<h1>Encabezado</h1>"
    
    def add_content(self):
        return "<p>Contenido del documento</p>"
    
    def add_footer(self):
        return "<p>Pie de página</p>"


simple = SimpleDocument()
simple.generate("documento.txt")

markdown = MarkdownDocument()
markdown.generate("documento.md")

html = HTMLDocument()
html.generate("documento.html")

