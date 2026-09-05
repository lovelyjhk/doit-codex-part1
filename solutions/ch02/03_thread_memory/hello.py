from datetime import date

name = input("이름을 입력하세요: ")
greeting = f"안녕하세요, {name}님!"
today = date.today()

print(f"{greeting} 오늘 날짜는 {today}입니다.")
