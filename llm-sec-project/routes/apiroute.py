
from flask import request,jsonify
from ..llm.llmclient import ai_answer


def register_api_route(app):
    '''api route for LLM question answering'''
    @app.route('/ask',methods=['POST'])
    def ask():
        '''handle the question from frontend and return the answer from LLM'''
        if request.method == 'POST':
            try:
                question = request.form.get('question','')#获取post方法传递的question参数
                if not question:
                    return jsonify({"error":'The question can\'t be empty.'}),400
                
                answer = ai_answer(question)
                if answer:
                    return jsonify({'answer':answer})
                else:
                    return jsonify({'error':'Failed to get answer from LLM.'}),500
                
                return ai_answer(question)
            except Exception as e:
                return jsonify({'error':str(e)}),500