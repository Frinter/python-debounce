import time

from debounce import debounce

class TestBasicDebounce(object):
    def run(self):
        self.calls = 0

        def func():
            self.calls += 1

        debounced_func = debounce(func, 0.05)

        debounced_func()
        debounced_func()
        debounced_func()
        debounced_func()

        time.sleep(0.1)

        assert self.calls == 1

class TestMultipleDebounce(object):
    def run(self):
        self.calls = 0

        def func():
            self.calls += 1

        debounced_func = debounce(func, 0.05)

        debounced_func()
        debounced_func()

        time.sleep(0.1)

        debounced_func()
        debounced_func()

        time.sleep(0.1)
        assert self.calls == 2

if __name__ == '__main__':
    TestBasicDebounce().run()
    TestMultipleDebounce().run()
