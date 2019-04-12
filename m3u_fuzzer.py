from sulley import *

s_initialize("M3U")

s_static("#EXTM3U\r\n")
s_static("#EXTINF:123, Sample artist - Sample title\r\n")

s_static("http://")
s_string("www")
s_delim(".")
s_string("example")
s_delim(".")
s_string("com")
s_delim("/")
s_string("test")
s_delim(".")
s_static("m3u")

i=1
while s_mutate():
	fuzzfile=open("M3U_HTTP/mutant-"+str(i)+".m3u","w")
	fuzzfile.write(s_render())
	fuzzfile.closed
	i+=1
print ("Done Fuzzing")