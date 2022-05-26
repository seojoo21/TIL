from flask import Flask # 서버 구현을 위한 Flask 모듈 import
from flask_restx import Api, Resource # Api 구현을 위한 Api 모듈 import

app = Flask(__name__) # Flask 객체 선언, 파라미터로 어플리케이션 패키지의 이름을 넣어줌.
api = Api(app) # Flask 객체에 Api 객체 등록

@api.route('/hello')
class HelloWorld(Resource):
    def get(self): # GET 요청시 리턴 값에 해당하는 딕셔너리를 JSON 형태로 반환
        return {"hello" : "world!"}

@api.route('/hello/<string:name>')
class HelloWorld(Resource):
    def get(self, name): # GET 요청시 리턴 값에 해당하는 딕셔너리를 JSON 형태로 반환
        return {"message" : "Welcome, %s" %name}
    
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
