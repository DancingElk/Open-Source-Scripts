#python unix_timestamp to date time converter
#Seth Jensen 5/23/2016 the.anonymous.mustache@gmail.com
#tries to convert a field from unix timestamp to standard date time format 

import sys
import urllib
import datetime
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("input_source", help="Source with dates to be converted, accepts files or urls")
parser.add_argument("output_file", help="Location of output, can only be file")
args = parser.parse_args()

try: 
        f = urllib.urlopen(args.input_source) #try it as a url first    
except ValueError:
        f = open(args.input_source, 'r') #try as a file second

out_file = open(args.output_file, 'w')

archive = f.read()

keywords = ["start\": ","end\": ","timestamp\":"]
keyword_ind = 0
current_index = 0

        
while (True):

        current_index=archive.find(keywords[keyword_ind],current_index,"\n")
        
        if (current_index >= 0):
                timestamp_end = archive.find("\n",current_index+3)
                unix_timestamp = archive[current_index+len(keywords[keyword_ind]):timestamp_end-1]
                unix_timestamp = unix_timestamp.replace(',','')

                try:
                        junk = int(unix_timestamp)
                except ValueError:
                        current_index = timestamp_end
                        continue
                
                new_timestamp = datetime.datetime.fromtimestamp(int(unix_timestamp)/1000).strftime('%Y-%m-%d %H:%M:%S')
                archive = archive.replace(unix_timestamp,new_timestamp,1)
                current_index = timestamp_end

                if (keyword_ind < len(keywords)-1):
                        keyword_ind += 1
                else:
                        keyword_ind = 0
                
        else:
                break
        

out_file.write(archive) 
print(archive)
			
			
