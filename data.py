class Data:
    URL = 'https://stellarburgers.nomoreparties.site/'
    REG_PATH = 'api/auth/register'
    AUTH_PATH = 'api/auth/login'
    CHANGE_PATH = 'api/auth/user'
    DEL_PATH = 'api/auth/user'
    CREATE_ORDER_PATH = 'api/orders'
    GET_ORDERS_PATH = 'api/orders'

    WRONG_EMAIL_OR_PASSWORD_MASSAGE = '"message":"email or password are incorrect"'
    AUTH_ERROR_MASSAGE = '"message":"You should be authorised"'
    EMPTY_ID_OF_INGREDIENT_MASSAGE = '"message":"Ingredient ids must be provided"'
    MISSED_REQUIRED_FIELD_MASSAGE = '"message":"Email, password and name are required fields"'
    REG_EXISTENT_USER_MASSAGE = '"message":"User already exists"'