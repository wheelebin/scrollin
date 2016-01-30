import time
from datetime import datetime, date
import sys
import os

# Make sure to add spaces at the begining of the file and at end
# or else text will look weird while scrolling!
_dir = os.path.realpath(__file__).replace("scroll.py", "")

def letter_shuffle(word):
	# Swaps the position of letters creating a scroll effect 
	# when flushed and printed with a time interval, like in i3blocks.

	print(word.replace("_", " "))

	n = 0
	# Create list for easy position swaping
	word = list(str(word))

	# Store first letter in temp & then swap first letter with second letter,
	# store second letter in temp & then swap second letter with third letter 
	# and etc... try will break when list index is out of range
	for x in word:
		try:
			temp = word[n]
			word[n] = word[n+1]
			word[n+1] = temp
		except Exception:
			pass
		n += 1

	return "".join(word)

def parse_config():
	option = ""
	with open(_dir + 'config.txt', 'r') as f:
		for line in f.readlines():
			if "#date" in line:
				option = line

	return option

def _cache(option, _input=None):
	if option == 'r':
		# Get command to run from file
		with open(_dir+"cache.txt", 'r') as f:
			command = f.readlines()
			f.close()
		return command

	elif option == "w":
		# Overwrite old command with new_command
		with open(_dir+"cache.txt", 'w') as f:
			try:
				f.write(_input)
				f.close()
			except TypeError:
				_input = "".join(_input)
				f.write(_input)
				f.close()
	
def scroll_date(command):
	current_mon_day = str(date.today().strftime("%B_%d"))

	current_h = str(datetime.now().hour)
	current_min = str(datetime.now().minute)
	# Show 13:03 instead of 13:3
	if len(current_min) != 2:
		current_min = "0%s" % current_min
	current_time = "%s:%s" % (current_h, current_min)

	current_date = "_%s_/_%s_\n" % (current_mon_day, current_time)

	data = _cache('r')
	# Remove newline
	for x in range(0,len(data)):
		data[x] = data[x].rstrip('\n')
		n =+ 1
	
	if command == []:
		original_date = current_date
		scrolling_date = letter_shuffle(original_date.splitlines()[0])

		_cache('w', [original_date, scrolling_date])

		return scrolling_date

	elif data[0] != data[1]:
		data = _cache('r')

		data[1] = letter_shuffle(data[1].rstrip())

		_cache('w', [data[0], data[1]])

		return data[1]

	elif data[0] == data[1]:
		if data[0] == current_date:
			data[0] = current_date
			data[1] = current_date

			_cache('w', [data[0], data[1]])
		else:
			original_date = current_date
			scrolling_date = letter_shuffle(original_date.splitlines()[0])

			_cache('w', [original_date, scrolling_date])

			return scrolling_date

if __name__ == '__main__':
	option = parse_config()
	if "date" in option:
		command = _cache('r')
		#print(command)
		scroll_date(command)

	else:
		command = _cache('r')
		command[2] = "test3"
		_cache('w', command)

		# Run letter_shuffle and store as variable
		#new_command = letter_shuffle(command)
		#_cache('w', new_command)

		