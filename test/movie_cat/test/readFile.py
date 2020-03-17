import logging
from movie_cat.common.utils.fileUtil import *

print('path============'+getConfigPath())
logging.info('this is test............')
print(readConfig('application.properties'))

