class Report:

    def __init__(self):

        self.header = ""
        self.sections = []
        self.footer = ""
        self.style = None

    def export_text(self):

        print(self.header)

        for name, content in self.sections:

            print(name)
            print(content)

        print(self.footer)

    def export_html(self):

        print(f"<body style='background:{self.style.background}; font-family:{self.style.font}; font-size:{self.style.size}px'>")

        print(f"<h1>{self.header}</h1>")

        for name, content in self.sections:

            print(f"<h2>{name}</h2>")
            print(f"<p>{content}</p>")

        print(f"<footer>{self.footer}</footer>")
