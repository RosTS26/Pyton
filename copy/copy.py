import os # Импортируем модуль операционной системы
import time # Втроенный модуль времени

sor = ['D:\\Python', '"D:\\С ИНТЕРНЕТА"'] # Указываем переменной пути того, что нужно скопировать (Делаем из этого список)

target_dir = 'D:\\Backup' # Указываем куда будет перемещена копия source
z = '.iso'

# Указываем место, дату, время и формат для нашего файла
target = target_dir,os.sep, time.strftime('%Y %m %d %H:%M:%S') , z
# 
#  Используем команду "zip" для помещения файлов в zip-архив
iso_command = 'iso -qr {} {}'.format(target, ' '.join(sor))

print(iso_command)
if os.system(iso_command) == 0:
	print('Резервная копия успешно создана в:', target)
else:
	print('ОШИБКА!')
