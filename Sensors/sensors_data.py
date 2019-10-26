import time
import runner
import threading

thread = None
is_running = threading.Event()
sensors_state = runner.Runner(5)

class Sensors():
    """
    :param _state: Runner object
    :param _event: Event object
    """
    def __init__(self, _state, _event):
        self.thread = None
        self.runner = _state
        self.is_running = _event

    def reset_sensors(self, _sleep=5):
        """
        Funciton initializing thread
        which will collect data from sensors
        based on provieded in '*.ini' file
        'sleep' timeout
        Timeout = [1,3600]
        """
        if self.thread is None:
            self.is_running.clear()
            self.runner.set_sleep(_sleep)
            self.thread = threading.Thread(target=self.runner.launch, args=(self.is_running,))
            self.thread.start()
        else:
            """
            Relaunching sensors
            if new value in config file occur
            or the function was called directly
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

my_sensors = Sensors(sensors_state, is_running)
my_sensors.reset_sensors(2)
time.sleep(10)
my_sensors.reset_sensors(5)
time.sleep(10)
print('After terminate')
my_sensors.stop_sensors()
my_sensors.runner.get_sleep()
