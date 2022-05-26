from flask import Flask, request
from flask_restx import Api, Resource

app = Flask(__name__)
todo_api = Api(app)

todos = {}
count = 1

@todo_api.route('/todos')
class Todo(Resource):
    def get(self):
        return {"hello" : "world"}

    def post(self):
        global todos
        global count
        
        idx = count
        count += 1 
        todos[idx] = request.json.get('data')
        # body에 있는 데이터를 가져오기 위해서, 취하는 방법은 간단합니다. 
        # flask 모듈 내의 request 내의 json 객체를 이용하여, request body로 들어온 json값을 파싱하면 됩니다.
        # post 로 데이터 전송 시 예시) 
        # {
        #   "data" : "test"    
        # }
        
        return {
            'todo_id' : idx,
            'data' : todos[idx]
        }
        
@todo_api.route('/todos/<int:todo_id>')
class TodoSimple(Resource):
    def get(self, todo_id):
       return {
           'todo_id' : todo_id,
           'data' : todos[todo_id]
       } 
       
    def put(self, todo_id):
        todos[todo_id] = request.json.get('data')
        return {
           'todo_id' : todo_id,
           'data' : todos[todo_id]
        } 

    def delete(self, todo_id):
        del todos[todo_id]
        return {
            "delete" : "success"
        }
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')