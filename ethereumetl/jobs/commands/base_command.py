from ethereumetl.executors.batch_work_executor import BatchWorkExecutor
from ethereumetl.jobs.commands.composite_command import CompositeCommand


class BaseCommand:
    def __init__(
            self,
            batch_size,
            max_workers):
        self.batch_work_executor = BatchWorkExecutor(batch_size, max_workers)

    def execute(self, input_iterable):
        pass

    def pipe(self, other_command):
        return CompositeCommand(self, other_command)

