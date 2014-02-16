import os
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
import time

print "\n\t\tWelcome to MP3 Tag Editor v0.01a"

path = raw_input('\tEnter the path :\t')

def get_files(path):
  for root,dirs,files in os.walk(path):
		print "\tTraversing through the directory\n"

	new_album = raw_input('\tEnter new album name\t: ')
	new_artist = raw_input('\tEnter new artist name\t: ')
	new_date = raw_input('\tEnter new date/year name\t : ')

	for filename in files:
		file_path = root+'/'+filename
		audio = MP3(str(file_path), ID3=EasyID3)		
		if not (new_album=="" and new_artist=="" and new_date==""):
			file_path = root+'/'+filename
			print "\tChanging \'" + filename + "\'s Album Name"
			audio["album"] = str(new_album)
			print "\tChanging \'" + filename + "\'s Artist Name"
			audio["artist"] = str(new_artist)
			print "\tChanging \'" + filename + "\'s Date/Year"
			audio["date"] = new_date
			audio.save()
			print "\tSuccessfully Tagged!\n\n"
			time.sleep(5)
				
def main():
	get_files(path)

if __name__ == '__main__':
	main()	
