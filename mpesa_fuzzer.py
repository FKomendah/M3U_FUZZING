from sulley import *

s_initialize("MPESA")

s_static("APR-11-2019\r\n")
s_static("Phone Number: 0720991848\r\n")
s_static("From\t\tAmount\t\tDate\t\tID\t\r\n")

s_string("0716513473")
s_delim("\t\t")
s_string("2000")
s_delim("\t\t")
s_string("4/8/2019")
s_delim("\t\t")
s_string("hjxkjdlkahdwlkd")
s_delim("\r\n")
s_static("FELIX KOMENDAH\r\n")
s_static("Signed")

i=1
while s_mutate():
	fuzzfile=open("MPESA/mutant-"+str(i)+".mpesa","w")
	fuzzfile.write(s_render())
	fuzzfile.closed
	i+=1

print ("Done Fuzzing")