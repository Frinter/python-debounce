import threading

def debounce(fn, delay):
    def debounced_function(*args, **kwargs):
        def do_call():
            fn(*args, **kwargs)

        if hasattr(debounced_function, 'timer'):
            debounced_function.timer.cancel()

        debounced_function.timer = threading.Timer(delay, do_call)
        debounced_function.timer.start()

    return debounced_function
