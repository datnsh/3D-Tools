from PySide6.QtCore import QThread, Signal

class Worker(QThread):
    finished_with_result = Signal(object)
    failed = Signal(str)

    def __init__(self, task, *args, **kwargs):
        super().__init__()
        self.task = task
        self.args = args
        self.kwargs = kwargs

    def run(self):
        try:
            result = self.task(*self.args, **self.kwargs)
            self.finished_with_result.emit(result)
        except Exception as e:
            self.failed.emit(str(e))