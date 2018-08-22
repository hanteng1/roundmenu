import os
os.environ['PYTHON_EGG_CACHE'] = '/tmp'

import numpy as np
import csv
import argparse


#put all data together

#put all data together
def create_all_raw():
	data_dir = "/Users/tenghan/Dropbox/Rotary Watch/Study1-gesturePerformance/Study 1"
	all_date = []

	for subdir, dirs, files in os.walk(data_dir):
		for file in files:
			if '_summary' in file:
				print(os.path.join(subdir, file))
				single_file_data = open(os.path.join(subdir, file))
				user_index = subdir
				user_index = user_index[20:]
				csv_f = csv.reader(single_file_data)
				for row in csv_f:
					if row[0] != 'participant_id':
						# row.insert(0, user_index)
						all_date.append(row)

	with open('all_data_step_1.csv', 'w') as csvfile:
		writer = csv.writer(csvfile)
		writer.writerow(['participant_id', 'trial_number', 'block', 'motor_condition', 'visual_condition', 'id_current_selection', 'current_selection', 'id_target_selection', 'target_selection', 'target_angle', 'selection_success', 'num_overshoots', 'selection_time', 'first_rotation_time',	'total_rotation_angle',	'num_+15', 'num_-15'])
		for data in all_date:
		    writer.writerow(data)


if __name__ == "__main__":

	parser = argparse.ArgumentParser(description='data_dealer --step string')
	parser.add_argument('--step', action='store', dest='step', default='0' ,help='step to execute')

	args = parser.parse_args()

	if args.step == '0':
		print("expecting > 0")
	elif args.step == '1':
		create_all_raw()