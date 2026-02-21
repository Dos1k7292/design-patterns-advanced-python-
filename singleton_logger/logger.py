import threading
import json
import datetime


class LogLevel:
    INFO = 1
    WARNING = 2
    ERROR = 3


class Logger:

    _instance = None
    _lock = threading.Lock()

    def __new__(cls, config_path="config.json"):

        if cls._instance is None:

            with cls._lock:

                if cls._instance is None:

                    cls._instance = super().__new__(cls)

                    cls._instance._initialize(config_path)

        return cls._instance

    def _initialize(self, config_path):

        self.file_lock = threading.Lock()

        with open(config_path, "r") as f:

            config = json.load(f)

        self.log_file = config["log_file"]

        level = config["log_level"]

        self.log_level = getattr(LogLevel, level)

    def set_log_level(self, level):

        self.log_level = level

    def log(self, message, level):

        if level < self.log_level:
            return

        time = datetime.datetime.now()

        level_name = {

            LogLevel.INFO: "INFO",
            LogLevel.WARNING: "WARNING",
            LogLevel.ERROR: "ERROR"

        }[level]

        log_message = f"{time} [{level_name}] {message}\n"

        with self.file_lock:

            with open(self.log_file, "a") as f:

                f.write(log_message)

        print(log_message, end="")
