# ffmpeg-text-overlay-fail-log

### ❌ 목표
- ffmpeg로 영상에 텍스트, 배경음악, 자막 자동 삽입 (Python 스크립트 포함)
- 실패를 반복하면서 문제 파악

---

### 🧪 시도한 것들
- drawtext로 한글 자막 입히기
- fontfile 사용 (malgun.ttf, 경로 슬래시 처리 등)
- srt 자막 삽입 시도
- Python subprocess 기반 자동화
- Windows CLI 직접 입력 등

---

### 💥 주요 실패 요약
- `drawtext=text=...` 한글 + 특수문자 처리에서 계속 파싱 오류
- srt 자막 삽입 실패 (libass / encoding 문제)
- Python subprocess로 실행 시 경로 및 filter 파싱 충돌
- 영상 2초인데 결과물이 2시간짜리 나옴 (...)

---

### 🪓 결론
- CapCut이 인간의 승리
- ffmpeg는 "한글 drawtext"에 빡침 주는 의외의 툴
- 다음엔 Python이 아닌 `.bat` 기반으로 조립하는 게 차라리 낫다

---

### 📁 폴더 구조
