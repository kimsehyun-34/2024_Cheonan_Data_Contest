# 2024 Cheonan Data Contest Exhibit
- 2024_2nd_천안 데이터 공모전_클라우드
- 김민수, 김세현, 이혜준, 이지우

---------------------------------
---------------------------------
# 24.08.08 공모전 4차 회의
- 데이터 (빵집, 관광명소, 숙박시설) , 카페 대신에 빵집, 숙박시설 + 천안시 장기체류 비율을 높이기 위해서 주변 관광지(나이, 성별, 세대을 고려한 코스) 넣는 것이다.
- 기본 토대는 천안시 관광코스를 따라가되 사이사이에 빵집과 관광명소를 끼워넣는 것
- ### 정적 알고리즘 으로 할것
---------------------------------
---------------------------------
# 24.08.08 공모전 4차 회의
- ## 주제 변경
  - ### 최적화된 천안시 관광요소 + 빵집 추천
---------------------------------
---------------------------------
# 24.08.05 공모전 3차 결과보고
- 리뷰 크롤링 완료
- 웹 작업 70%완료
- QGIS대신 파이썬으로 대체
---------------------------------
---------------------------------
# 24.07.31 공모전 2차 회의

### 1. 관광 활성화

- 빵집 순례 -> 시민들 대상 이벤트 

### 관광의 이유 ? 
- 천안시 공인 빵 맛집 리뷰 크롤링 및 데이터분석이 가능하다!
  - 빵이 이뻐서
  - 시설이 너무 좋아서

- 빵집(=카페) / 가는 기준이 무엇인가 ?
  -남성, 여성 카드소비데이터 -> 빈도수를 파악 (포인트 적립 등 데이터에 대한 객관성이 떨어진다 생각함)

### 군집화의 기준이란 ? 
  - 맛(빵의 종류), 거리, 주변 시설, 관경, 가격, 대기시간(시간대별), 청결(?), 서비스, 음식 양

### 장점을 극대화해라
  - 빵빵데이 사이트 , 빵소 팜플렛 pdf 파일
  - 기존의 빵지순례 루트를 보고 극대화 시켜야 겠다 (주제 선정 이유)

### [역할분담]
  - 김민수 : 크롤링
  - 김세현 : 웹 개발
  - 이혜준: qgis
  - 이지우: 앱 개발 

## 프론트 엔드 순서
1. 자신의 위치 정보 수집
2. 위치 주변에서 5분 또는 10분 등 으로 조건 수집
3. 유저가 선택한 조건들로 검색
   
#### [첫 화면] GPS 허용하시겠습니까?
#### [두번째 화면] 허용시, 선택란 휴대폰과 떨어진 거리 범위 허용 (5분) (10분) (15분) 선택란뜨게
- 5분을 눌렀을 때, 그 범위내에 빵소가 없다면, "근처에 빵소가 존재하지 않습니다." 뜨고
- 빵소가 있다면, "근처에 빵소 2곳이 발견되었습니다."
#### [세번째 화면] 특성: 맛, 청결, 빵소디자인, 주차공간, 분위기, 등
- 여기서 중요도1: , 중요도2: , 중요도3: 이렇게 뜨게해서 넣어지게
- 여기서 데이터를 활용, (데이터활용 -> 천안시가 선정한 빵소들을 네이버 댓글 크롤링하여 워드클라우드, 히스토그램들로 특성 군집화 통해 선정)
- 중요도1 중요도2 중요도3 여기서 가중치를 다르게 두어 최단 거리 선정 <- 여기서 사용되는 알고리즘 코드는 다이나믹프로그래밍을 이용한 TSP
- 그리고 예를들어 북구에 북대문이 유명하다, GPS로 인해자동추천하여 빵소1 - 북대문 - 빵소2  : 최단거리 12분입니다 하고지도로 뜨게하는 구현영상
---------------------------------
---------------------------------
# 24.07.28 공모전 1차 회의
- 천안 빵집 데이터 수집 (객관적인 데이터일 필요 있음) 
- 리뷰 데이터(광고성 댓글이 많기 때문에, 주관성이 높을 수 있음)
   - 데이터 전처리 통하여, 잘 선별필요있음
- 객관적인 데이터 토대로, 네이버 리뷰 댓글들을 크롤링하여, 히스토그램 및 워드 클라우드를 가지고 시각화 (청결, 주차, 맛, 가게 디자인, 지역별 등 다양한 특성별로 데이터 전처리 및 분류)
- 천안 빵집 관련하여 논문 기사 조사
- 추후, 다익스트라 알고리즘 또는 다른 알고리즘을 가지고 가중치를 두어 자동으로 경로를 짜주는 빵집투어 지도 제작
- 기회가 된다면, 앱개발 또는 UI 디자인하여 천안 명소+빵집+빵집을 넣었을때 자동으로 경로를 짜주는 시스템 개발
- 기대효과로는 천안에 유명한 대학(단국대, 상명대, 호서대, 등) 청년인구 경제 활성화, 지역 경제 활성회, 빵리단길과 같은 지역 특성 개발가능 
