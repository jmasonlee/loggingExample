import logging
import sys
from abc import ABC, abstractmethod


class SomeBaseClass(ABC):
    """
    I have no control over this class and I need it. It's just here to illustrate structure
    """
    log = logging.getLogger("")

    def start(self):
        self.run()

    @abstractmethod
    def run(self):
        pass



class DoTheThing(SomeBaseClass):
    """
        This is the main thing with all the logs
    """

    def run(self):
        # Other things happen here, but they aren't important
        self._double_check("We're really about to do this")

    def _double_check(self, msg: str) -> None:
        self._log_and_email(msg)
        if input("Are you sure? (y/n) ") == "y":
            return
        self._log_and_email("script has been stopped by the user")
        sys.exit(0)

    def _log_and_email(self, msg: str) -> None:
        self.log.info(msg)
        self.send_email_with_attachment(msg)

    def send_email_with_attachment(self, msg):
        pass
        
if __name__ == "__main__":
    DoTheThing().start()
