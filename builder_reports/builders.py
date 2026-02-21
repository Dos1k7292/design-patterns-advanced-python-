from report import Report


class TextReportBuilder:

    def __init__(self):

        self.report = Report()

    def set_header(self, header):

        self.report.header = header

    def add_section(self, name, content):

        self.report.sections.append((name, content))

    def set_footer(self, footer):

        self.report.footer = footer

    def set_style(self, style):

        self.report.style = style

    def get_report(self):

        return self.report


class HtmlReportBuilder(TextReportBuilder):

    pass
