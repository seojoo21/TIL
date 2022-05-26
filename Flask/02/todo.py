from flask import request
from flask_restx import Resource, Api, Namespace, fields

todos = {}
count = 1

Todo = Namespace(
    name = 'Todos',
    description= 'Todo 리스트를 작성하기 위해 사용하는 API'
    )

# Namespace.model()은 입력, 출력에 대한 스키마를 나타내는 객체 입니다.
# flask_restx 내의 field 클래스를 이용하여, 설명, 필수 여부, 예시를 넣을 수 있습니다.
# 또한 Namespace.inherit()을 이용하여, Namespace.model() 을 상속 받을 수 있습니다.
todo_fields = Todo.model('Todo', {  # Model 객체 생성
    'data': fields.String(description='a Todo', required=True, example="what to do")
})

todo_fields_with_id = Todo.inherit('Todo With ID', todo_fields, {
    'todo_id': fields.Integer(description='a Todo ID')
})

@Todo.route('')
class TodoPost(Resource):
    # Namespace.expect() 특정 스키마가 들어 올 것을 기대한다. Namespace.Model 객체를 등록하면 됩니다.
    # Namespace.response() 말 그대로 특정 스키마가 반환 된다. 첫 번째 파라미터로 Status Code, 두 번째 파라미터로 설명, 세 번째 파라미터로 Namespace.Model 객체가 들어 갑니다.
    @Todo.expect(todo_fields)
    @Todo.response(201, 'success', todo_fields_with_id)
    def post(self):
        """Todo 리스트에 할 일을 등록 합니다.""" # Document에 설명 추가 
        global count
        global todos
        
        idx = count
        count += 1
        todos[idx] = request.json.get('data')
        
        return {
            'todo_id': idx,
            'data': todos[idx]
        }

@Todo.route('/<int:todo_id>')
@Todo.doc(params={'todo_id' : 'An ID'})
class TodoSimple(Resource):
    
    # Namespace.doc() 데코레이터를 이용하여, Status Code 마다 설명을 추가하거나, 쿼리 파라미터에 대한 설명을 추가 할 수 있습니다.
    @Todo.doc(response={202: 'Success'})
    @Todo.doc(response={500: 'Failed'})
    def get(self, todo_id):
        """Todo 리스트에 todo_id와 일치하는 ID를 가진 할 일을 가져옵니다."""
        return {
            'todo_id': todo_id,
            'data': todos[todo_id]
        }

    def put(self, todo_id):
        """Todo 리스트에 todo_id와 일치하는 ID를 가진 할 일을 수정합니다."""
        todos[todo_id] = request.json.get('data')
        return {
            'todo_id': todo_id,
            'data': todos[todo_id]
        }
    
    def delete(self, todo_id):
        """Todo 리스트에 todo_id와 일치하는 ID를 가진 할 일을 삭제합니다."""
        del todos[todo_id]
        return {
            "delete" : "success"
        }