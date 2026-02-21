from logger import LogLevel


class LogReader:

    def __init__(self, file):

        self.file = file

    def read(self, level=None):

        with open(self.file, "r") as f:

            for line in f:

                if level is None:

                    print(line, end="")

                else:

                    level_name = {

                        LogLevel.INFO: "INFO",
                        LogLevel.WARNING: "WARNING",
                        LogLevel.ERROR: "ERROR"

                    }[level]

                    if level_name in line:

                        print(line, end="")
