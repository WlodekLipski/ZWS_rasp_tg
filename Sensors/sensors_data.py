import runner
import light
import time
import threading

thread = None
is_running = threading.Event()
sensors_state = runner.Runner()

class Sensors():
    """
    :param _state: Runner object
    :param _event: Event object
    """
    def __init__(self, _state, _event):
        self.state = _state
        self.is_running = _event
        self.thread = None
        self.reset_sensors()

    def reset_sensors():
        """
        Funciton initializing thread
        which will collect data from sensors
        based on provieded in '*.ini' file
        'sleep' timeout
        Timeout = [1,3600]
        """
        if self.thread is None:
            self.is_running.clear()
            self.state._set_sleep()
            self.thread = threading.Thread(target=self.state._launch, args=(self.is_running,))
            self.thread.start()
        else:
            """
            Relaunching sensors
            if new value in config file occur
            or the function was called directly
            """
            self.state._terminate(self.is_running)
            self.thread.join()
            self.thread = None
            self.state._set_sleep()
            return self.reset_sensors()

    def stop_sensors():
        """
        Function stopping sensors thread
        End of communication with sensors
        """
        self.state._terminate(self.is_running)
        self.thread.join()
        self.thread = None

reset_sensors()
time.sleep(10)

print(reset_sensors())

print('After terminate')
time.sleep(20)

stop_sensors();
print('After terminate')
sensors_state._print()
