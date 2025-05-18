ffmpeg -i mini_so.mp4 -vf "drawtext=text='cypher: 안녕?':fontcolor=white:fontsize=48:x=(w-text_w)/2:y=h-100" -t 2.5 mini_out.mp4
