import time

from .address import MemoryMap


class CpuState:
    def __init__(self):
        self.ram_size = MemoryMap.RAM.size
        self.write_to_stdout = True
        self.input_buffer = []
        self.output_storage = []
        self.epoch = time.time()
        self.syscall_buffer_size = 0
        self.cycle = 100000

    def verify(self):
        assert self.ram_size <= MemoryMap.RAM.size

    @classmethod
    def load(cls, buffer):
        pass

    def save(self):
        pass
