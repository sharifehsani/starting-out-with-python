"""
- Author: Sharif Ehsani
- Date: August 2020
- https://github.com/sharifehsani

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

Get the number of videos in the project.
Open an output file.
For each video in the project:
Get the video’s running time.
Write the running time to the file.
Close the file.
"""

# functoin to start the program
def main():

	# Get the number of videos in the project.
	number_of_videos = int(input("How many videos do you want to enter: "))

	# Open an output file with 'w' access mode
	file_out = open('video_running_time.txt', 'w')

	# in a loop write the running time of the vidoes
	for count in range(1, number_of_videos + 1):
		# get the running time for each video from the user
		print("Enter the running time for video # ", count, ": ", end='')
		running_time = input()
		# write the running time to the file with new line at the end of each entry
		file_out.write(running_time + '\n')

	print("The times have been saved for all ", number_of_videos, "videos.")
	# close the file
	file_out.close()

# call the main function
main()



