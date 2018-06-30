import json

from ethereumetl.executors.batch_work_executor import BatchWorkExecutor


class CallIpcCommand:
    def __init__(self, ipc_wrapper, batch_size, max_workers):
        self.ipc_wrapper = ipc_wrapper
        self.batch_work_executor = BatchWorkExecutor(batch_size, max_workers)

    def execute(self, input_iterable):
        self.batch_work_executor.execute(input_iterable, self._handle_ipc_response)

    def _handle_ipc_response(self, request_batch):
        response_batch = self.ipc_wrapper.make_request(json.dumps(request_batch))
