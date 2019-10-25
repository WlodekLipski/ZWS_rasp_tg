import runner
import light
import time
import threading

thread = None
is_running = threading.Event()
sensors_state = runner.Runner()

def reset_sensors():
    global thread
    if thread is None:
        is_running.clear()
        sensors_state._set_sleep()
        thread = threading.Thread(target=sensors_state._launch, args=(is_running,))
        thread.start()
        return 0
    else:
        sensors_state._terminate(is_running)
        thread.join()
        thread = None
        sensors_state._set_sleep()
        return reset_sensors()

def stop_sensors():
    global thread
    sensors_state._terminate(is_running)
    thread.join()
    thread = None

reset_sensors()
time.sleep(10)

print(reset_sensors())

print('After terminate')
time.sleep(20)

stop_sensors();
print('After terminate')
sensors_state._print()
