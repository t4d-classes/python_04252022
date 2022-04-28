import os


class Logger:

    def __init__(self, log_file_name, clear_log=False, log_name="App"):
        self.__log_name = log_name
        self.__log_file_name = log_file_name
        self.__clear_log = clear_log
        self.__is_configured = False

    def _config(self):
        try:
            if self.__clear_log and os.path.exists(self.__log_file_name):
                os.remove(self.__log_file_name)
        except BaseException:  # pylint: disable=broad-except
            pass

    def log(self, message, level="Log"):

        if not self.__is_configured:
            self._config()
            self.__is_configured = True

        try:
            with open(self.__log_file_name, "a", encoding="UTF-8") as log_file:
                log_file.write(f"{self.__log_name}:{level} > {message}\n")
        except BaseException:  # pylint: disable=broad-except
            pass

    def error(self, message):
        self.log(message, level="Error")

    def info(self, message):
        self.log(message, level="Info")
