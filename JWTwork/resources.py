from flask_restful import Resource, reqparse
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, get_jwt_identity, get_jwt)
from models import UserModel, RevokedTokenModel

# 在RESTful API中每个接口都被称作资源,
# 每个类都继承自Resource也就拥有了API端点的全部特性
# 服务器所有返回内容都应该被jsonify()包装
# 而Flask-RESTful不需要显示调用jsonify

parser = reqparse.RequestParser()
# 用reqparse.RequestParser()初始化parser
# 添加参数username and password并制定这两个参数为必选
# 添加location=<target>,target可以是json, args, and form
parser.add_argument('username', location='json', help = 'This field cannot be blank', required = True)
parser.add_argument('password', location='json', help = 'This field cannot be blank', required = True)

class UserRegistration(Resource):
    def post(self):
        data = parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {'message': 'User {} already exists'.format(data['username'])}

        # 收到一个请求时将会创建一个UserModel对象
        new_user = UserModel(
            username = data['username'],
            password = UserModel.generate_hash(data['password'])
        )

        try:
            new_user.save_to_db()
            # 用于访问被保护的敏感信息
            access_token = create_access_token(identity = data['username'])
            print(access_token)
            # 用户重新颁发过期的access token
            refresh_token = create_refresh_token(identity = data['username'])
            return {
                'message': 'User {} was created'.format(data['username']),
                'access_token': access_token,
                'refresh_token': refresh_token
            }
        except:
            return {'message': 'Something went wrong'}, 500


class UserLogin(Resource):
    def post(self):
        data = parser.parse_args()
        current_user = UserModel.find_by_username(data['username'])

        if not current_user:
            return {'message': 'User {} doesn\'t exist'.format(data['username'])}
        
        # 用户存在检查密码
        if UserModel.generate_hash(data['password']) == current_user.password:
            access_token = create_access_token(identity = data['username'])
            refresh_token = create_refresh_token(identity = data['username'])
            return {
                'message': 'Logged in as {}'.format(current_user.username),
                'access_token': access_token,
                'refresh_token': refresh_token
            }
        else:
            return {'message': 'Wrong credentials'}
      
      
class UserLogoutAccess(Resource):
    @jwt_required()
    def post(self):
        jti = get_jwt()['jti']
        try:
            revoked_token = RevokedTokenModel(jti=jti)
            revoked_token.add()
            return {'message': 'Access token has been revoked'}
        except:
            return {'message': 'Something went wrong'}, 500


class UserLogoutRefresh(Resource):
    @jwt_required(refresh=True)
    def post(self):
        jti = get_jwt()['jti']
        try:
            revoked_token = RevokedTokenModel(jti=jti)
            revoked_token.add()
            return {'message': 'Refresh token has been revoked'}
        except:
            return {'message': 'Something went wrong'}, 500
      
# token刷新。
# token需要有一个过期时间，默认情况下access token有15分钟的有效期，
# refresh tokens是30天
class TokenRefresh(Resource):
    @jwt_required(refresh=True)
    def post(self):
        """
        为了确定用户身份，我们使用get_jwt_identity()从refresh token中抽取身份信息，
        然后使用这个身份生成新的access token并返回给用户。
        """
        current_user = get_jwt_identity()
        access_token = create_access_token(identity=current_user)
        return {'access_token': access_token}
      
      
class AllUsers(Resource):
    def get(self):
        return UserModel.return_all()

    def delete(self):
        return UserModel.delete_all()
      

# 获取数据接口（测试access token)
class SecretResource(Resource):
    @jwt_required()
    def get(self):
        return {
            'answer': 42
        }