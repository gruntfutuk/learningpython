import time

def check(sample, validation, cycles=500000):
    t = time.process_time()
    print('Testing: ', str(type(validation)))
    for _ in range(cycles):
        answer = sample.lower() in validation
    print('seconds: ', time.process_time() - t)


affset = {'y', 'yes', 'yeh', 'yup', 'ok', 'okay', 'agreed', 'please', 'yah'}
afflist = ['y', 'yes', 'yeh', 'yup', 'ok', 'okay', 'agreed', 'please', 'yah']
check('Yup', affset, 10000000)
check('Yup', afflist, 10000000)
