from abc import ABC, abstractmethod

class IWorker(ABC):
    @abstractmethod
    def work(self):
        pass


class Worker(IWorker):
    def work(self):
        print("I'm working!!")


class SuperWorker(IWorker):
    def work(self):
        print("I work very hard!!!")


class Manager:
    def __init__(self):
        self.worker = None

    def set_worker(self, worker: IWorker):
        assert isinstance(worker, IWorker), '`worker` must implement IWorker'
        self.worker = worker

    def manage(self):
        if self.worker is not None:
            self.worker.work()


# Тест на програмата
worker = Worker()
manager = Manager()
manager.set_worker(worker)
manager.manage()

super_worker = SuperWorker()
manager.set_worker(super_worker)
manager.manage()

