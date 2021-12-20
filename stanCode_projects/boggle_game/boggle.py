"""
File: boggle.py
Name:
----------------------------------------
TODO:
"""

import time
import random

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'

ro = 0
match = 0
r = 5
c = 5
count = 0

result = ''
sub_s = ''
voc_result = []
names = {}

def main():
	"""
	TODO:
	"""
	start = time.time()
	####################
	#                  #
	#       TODO:      #
	#                  #
	####################
	file = read_dictionary(FILE)
	voc_lst = input_letter()
	find_voc([], voc_lst)
	print(f'There are {count} words in total')
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def read_dictionary(filename):
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	global names
	with open(filename, 'r') as f:
		for name in f:
			name = name.strip()
			names[name] = 0
	return names


def input_letter():
	global ro
	final_lst = []
	for i in range(0, 4):
		row = input(str(i+1) + " row of letters: ")
		row = row.lower()
		final_lst.append([])
		# print(row)
		r_lst = list(row)
		if len(r_lst) < 7 or len(row) > 8:
			print("Illegal input")
			break
		elif len(r_lst) == 8:
			if r_lst[len(r_lst)-1] != ' ':
				print("Illegal input")
				break
		else:
			for ro in r_lst:
				if ro != ' ':
					final_lst[i].append(ro)
	return final_lst


def find_voc(voc, voc_lst):
	global result
	for row in range(0, 4, 1):
		for column in range(0, 4, 1):
			ind = [row, column]
			find_helper(voc, voc_lst, [], ind)  # helper的參數可直接增加一個參數放ind，這樣就不用擔心上面的清空問題
	return voc


def find_helper(voc, voc_lst, real_voc, ind):
	global r, c, result, voc_result, sub_s, count
	# BASE CASE
	if len(voc) >= 4 and result in names:  # 存在於字典且長度大於4之文字
		print(f'Found: ...{result}')
		count += 1
		voc_result.append(result)
		del names[result]  # 於字典刪除已找到的文字，為之後比對更長文字組合使用 ex:room & roomy
		find_helper(voc, voc_lst, real_voc, ind)

	# Not BASE CASE
	else:
		if len(voc) == 2:
			sub_voc = []
			for i in voc:  # 位置轉換為文字
				for j in i:
					if r == 5:
						r = j
					else:
						c = j
				sub_voc.append(voc_lst[r][c])
				r = 5
				c = 5
				sub_s = ''.join(real_voc)
				if has_prefix(sub_s) is False:
					pass
		# 定義每次的起始index
		if not voc:  # if voc is None
			row = ind[0]
			col = ind[1]
		else:
			row = voc[-1][0]
			col = voc[-1][1]
		for row_change in range(-1, 2, 1):  # 字串可以串每個位置的+-1
			# row = voc[len(voc) - 1][0]
			if 0 <= row + row_change < 4:
				# row += row_change
				for column_change in range(-1, 2, 1):  # 字串可以串每個位置的+-1
					# column = voc[len(voc) - 1][1]
					if 0 <= col + column_change < 4:
						x = row + row_change
						y = col + column_change
						next_index = (x, y)
						if next_index not in voc:  # 已在排序組合之位置不使用
							# ***choose***
							voc.append(next_index)  # 串上新位置
							real_voc = []
							for i in voc:  # 位置轉換為文字
								for j in i:
									if r == 5:
										r = j
									else:
										c = j
								real_voc.append(voc_lst[r][c])
								r = 5
								c = 5
								result = ''.join(real_voc)

							# ***explore***
							find_helper(voc, voc_lst, real_voc, ind)  # 找下一格字

							# ***un-choose***
							voc.pop()  # 刪除已不需要之位置
							result = result[:-1]  # 刪除不需要之文字


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for name in names:
		if str(name).startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
