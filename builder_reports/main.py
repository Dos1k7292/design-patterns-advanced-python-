from builders import TextReportBuilder, HtmlReportBuilder
from director import ReportDirector
from report_style import ReportStyle


style = ReportStyle("white", "Arial", 12)

director = ReportDirector()


text_builder = TextReportBuilder()

director.construct(text_builder, style)

text_report = text_builder.get_report()

print("\nTEXT REPORT\n")

text_report.export_text()


html_builder = HtmlReportBuilder()

director.construct(html_builder, style)

html_report = html_builder.get_report()

print("\nHTML REPORT\n")

html_report.export_html()
