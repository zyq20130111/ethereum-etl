#!/usr/bin/env python3
from concurrent.futures import ThreadPoolExecutor

from ethereumetl.exporters import CsvItemExporter
from ethereumetl.file_utils import get_file_handle

test_str = '0x' + ('0123456789' * 10000)

executor = ThreadPoolExecutor(max_workers=5)

output_file = get_file_handle('testconcurrency.csv', binary=True, create_parent_dirs=True)
exporter = CsvItemExporter(output_file)

for i in range(1, 10000):
    executor.submit(exporter.export_item, {
        'field1': 'test',
        'field2': test_str
    })

executor.shutdown(True)

output_file.close()

with open('testconcurrency.csv') as file:
    ind = 0
    for line in file:
        expected = 'test,' + test_str
        if ind != 0 and line != expected:
            ind += 1
            print(expected)
            print(line)
            raise ValueError
