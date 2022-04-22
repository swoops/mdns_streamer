# mdns_streamer
Stream console videos to responder over mdns

# This is not a vulnerability or exploit
Just fun with console codes

# Making your own videos
This is left as a fun exercise. I just used `man console_codes` and modified https://github.com/FFmpeg/FFmpeg/blob/master/doc/examples/filtering_video.c a lot. 

Video stream must be broken into hostnames that are at most 255 chars, followed by a dot, then 255 more chars. This makes for some fun trying to compress things. See the example video files for ideas, let me know if you improve upon them.
