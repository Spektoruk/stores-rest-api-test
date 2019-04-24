from werkzeug .security import safe_str_cmp
from models.user import UserModel

def authenticate(username, password):
    """
    Function thatets called when a user calls the /auth endpoint
    with their username and password.
    :param username:User's username in string format.
    :param password:User's un-encrypted password in string format.
    :return:A UserModel object if authentiation was succsessful, None otherwise.
    """

    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user

def identity(payload):
    """
    Function that gets called when user is already authenticated, and FlaskJWT
    verified their authorization header is correct.
    :param payload:A dictionary with 'identity' key, which is user id.
    :return:A UserModel object.
    """
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)