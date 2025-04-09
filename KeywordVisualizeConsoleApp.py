from collections import Counter
import mylib.NaverNewsCrawler as nnc
import mylib.myTextMining as tm
keyword = input("검색어 : ").strip()

resultAll = []

start = 1
display = 10

resultJSON = nnc.searchNaverNews(keyword, start, display)

while (resultJSON != None) and (resultJSON['display'] > 0):
    nnc.setNewsSearchResult(resultAll, resultJSON)
 
    start += display

    resultJSON = nnc.searchNaverNews(keyword, start, display)
    if resultJSON != None:
        print(f'{keyword} [{start}] : Search Request Success')
    else :
        print(f'{keyword} [{start}] :Error ~~')

filename = f'./data/{keyword}_naver_news.csv'
nnc.saveSearchResult_CSV(resultAll, filename)

from konlpy.tag import Okt

corpus_list = nnc.load_corpus_from_csv(filename, "description")

my_tokenizer = Okt().pos
my_tags = ['Noun', 'Adjective', 'Verb']
my_stopwords = ['하며', '입', '하고', '로써', '하게', '하여', '한다']
counter = nnc.analyze_word_freq(corpus_list, my_tokenizer, my_tags, my_stopwords)

nnc.visuallize_wordcloud(counter, keyword)
tm.visualize_barchart(counter, '네이버 뉴스 키워드 분석', '빈도', '키워드')