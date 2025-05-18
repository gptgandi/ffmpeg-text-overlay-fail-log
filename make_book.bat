ffmpeg -i book_so.mp4 -vf "drawtext=text='ai: 안녕하세요 무엇을 도와드릴까요?':fontcolor=white:fontsize=48:x=(w-text_w)/2:y=h-100" -t 2.5 book_out.mp4
