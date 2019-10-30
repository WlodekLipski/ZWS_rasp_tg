import time
from . import runner
import threading

class Sensors():
    """
    :param _state: Runner object
    :param _event: Event object
    """
    def __init__(self):
        self.thread = None
        self.runner = runner.Runner(5)
        print('Runner type',self.runner)
        self.is_running = threading.Event()

    def reset_sensors(self, _sleep=5):
        """
        Funciton initialize the thread
        which will collect data from sensors
        based on provieded 'sleep' timeout
        Timeout = [1,3600]
        """

        # integer division
        _sleep //= 2
        if self.thread is None:
            self.is_running.clear()
            self.runner.set_sleep(_sleep)
            self.thread = threading.Thread(target=self.runner.launch, args=(self.is_running,))
            self.thread.start()
        else:
            """
            Relaunching sensors
            """
            self.runner.terminate(self.is_running)
            self.thread.join()
            self.thread = None
            self.runner.set_sleep()
            return self.reset_sensors(_sleep)

    def stop_sensors(self):
        """
        Function stopping sensors thread
        End of communication with sensors
        """
        self.runner.terminate(self.is_running)
        self.thread.join()
        self.thread = None
