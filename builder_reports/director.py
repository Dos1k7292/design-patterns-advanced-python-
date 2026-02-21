class ReportDirector:

    def construct(self, builder, style):

        builder.set_style(style)

        builder.set_header("Sales Report")

        builder.add_section("Section 1", "Content 1")

        builder.add_section("Section 2", "Content 2")

        builder.set_footer("End")
