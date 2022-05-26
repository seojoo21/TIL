from flask import Flask
from flask_restx import Resource, Api
from todo import Todo

app = Flask(__name__)
api = Api(
        app,
        version='0.1', # API Server의 버전을 명시합니다.
        title="TEST API SERVER", # API Server의 이름을 명시합니다.
        description="TEST API SERVER", # API Server의 설명을 명시합니다.
        terms_url="/", # API Server의 Base Url을 명시합니다.
        contact="kangj2022@yjmedia.com", # 제작자 E-Mail 등을 삽입합니다.
        license="MIT"  # API Server의 라이센스를 명시 합니다.
          )

api.add_namespace(Todo, '/todos')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')