import numpy as np
from PIL import Image
import streamlit as st
import openai
import requests

openai.api_key = 'API-KEY'
def get_openai_response(prompt, prompt1, prompt2, prompt3):
    """
    Get completion from OpenAI based on a given prompt.
    """
    message_history = [
                    {"role": "system", "content": "You are a helpful AI assistant."},
                    {"role": "user", "content": f"역할 놀이를 할거야. 너는 나의 전문 운동 트레이너라서 나의 식단과 운동법을 엄격하게 관리해야돼. 나의 오늘 아침식사는 {prompt}이고, 점심식사는 {prompt1}, 저녁식사는 {prompt2}야. 오늘 하루동안 섭취한 단백질의 양을 대략적으로 gram으로 알려주고 오늘 먹은 음식 중 건강하지 않은 음식(예를 들어 지방이나 당이 너무 많은 음식, 또는 알코올)을 찾아내서 나를 혼내줘. 그리고 앞으로의 식단법과 운동법 대해 구체적으로 조언해줘. 내 몸무게는 {prompt3}kg이야."},
                ]
    response = openai.ChatCompletion.create(
                    model='gpt-3.5-turbo', # model 선택
                    messages=message_history,
                    stream=False
                )
    return response['choices'][0]['message']['content']


def main():
    st.title('오늘 식단의 단백질 양을 알려줘!')
    st.image("protein.png", use_column_width=True)

    user_input = st.text_input("아침식사: ", "")
    user_input1 = st.text_input("점심식사: ", "")
    user_input2 = st.text_input("저녁식사: ", "")
    user_input3 = st.text_input("몸무게를 입력하세요: ", "")
    if st.button("Send"):
        if user_input:
            with st.spinner('생성 AI로 답변을 생성하는 중입니다 ...'):
                response = get_openai_response(user_input, user_input1, user_input2, user_input3)
            st.markdown(f'**Bot:**\n{response}')
        else:
            st.warning("생성 AI에게 물어보고 싶은 메시지를 입력해주세요!")

if __name__ == '__main__':
    main()
