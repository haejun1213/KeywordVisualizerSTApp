import streamlit as st
import pandas as pd
from konlpy.tag import Okt
import lib.NaverNewsCrawler as nnc
import lib.myTextMining as tm
import lib.STViualizer as stv

def process_text_data(df, column_name, freq, wordcloud, freq_word, wordcloud_word):
    if column_name not in df.columns:
        st.error(f"'{column_name}' 컬럼이 존재하지 않습니다. 올바른 컬럼명을 입력하세요.")
        return
    
    corpus_list = list(df[column_name].dropna())

    my_tokenizer = Okt().pos
    my_tags = ['Noun', 'Adjective', 'Verb']
    my_stopwords = ['하며', '입', '하고', '로써', '하게', '하여', '한다', '고', '과', '그', '등', '이', '있다', '했다', '관련', '위', '의', '해', '베', '하면', '도']
    
    counter = nnc.analyze_word_freq(corpus_list, my_tokenizer, my_tags, my_stopwords)

    if freq:
        stv.visualize_barchart(counter, '키워드', '빈도', top_n=freq_word)
    if wordcloud:
        stv.visualize_wordcloud(counter, top_n=wordcloud_word)

with st.form("설정"):
    st.write("설정")

    freq = st.checkbox("빈도수 그래프")
    freq_word = st.slider("빈도수 그래프 단어 수", min_value=10, max_value=50, value=20)
    
    wordcloud = st.checkbox("워드클라우드")
    wordcloud_word = st.slider("워드클라우드 단어 수", min_value=20, max_value=500, value=50)
    
    column_name = st.text_input("분석할 데이터 컬럼명", value="description")

    settings_submitted = st.form_submit_button("설정 저장")

with st.form("news_search"):
    st.write("Naver News 검색")
    keyword = st.text_input("키워드 입력")
    csv_save = st.checkbox("CSV 저장 여부")
    
    search_submitted = st.form_submit_button("검색")

    if search_submitted:
        st.write("키워드:", keyword, "| CSV 저장:", csv_save)
        resultAll = []

        start = 1
        display = 10

        resultJSON = nnc.searchNaverNews(keyword, start, display)

        while (resultJSON is not None) and (resultJSON['display'] > 0):
            nnc.setNewsSearchResult(resultAll, resultJSON)
            start += display
            if start > 99:
                break
            resultJSON = nnc.searchNaverNews(keyword, start, display)

        if csv_save:
            filename = f'./data/{keyword}_naver_news.csv'
            nnc.saveSearchResult_CSV(resultAll, filename)

        df = pd.DataFrame(resultAll)

        process_text_data(df, column_name, freq, wordcloud, freq_word, wordcloud_word)

uploaded_file = st.file_uploader("CSV 파일 업로드")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    process_text_data(df, column_name, freq, wordcloud, freq_word, wordcloud_word)
