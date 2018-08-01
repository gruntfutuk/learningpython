import queue
import threading

num_worker_threads = 10


def source(x=10):
    return [y for y in range(1, x)]


def do_work(item):
    print(f'I\'m working on {item}')


def worker():
    while True:
        item = q.get()
        if item is None:
            break
        do_work(item)
        q.task_done()


q = queue.Queue()
threads = []
for i in range(num_worker_threads):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)

for item in source():
    q.put(item)

# block until all tasks are done
q.join()

# stop workers
for i in range(num_worker_threads):
    q.put(None)
for t in threads:
    t.join()
