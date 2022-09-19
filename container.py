from utils import FileHandler, LogQuery
from config import DATA_DIR

file_handler = FileHandler(DATA_DIR)
log_query = LogQuery()

data = file_handler.read_file('apache_logs.txt')


