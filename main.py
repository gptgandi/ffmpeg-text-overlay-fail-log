
import openai
import os
import subprocess

# 1. API KEY
client = openai.OpenAI(api_key="")  # 여기에 실제 API 키 입력

# 2. 입력 텍스트
prompt_text = """
cypher: 안녕?
ai: 안녕하세요. 무엇을 도와드릴까요?
"""

# 3. SRT 변환 요청
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Convert the following dialogue to proper SRT format with timestamps."},
        {"role": "user", "content": prompt_text}
    ]
)
srt_output = response.choices[0].message.content

# 4. SRT 저장
with open("subtitle.srt", "w", encoding="utf-8") as f:
    f.write(srt_output)

# 5. 캐릭터별 영상 리스트 생성
video_list = []
for line in prompt_text.strip().split("\n"):
    if "ai:" in line.lower():
        video_list.append("file 'book_so.mp4'")
    elif "cypher:" in line.lower():
        video_list.append("file 'mini_so.mp4'")

# 6. 영상 병합용 파일 생성
with open("input.txt", "w", encoding="utf-8") as f:
    f.write("file 'intro.mp4'\n")
    f.write("\n".join(video_list) + "\n")
    f.write("file 'outro.mp4'\n")

# 7. 영상 병합 (인트로+본문+아웃트로)
subprocess.run("ffmpeg -f concat -safe 0 -i input.txt -c copy temp_output.mp4", shell=True)

# 8. 자막과 배경음 추가
subprocess.run(
    'ffmpeg -i temp_output.mp4 -vf "subtitles=subtitle.srt" -i bgm.mp3 '
    '-filter_complex "[1:a]volume=0.3[a1];[0:a][a1]amix=inputs=2:duration=first" '
    '-shortest final_output.mp4',
    shell=True
)
