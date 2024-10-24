""" what is main thread ---> python interpreter starts
                              python interpreter request OS for for creating one thread
                              called as main thread"""


""" any process have at least one default thread called as main thread"""
# main thread is created by python virtual machine (interpreter)

import threading

print(threading.current_thread())   # we have only one thread so  it is main thread

# threads have id number , which can be vary

# if name thread then we use .name
print(threading.current_thread().name)
# if we want to print id the we use indentity

print(threading.current_thread().ident)

# if we want to check the status of thread we use is_aliva it return booleans value

print(threading.current_thread().is_alive())