import threading
from logger import Logger, LogLevel
from log_reader import LogReader


def worker(name):

    logger = Logger("config.json")

    logger.log(f"{name}: info message", LogLevel.INFO)

    logger.log(f"{name}: warning message", LogLevel.WARNING)

    logger.log(f"{name}: error message", LogLevel.ERROR)


threads = []

for i in range(5):

    t = threading.Thread(target=worker, args=(f"Thread-{i}",))

    threads.append(t)

    t.start()

for t in threads:
    t.join()


print("\nREAD ONLY ERRORS:\n")

reader = LogReader("app.log")

reader.read(LogLevel.ERROR)
