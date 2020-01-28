from functools import wraps

def static_variables(**static_kw):
    def static_setter(func):
        for static_name, init_value in static_kw.items():
            setattr(func, static_name, init_value)
        return func
    return static_setter

@static_variables(cnt = 0)  # intialises variable
def calls_counter():
    calls_counter.cnt += 1  # takes advantage of initialised variable
    print(f'Called {calls_counter.cnt} times.')


calls_counter()
