import pandas as pd
import streamlit as st
import altair as alt

def visualize_barchart(counter, xlabel, ylabel, top_n):
    word_list = [word for word, count in counter.most_common(top_n)]
    count_list = [count for word, count in counter.most_common(top_n)]

    df = pd.DataFrame({"키워드": word_list, "빈도": count_list})
    df = df.sort_values(by="빈도", ascending=True)

    chart = alt.Chart(df).mark_bar().encode(
        x=alt.X('빈도:Q', title=ylabel),
        y=alt.Y('키워드:N', sort='-x', title=xlabel)
    ).properties(
        width=600,
        height=500
    )
    st.altair_chart(chart, use_container_width=True)

def visualize_wordcloud(counter, top_n):
    from wordcloud import WordCloud
    import matplotlib.pyplot as plt

    font_path = "c:/Windows/fonts/malgun.ttf"

    wordcloud = WordCloud(font_path, width=600, height=600, max_words=top_n, background_color='ivory')

    wordcloud = wordcloud.generate_from_frequencies(counter)

    fig = plt.figure()
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()
    st.pyplot(fig)