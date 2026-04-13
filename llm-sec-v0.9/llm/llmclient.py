#communicate with LLM API with openai

from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()#加载当前根目录下的环境变量
DASHSCOPE_API_KEY = os.getenv('DASHSCOPE_API_KEY')#获取环境变量中的API_KEY
# 初始化OpenAI客户端，指向通义千问的兼容地址
client = OpenAI(
    api_key=DASHSCOPE_API_KEY,
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1" # 这是通义千问兼容模式的固定地址
)

def ai_answer(question:str)->str:
    '''send question to LLM and get answer'''
    try:
        #调用千问API
        completion = client.chat.completions.create(
            model='qwen-turbo',
            messages=[
                {"role":"system","content":"You are a helpful assistant."},#设定ai角色
                {"role":"user","content":question}#用户问题
            ],
            temperature=0.9,
        )
        return completion.choices[0].message.content
    except Exception as e:
        #print the error message
        print(f'Error: {e}')
        return None