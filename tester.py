# tester.py
from geo.utils import circumference, area

r = 10.0  # 반지름 값: 자동채점 기준에서는 10이 되어야 'area = 314.159...'이 나옵니다.
c = circumference(r)
a = area(r)
print(f"c = {c}")
print(f"area = {a}")
