# 텍스트 불러오기
bread_ccomangs_review <- readLines("C:/Users/SON/Desktop/ccomangs_cake_review.txt", encoding = "UTF-8")

bread_ccomangs_review
head(bread_ccomangs_review)

# 특수 문자, 한자, 공백, 이모티콘 제거하기 - 분석대상이 아님
install.packages("stringr")
library(stringr) # str_replace_all() : 텍스트에서 특정 규칙에 해당하는 문자를 다른 문자로 바꾸는 함수, 불필요한 문자를 제거하는 기능을 갖고 있음
# str_replace_all_bcr <- str_replace_all(string = bread_ccomangs_review, pattern = "[^가-힣]", replacement = "")
# str_replace_all_bcr

# 기존 띄워쓰기 유지
str_replace_all_bcr <- str_replace_all(string = bread_ccomangs_review, pattern = "[^가-힣\\s]", replacement = "")
str_replace_all_bcr

# 연속된 공백 제거하기 
str_squish_bcr <- str_squish(str_replace_all_bcr)
str_squish_bcr

# 기존 텍스트 파일은, 문자가 나열된 문자열 벡터 구조로 되어 있음
# 문자열 벡터는 행에 들어 있는 모든 내용을 출력하기 때문에 긴 문자가 있으면 출력 결과를 알아보기 어렵다.
# 그러므로, 문자열 벡터를 tibble 구조로 바꾸자.
# dplyr패키지의 as_tibble() : 문자열 벡터를 tibble 구조로 변환하면 텍스트가 보기 편하게 출력이 되고, 텍스트 처리 함수를 적용하기 쉬운 상태가 된다 
install.packages("dplyr")
library(dplyr)
tibble_txt <- as_tibble(str_squish_bcr)
View(tibble_txt) # 전체 확인 가능
as_tibble(tibble_txt) # Console창에 맞게 출력이 되어, 창이 작아 출력되지 않은 행과 열의 정보를 알려주면서 출력

# 단어 토큰화
# unnest_tokens() : 텍스트를 토큰화 
install.packages("ggplot2")
library(ggplot2)
install.packages("tidytext") # 텍스트를 정돈된 데이터 형태를 유지하며 분석할 수 있게 도와주는 패키지
library(tidytext)
library(dplyr)

text <- tibble(value = str_squish_bcr)
text

#  input : 토큰화할 텍스트 
# output : 토큰을 담을 변수명
#  token : 텍스트를 나누는 기준, 문장 = sentences, 띄어쓰기 = words, 글자 = characters
word_space <- text %>%
  unnest_tokens(input = value,
                output = word,
                token = "words")
word_space

# 단어 빈도 분석
# dplyr 패키지의 count() : 단어의 빈도 수를 구할 수 있음
# count()에 sort = T를 입력하면 빈도가 높은 순으로 단어를 정렬한다
word_space <- word_space %>%
  count(word, sort = T)

word_space
# 문제점? 텍스트를 띄어쓰기 기준으로 토큰화했다면 출력한 단어가 대부분 '합니다', '있습니다'와 같이 서술어이다. 
# 텍스트의 의미를 파악하려면 띄어쓰기가 아니라 의미를 결정하는 단위로 토큰화해야 한다. 

# 한 글자로 된 단어는 제거하기
# stringr 패키지의 str_count() : 문자열의 글자 수를 구하는 기능 >> filter(str_count())
# 예시
str_count("좀")
str_count("아")
# 두 글자 이상만 남기기
word_space <- word_space %>%
  filter(str_count(word) > 1)
word_space
View(word_space)

# 자주 사용된, 빈도수가 높은 단어 추출하기 : head()
top20_words <- word_space %>%
  head(20)
top20_words

# 막대 그래프로 시각화 : geom_col()
# ggplot2 패키지의 geom_col() 
library(ggplot2)
ggplot(top20_words, aes(reorder(word, n), y=n)) + # 단어 빈도순으로 정렬
  geom_col() +
  coord_flip() # 회전 -> 단어가 겹쳐보이므로

# 그래프 다듬기 
library(ggplot2)
view_graph_bcr <- ggplot(top20_words, aes(reorder(word, n), y=n)) + # 단어 빈도순으로 정렬
  geom_col() +
  coord_flip() + # 회전 -> 단어가 겹쳐보이므로
  geom_text(aes(label = n), hjust = -0.3) + # 막대 밖 빈도 표시
  labs(title = "꼬망스케잌 리뷰 단어 빈도 수",
       x = NULL, y = NULL) + # 그래프 제목 짓기, 축 이름 삭제
  theme(title = element_text(size = 12)) # 제목 크기
view_graph_bcr

# 그래프의 폰트 변경하기
font_add_google(name = "Gamja Flower", family = "gamjaflower")
showtext_auto()
view_graph_bcr <- ggplot(top20_words, aes(reorder(word, n), y=n)) + # 단어 빈도순으로 정렬
  geom_col() +
  coord_flip() + # 회전 -> 단어가 겹쳐보이므로
  geom_text(aes(label = n), hjust = -0.3) + # 막대 밖 빈도 표시
  labs(title = "꼬망스케잌 리뷰 단어 빈도 수",
       x = NULL, y = NULL) + # 그래프 제목 짓기, 축 이름 삭제
  theme(title = element_text(size = 12), # 제목 크기
        text = element_text(family = "gamjaflower")) # 폰트 적용 
view_graph_bcr


