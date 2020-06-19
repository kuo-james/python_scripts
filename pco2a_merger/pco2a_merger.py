import re
import Tkinter
import tkFileDialog
import shutil
import os
from os import listdir
from os.path import isfile, join

root = Tkinter.Tk()
root.withdraw()
currdir = os.getcwd()
folder_path = tkFileDialog.askdirectory(parent=root, initialdir=currdir, title='Please select a directory')
#Folder where pco2a.log files are in
#folder_path = '/Users/jameskuo/Documents/Code/python_scripts/pco2a_merger/pco2a_d00011'

os.chdir(folder_path)
#Finds for files ending with .log and sorts the file names in ascending order
file_list = [f for f in listdir(folder_path) if isfile(join(folder_path, f)) and f.endswith('.log')]
file_list = sorted(file_list)

os.mkdir(folder_path+'/archive')
for file in file_list:
	print('Reading {}'.format(file))
	f = bytearray(open(file, 'rb').read())

	file_1 = open('merged_files.log', 'ab')
	file_1.write(f)
	file_1.close()

	#Moves read file to archive
	shutil.move(file, folder_path+'/archive/'+file)

	re_pattern = re.compile(b'\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2}\.\d{3} \D \D,.+?\r\n')
	re_result = re.findall(re_pattern, f)

	file_2 = open('data_only.log', 'ab')
	for data in re_result:
		file_2.write(data)
	file_2.close()
