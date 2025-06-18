# 🕳️ blind-sqli-extractor

**Blind SQL Injection (Boolean-based) 자동화 추출 도구**

이 도구는 Blind SQL Injection 취약점을 이용해 데이터베이스 이름을 문자 단위로 추출합니다.  
응답 본문에 특정 키워드나 패턴이 존재하는지를 기반으로 참/거짓을 판별합니다.

---

## 🎯 Features

- Boolean-based Blind SQLi 지원
- `substring()` 함수 기반 한 글자씩 추출
- 사용자 정의 charset 가능
- 참 조건은 **응답 내용 또는 길이 기반**으로 판단 가능
- Python 표준 라이브러리만으로 간단하게 구현됨

---

## 🛠 Requirements

- Python 3.x
- `requests` 모듈

설치:
```bash
pip install requests
pip install string
