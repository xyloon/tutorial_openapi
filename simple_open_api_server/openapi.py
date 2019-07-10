from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


door = "closed"

passwords = set()


class PassWord(Resource):
    def post(self):
        global door, passwords
        user_input = request.form['data']
        print(user_input, passwords, user_input in passwords)

        checked_result = user_input in passwords
        if checked_result:
            door = "opened"
        return {
            "result": "OK" if checked_result else "FAIL",
            "state": door
        }

    def put(self):
        global door, passwords
        idstring = request.form['data']
        passwords.add(idstring)
        return {
            "result": "OK",
            "state": door
        }


class SensorClose(Resource):
    def put(self):
        global door, passwords
        door = "closed"
        return {
            "result": "OK",
            "state": door
        }


api.add_resource(PassWord, '/user_input')
api.add_resource(SensorClose, '/sensor')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
