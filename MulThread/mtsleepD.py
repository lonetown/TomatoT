from time import sleep, ctime
import threading

loops = [4, 2]


class ThreadFun(object):
    def __init__(self, func, args, name=''):
        self.name = name
        self.func = func
        self.args = args

    def __call__(self):
        self.func(*self.args)


def loop(nloop, nsec):
    print('Start loop', nloop, ' at:', ctime())
    sleep(nsec)
    print('loop', nloop, ' done at:', ctime())


def main():
    print('starting at:', ctime())
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = threading.Thread(target=ThreadFun(loop, (i, loops[i]), loop.__name__))
        threads.append(t)

    for i in nloops:
        threads[i].start()

    # for i in nloops:
    #     threads[i].join()
    print('all done at:', ctime())


if __name__ == '__main__':
    main()
