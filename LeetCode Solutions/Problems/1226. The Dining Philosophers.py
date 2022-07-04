from threading import Lock
class DiningPhilosophers:
    def __init__(self):
        self.num_philosophers = 5
        self.forks = [Lock() for _ in range(self.num_philosophers)]
    # call the functions directly to execute, for example, eat()
    def wantsToEat(self,
                   philosopher: int,
                   pickLeftFork: 'Callable[[], None]',
                   pickRightFork: 'Callable[[], None]',
                   eat: 'Callable[[], None]',
                   putLeftFork: 'Callable[[], None]',
                   putRightFork: 'Callable[[], None]') -> None:
        right_fork = self.forks[philosopher]
        left_fork = self.forks[(philosopher + 1) % self.num_philosophers]
        if philosopher % 2 == 0:
            left_fork.acquire()
            pickLeftFork()
            right_fork.acquire()
            pickRightFork()
            eat()
            putLeftFork()
            left_fork.release()
            putRightFork()
            right_fork.release()
        else:
            right_fork.acquire()
            pickRightFork()
            left_fork.acquire()
            pickLeftFork()
            eat()
            putLeftFork()
            left_fork.release()
            putRightFork()
            right_fork.release()