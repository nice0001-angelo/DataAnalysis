from pandas import DataFrame #모듈참조
from pandas import read_csv #모듈참조
from matplotlib import pyplot #모듈참조
#from sample import height #데이터참조

# 성적표 데이터 -> 기술통계 수치값, 상자그림 확인을 위한 샘플 데이터
성적표csv=read_csv("http://itpaper.co.kr/demo/python/grade.csv",encoding="euc-kr")
print(성적표csv)



학생이름={}
for i, v in enumerate(list(성적표csv['이름'])):

    학생이름[i]=v
print(학생이름[i])
