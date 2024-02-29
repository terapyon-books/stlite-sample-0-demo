import streamlit as st

st.title("文字列変換機能アプリ")
st.write("入力された文字列をルールに基づき変換します。")

text = st.text_input("変換前の文字列を入力してください")
rule = st.radio("変換ルールを選択してください", ("大文字", "小文字", "タイトルケース"))
convert = st.button("変換")

if convert:
    if rule == "大文字":
        result = text.upper()
    elif rule == "小文字":
        result = text.lower()
    elif rule == "タイトルケース":
        result = text.title()
    st.write("変換結果:", result)
