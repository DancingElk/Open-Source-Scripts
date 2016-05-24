#python unix_timestamp to date time converter
#Seth Jensen 5/23/2016 the.anonymous.mustache@gmail.com
#tries to convert any field starting with a ": from unix timestamp to standard date time format 

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
current_index = 0

while (True):
        current_index=archive.find("\": ",current_index)
        
        if (current_index >= 0):
                timestamp_begin = archive.find(": ",current_index)
                timestamp_end = archive.find("\n",timestamp_begin)
                unix_timestamp = archive[timestamp_begin+1:timestamp_end-1]
                unix_timestamp = unix_timestamp.replace(',','')
                current_index = timestamp_end
                try:
                        new_timestamp = datetime.datetime.fromtimestamp(int(unix_timestamp)/1000).strftime('%Y-%m-%d %H:%M:%S')
                except ValueError:
                        current_index = timestamp_end
                        continue
                
                archive = archive.replace(unix_timestamp,new_timestamp)
                
        else:
                break

out_file.write(archive)      
#print(archive)
			
			
