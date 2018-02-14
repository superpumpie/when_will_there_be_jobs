# -*- coding: utf-8 -*-
# tsj, feb 19
# quick and dirty script
# e.g. month loop is inefficient

import sys, re, os
reload(sys)

sys.setdefaultencoding('utf-8')


def main():
	
	path = '/Users/tsjuzek/Desktop/when_will_there_be_jobs/ll_emails/'
	
	month_list = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
	
	for month  in month_list:
		prof_counter = 0
		postdoc_counter = 0
		other_uni_counter = 0
		industry_counter = 0
		for filename in os.listdir(path):
			if "Summary" in filename:
				filename_elements = filename.split(" ")
				email_month = filename_elements[6]
				if email_month == month:
					input_file = open(path + filename, "r")
					for line in input_file:
						if "Jobs: " in line:
							if "Professor"  in line or "Lecturer" in line or "Instructor" in line or "Rank Open" in line or "Open Rank" in line or "Assistant"  in line or "Fellow" in line or "Chair" in line or "Director" in line or "Dean" in line:
								prof_counter += 1
							elif "Post Doc" in line or "Postdoctoral Fellow" in line or "Post-doctoral" in line or "Post-Doc" in line or "Postdoc" in line or "PostDoc" in line:
								postdoc_counter += 1
							elif "University" in line or "College" in line:
								other_uni_counter += 1
							else:
								industry_counter += 1
					input_file.close()
		
		print prof_counter, postdoc_counter, other_uni_counter, industry_counter
	

# boilerplate
main()