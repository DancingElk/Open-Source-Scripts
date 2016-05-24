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



keyword_list = ["start\": ","end\": ","timestamp\":"]
current_index = 0
final_output = ""
        
while (True):
        archive = f.readline()
        if (archive == ""):
                break

        for keyword in keyword_list:
                
                current_index=archive.find(keyword)
                
                if (current_index >= 0):
                        
                        unix_timestamp = archive[current_index+len(keyword):len(archive)-2]
                        unix_timestamp = unix_timestamp.replace(',','')

                        try:
                                junk = int(unix_timestamp)
                        except ValueError:
                                continue
                
                        new_timestamp = datetime.datetime.fromtimestamp(int(unix_timestamp)/1000).strftime('%Y-%m-%d %H:%M:%S')
                        archive = archive.replace(unix_timestamp,new_timestamp,1)
                        
                
                else:
                        continue

        final_output = final_output + archive
  
        
#print(final_output)
out_file.write(final_output)			
			
