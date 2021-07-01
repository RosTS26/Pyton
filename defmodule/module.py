import sys, warnings
import os, platform, logging

print(sys.version_info)
if sys.version_info[0] < 3:
	warnings.warn('Для выполнения этой программы необходима как миниум Python 3-й версии!', RuntimeWarning)
else:
	print('Версия подходящая!')

if platform.platform().startswith('Windows'):
	logging_file = os.path.join(os.getenv('HOMEDRIVE'), os.getenv('HOMEPATH'), 'test.log')
else:
	logging_file = os.path.join(os.getenv('HOME'), 'test.log')

print('Сохраняем лог в', logging_file)

logging.basicConfig(
	level=logging.DEBUG,
	format='%(asctime)s : %(levelname)s : %(message)s',
	filename = logging_file,
	filemode = 'w',
)

logging.debug('Начало программы')
logging.info('Какие-то действия')
logging.warning('Программа умирает')