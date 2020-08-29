"""
- Author: Sharif Ehsani
- Date: August 2020
- www.gitbuh.com/ehsanis

In the Spotlight:
Working with Files
Kevin is a freelance video producer who makes TV commercials for local businesses. When he
makes a commercial, he usually films several short videos. Later, he puts these short videos
together to make the final commercial. He has asked you to write the following two programs.
1. A program that allows him to enter the running time (in seconds) of each short video
in a project. The running times are saved to a file.
2. A program that reads the contents of the file, displays the running times, and then displays
the total running time of all the segments.
Here is the general algorithm for the first program, in pseudocode:

Here is the general algorithm for the second program:
Initialize an accumulator to 0.
Initialize a count variable to 0.
Open the input file.
For each line in the file:
Convert the line to a floating-point number. (This is the running time for a video.)
Add one to the count variable. (This keeps count of the number of videos.)
Display the running time for this video.
Add the running time to the accumulator.
Close the file.
Display the contents of the accumulator as the total running time.
"""

# function to start the program
def main():

	# initialize an accumlator to 0
	total = 0

	# Initialize a count variable to 0.
	counter = 0

	# open the input file in 'r' access mode
	file_in = open('video_running_time.txt', 'r')

	# For each line in the file:
	# Convert the line to a floating-point number. (This is the running time for a video.)

	for line in file_in:
		line_read = float(line)
		counter = counter + 1
		print("The running time for video #", counter, '=', line_read)
		total = total + line_read

	# close the file
	file_in.close()
	print("The total running time for", counter, "videos: ", total)


# call the main function
main()