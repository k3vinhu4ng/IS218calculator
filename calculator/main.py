"""main scans and logs csv files and results"""
from tests.test_records import test_csv_write

print('Scanning files.')
test_csv_write()
print('Finished Scanning. All results are logged.')
