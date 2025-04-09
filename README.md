# KeywordVisualizerSTApp

**Korean News Keyword Visualizer**는 네이버 뉴스에서 수집한 기사 데이터를 바탕으로 자연어 처리를 수행하여 키워드 분석, 빈도 시각화, 워드클라우드 생성을 할 수 있는 Streamlit 기반의 시각화 대시보드입니다.

---

## 프로젝트 구조

.
├── lib/
│   ├── myTextMining.py         # 텍스트 마이닝 유틸 함수 모음
│   ├── NaverNewsCrawler.py     # 네이버 뉴스 API 크롤러
│   └── STViualizer.py          # Streamlit 시각화 함수
├── KeywordVisualizerSTApp.py   # 메인 Streamlit 앱
├── data/                       # 수집한 뉴스 CSV 저장 폴더
└── README.md                   # 프로젝트 설명

---

## 주요 기능

### 1. 뉴스 데이터 수집 (`lib/NaverNewsCrawler.py`)

- **searchNaverNews(keyword, start, display)**  
  → 네이버 뉴스 API를 이용하여 뉴스 기사 검색

- **setNewsSearchResult(resultAll, resultJSON)**  
  → API 응답을 리스트 형태로 정리

- **saveSearchResult_CSV(json_list, filename)**  
  → 수집한 데이터를 CSV로 저장

---

### 2. 텍스트 분석 및 시각화 (`lib/myTextMining.py`)

- **load_corpus_from_csv(corpus_file, col_name)**  
  → CSV 파일에서 텍스트 데이터 불러오기

- **tokenize_korean_corpus(corpus_list, tokenizer, tags, stopwords)**  
  → 형태소 분석 및 불용어 제거

- **analyze_word_freq(...)**  
  → 키워드 빈도 분석

- **visualize_barchart(...) / visuallize_wordcloud(...)**  
  → 빈도 그래프 및 워드클라우드 시각화

---

### 3. Streamlit 시각화 기능 (`lib/STViualizer.py`)

- **visualize_barchart(...)**  
  → Altair 기반 키워드 빈도 그래프

- **visualize_wordcloud(...)**  
  → 워드클라우드 시각화 및 Streamlit 출력

---

### 4. 메인 앱 (`KeywordVisualizerSTApp.py`)

- 키워드 기반 뉴스 수집 + 실시간 시각화
- CSV 업로드 분석 지원
- 사용자 설정을 통한 시각화 옵션 조절 (단어 수, 그래프 선택 등)

---

## 주요 라이브러리

konlpy

pandas

matplotlib

wordcloud

streamlit

altair

---

## 실행 예시

분석할 키워드 입력 후 뉴스 검색

검색 결과에서 특정 컬럼 (description 등) 선택

워드클라우드 및 빈도수 그래프 자동 생성

결과 CSV 저장 (옵션)

![image](https://github.com/user-attachments/assets/7f76e8ca-f000-4735-b371-4352d2c96947)
![image](https://github.com/user-attachments/assets/7bc3c511-22a7-4b06-accc-25292dd0b290)
