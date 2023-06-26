''' Tasks entities '''


class User:
    ''' User entity class '''

    def __init__(self):
        self.__username: str = None
        self.__password: str = None
        self.__first_name: str = None
        self.__last_name: str = None
        self.__email: str = None

    @classmethod
    def set_params(cls, **kwargs):
        """ Set parameters for the user entity.

        Args:
            username (str): user's username
            password (str): user's password
            first_name (str): user's first name
            last_name (str): user's last name
            email (str): user's email address
        """
        cls.__identity: int = kwargs.get('identity')
        cls.__username: str = kwargs.get('username')
        cls.__password: str = kwargs.get('password')
        cls.__first_name: str = kwargs.get('first_name')
        cls.__last_name: str = kwargs.get('last_name')
        cls.__email: str = kwargs.get('email')

        return cls

    @property
    def identity(self):
        ''' Identity property getter '''
        return self.__identity

    @property
    def username(self):
        ''' Username property getter '''
        return self.__username

    @property
    def password(self):
        ''' Password property getter '''
        return self.__password

    @property
    def first_name(self):
        ''' First name property getter '''
        return self.__first_name

    @property
    def last_name(self):
        ''' Last name property getter '''
        return self.__last_name

    @property
    def email(self):
        ''' Email property getter '''
        return self.__email
