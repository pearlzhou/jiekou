# -*- coding: utf-8 -*-
# @Time    : 2019/3/11 14:08
# @Author  : zhouzz
# @FileName: getoptTest.py

import sys
import getopt

def main(argv):
	inputfile = ''
	outputfile = ''
	try:
		opts, args = getopt.getopt(argv,"hi:o:", ["ifile=", "ofile="])
		print opts
		print args
	except getopt.GetoptError:
		print('test.py -i <inputfile> -o <outputfile>')
		sys.exit(2)

	for opt, arg in opts:
		print opt
		if opt == '-h':
			print('test.py -i <inputfile> -o <outputfile>')
			sys.exit()
		elif opt in ("-i", "--ifile"):
			inputfile = arg
		elif opt in ("-o", "--ofile"):
			outputfile = arg
	print('输入的文件为：', inputfile)
	print('输出的文件为：', outputfile)

if __name__ == "__main__":
	main(sys.argv[1:])