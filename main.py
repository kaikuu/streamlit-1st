import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('streamlit 超入門')

st.write('DataFrame')

df=pd.DataFrame({
    '1列目': [1,2,3,4],
    '２列目': [5,6,7,8]
})

st.write(df)
# 元のdataframeより大きくはできない
# st.dataframe(df,width=300,height=300)
# 大きさを指定するとdataframeが縮小
# st.dataframe(df,width=100,height=100)

# 行を強調
st.dataframe(df.style.highlight_max(axis=0))
# 静的な表を作成するのに最適
st.table(df.style.highlight_max(axis=0))

"""
# プログレスバーの表示
```python
bar=st.progress(0)
latest_iterrate=st.empty()
for i in range(100):
    latest_iterrate.write(f'iterrate:{i+1}')
    bar.progress(i+1)
    time.sleep(0.05)
```
"""
bar=st.progress(0)
latest_iterrate=st.empty()
for i in range(100):
    latest_iterrate.write(f'iterrate:{i+1}')
    bar.progress(i+1)
    time.sleep(0.05)

"""
# グラフ
## ランダムデータのグラフ
"""
st.write('【使用するデータフレーム】')
df=pd.DataFrame(
    np.random.rand(20,3),
    columns=['a','b','c']
)
st.dataframe(df)

"""
### ①折れ線グラフ
```python
st.line_chart(df)
```
"""
st.line_chart(df)

"""
### ②エリアグラフ
```python
st.area_chart(df)
```
"""
st.area_chart(df)

"""
### ③バーグラフ
```python
st.bar_chart(df)
```
"""
st.bar_chart(df)

"""
## 新宿周辺のマップ
"""
st.write('【使用するデータフレーム】')
df=pd.DataFrame(
    np.random.rand(100,2)/[50,50] + [35.69,139.70],
    columns=['lat','lon']
)
st.dataframe(df)

"""
### ④マップ
```python
st.map(df)
```
"""
st.map(df)


"""
# 画像
## DISPLAY IMAGE
```python
if st.checkbox('Show Image'):
    img = Image.open('meteo.jpg')
    st.image(img, caption='meteo', use_column_width=True )
```
"""
if st.checkbox('Show Image'):
    img = Image.open('meteo.jpg')
    st.image(img, caption='meteo', use_column_width=True )

"""
# インタラクティブなウィジェット
## ・セレクトボックス
```python
option=st.selectbox('あなたが好きな数字を教えてください',list(range(1,11)),key='option')
st.write('あなたが好きな数字は', option, 'です。')
```
"""
option=st.selectbox('あなたが好きな数字を教えてください',list(range(1,11)),key='option')
st.write('あなたが好きな数字は', option, 'です。')

"""
## ・テキストボックス
```python
text=st.text_input('あなたの趣味は何ですか？',key='text')
st.write('あなたの趣味は、',text,'です。')
```
"""
text=st.text_input('あなたの趣味は何ですか？',key='text')
st.write('あなたの趣味は、',text,'です。')

"""
## ・スライダー
```python
condition=st.slider('あなたの今の調子は？',0,100,50,key='condition')
st.write('あなたのコンディションは、',condition,'です。')
```
"""
condition=st.slider('あなたの今の調子は？',0,100,50,key='condition')
st.write('あなたのコンディションは、',condition,'です。')


"""
# レイアウト修正
## ・サイドバー
```python
st.sidebar.write('Intaractive Wedgets')
side_option=st.sidebar.selectbox('1.あなたが好きな数字を教えてください',list(range(1,11)))
side_text=st.sidebar.text_input('2.あなたの趣味は何ですか？')
side_condition=st.sidebar.slider('3.あなたの今の調子は？',0,100,50)
```
"""
st.sidebar.write('Intaractive Wedgets')
side_option=st.sidebar.selectbox('1.あなたが好きな数字を教えてください',list(range(1,11)),key='side_option')
side_text=st.sidebar.text_input('2.あなたの趣味は何ですか？',key='side_text')
side_condition=st.sidebar.slider('3.あなたの今の調子は？',0,100,50,key='side_condition')
st.write('1.あなたが好きな数字は', side_option, 'です。')
st.write('2.あなたの趣味は、',side_text,'です。')
st.write('3.あなたのコンディションは、',side_condition,'です。')

"""
## ・２カラムレイアウト
```pyton
left_column, right_column = st.beta_columns(2)
button1 = left_column.button('右からカラムに文字を表示',key='button1')
if button1:
    right_column.write('こちらは右カラム１です。')
    right_column.write('ー')

button2 = left_column.button('右からカラムに文字を表示',key='button2')
if button2:
    right_column.write('ー')
    right_column.write('こちらは右カラム２です。')
```
"""
left_column, right_column = st.beta_columns(2)
button1 = left_column.button('右からカラムに文字を表示',key='button1')
if button1:
    right_column.write('こちらは右カラム１です。')
    right_column.write('ー')

button2 = left_column.button('右からカラムに文字を表示',key='button2')
if button2:
    right_column.write('ー')
    right_column.write('こちらは右カラム２です。')


"""
## ・expander
```pyton
expander = st.beta_expander('問い合わせ１')
expander.text_area('問い合わせ内容',key='toiawase1')
expander.write('※誤りのないようご記入ください')
```
"""
expander = st.beta_expander('問い合わせ１')
expander.text_area('問い合わせ内容',key='toiawase1')
expander.write('※誤りのないようご記入ください')

expander = st.beta_expander('問い合わせ２')
expander.text_area('問い合わせ内容',key='toiawase2')
expander.write('※誤りのないようご記入ください')