# 워드 클라우드 만들기
# 워드 클라우드 : 단어 빈도를 구름 모양으로 표현한 그래프
# ggwordcloud 패키지의 geom_text_wordcloud()를 이용하면 워드 클라우드를 만들 수 있다. 
install.packages("ggwordcloud")
library(ggwordcloud)
wordcloud_bcr <- ggplot(word_space, aes(label = word, size = n)) +
  geom_text_wordcloud(seed = 1234) +
  scale_radius(limits = c(3, NA), # 최소, 최대 단어 빈도
               range = c(3, 30)) # 최소, 최대 글자 크기
wordcloud_bcr

# 그래프 다듬기 
# scale_color_gradient() : 단어의 색깔을 빈도에 따라 그라데이션으로 표현, low : 빈도가 최소, high : 빈도가 최고 
# theme_minimal() : 배경없는 테마, 이 이외에 theme_bw(), theme_dark() 등이 있으므로 취향에 따라 사용  
wordcloud_bcr <- ggplot(word_space, 
                        aes(label = word, 
                            size = n,
                            col = n)) + # 빈도에 따라 색깔 표현
  geom_text_wordcloud(seed = 1234) +
  scale_radius(limits = c(3, NA), # 최소, 최대 단어 빈도
               range = c(3, 30)) + # 최소, 최대 글자 크기
  scale_color_gradient(low = "#66aaf2", # 최소 빈도 색깔
                       high = "#004EA1") + # 최고 빈도 색깔
  theme_minimal() # 배경없는 테마 적용
wordcloud_bcr
# 워드 클라우드는 디자인이 아름다워서 자주 사용되지만, 분석 결과를 정확하게 표현하는 데에는 적합X
# 단어 배치가 산만해서 비교하기 어렵고, 어떤 단어가 몇번 사용이 되었는지 파악이 어려움

# 폰트 바꾸기 : font_add_google()
# showtext 패키지의 font_add_google()을 이용해 구글 폰트에서 사용할 폰트를 불러온 다음 showtext_auto()를 실행해 폰트를 R에 활용하도록 설정
install.packages("showtext")
library(showtext)
font_add_google(name = "Nanum Gothic", family = "nanumgothic")
showtext_auto()
wordcloud_bcr <- ggplot(word_space,
                        aes(label = word,
                        size = n,
                        col = n)) +
                        geom_text_wordcloud(seed = 1234,
                                            family = "nanumgothic") + # 폰트 적용
                        scale_radius(limits = c(3, NA),
                                     range = c(3, 30)) +
                        scale_color_gradient(low = "#66aaf2",
                                             high = "#004EA1") +
                        theme_minimal()
wordcloud_bcr
# =========================================== # 
font_add_google(name = "Black Han Sans", family = "blackhansans")
showtext_auto()
wordcloud_bcr <- ggplot(word_space,
                        aes(label = word,
                            size = n,
                            col = n)) +
                        geom_text_wordcloud(seed = 1234,
                        family = "blackhansans") + # 폰트 적용
                        scale_radius(limits = c(3, NA),
                        range = c(3, 30)) +
                        scale_color_gradient(low = "#66aaf2",
                        high = "#004EA1") +
                        theme_minimal()
wordcloud_bcr

#-----------------------------------------------------------------------------#
# 위에서 언급한 문제점에 대한 해결책
# 토큰화는 띄어쓰기가 아닌 의미 단위 기준으로 하는 게 좋다. --> 형태소 분석

# 형태소 분석 : 문장에서 형태소를 추출해 동사, 명사, 형용사 등 품사로 분류하는 작업 
# 의미를 지닌 가장 작은 말의 단위 : 형태소
# 형태소 분석 패키지 설치, 자바와 rJAVA 패키지 설치 ~ 의존성 패키지(?)
library(multilinguer)
# install_jdk()
# install.packages(c("stringr", "hash", "tau", "Sejong", "RSQLite", "devtools"), type = "binary")
# install.packages("remotes")
# remotes::install_github("haven-jeon/KoNLP", upgrade = "never", INSTALL_opts = c("--no-multiarch"))
library(KoNLP)
library(dplyr)
useNIADic()

text <- tibble(
  value = str_squish_bcr
)
text

word_noun <- extractNoun(text$value)
View(word_noun)

bcr_review <- readLines("C:/Users/SON/Desktop/ccomangs_cake_review.txt", encoding = "UTF-8")
library(stringr)
review <- bcr_review %>%
  str_replace_all("[^가-힣\\s]", replacement = " ") %>%
  str_squish() %>%
  as_tibble()

library(tidytext)
noun <- review %>%
  unnest_tokens(input = value, 
                output = word,
                token = extractNoun)
noun

# 명사 빈도 분석하기
word_noun <- noun %>%
  count(word, sort = T) %>%
  filter(str_count(word) > 1)
word_noun

# 상위 20개 단어 추출
top20 <- word_noun %>%
  head(20)
top20

# 막대 그래프 만들기
library(ggplot2)
ggplot(top20, aes(x= reorder(word, n), y = n)) +
  geom_col() +
  coord_flip() +
  geom_text(aes(label = n), hjust = -0.3) +
  labs(x = NULL) +
  theme(text = element_text(family = "nanumgothic"))

# 워드 클라우드 만들기 
library(showtext)
font_add_google(name = "Black Han Sans", family = "blackhansans")
showtext_auto()

library(ggwordcloud)
ggplot(word_noun, aes(label = word, size = n, col = n)) +
  geom_text_wordcloud(seed = 1234, family = "blackhansans") +
  scale_radius(limits = c(3, NA),
               range = c(3, 15)) +
  scale_color_gradient(low = "#66aaf2", high = "#004EA1") +
  theme_minimal()

# 특정 단어가 사용된 문장 살펴보기
word_space <- text %>%
  unnest_tokens(input = value,
                output = word,
                token = "words")
word_space
