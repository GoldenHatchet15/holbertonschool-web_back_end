#!/usr/bin/env python3
"""
DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import NoResultFound, InvalidRequestError
from user import Base, User


class DB:
    """DB class to manage the database connection and operations"""

    def __init__(self) -> None:
        """Initialize a new DB instance"""
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object"""
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Add a new user to the database"""
        new_user = User(email=email, hashed_password=hashed_password)
        self._session.add(new_user)
        self._session.commit()
        return new_user

    def find_user_by(self, **kwargs) -> User:
        """Find a user in the database based on keyword arguments

        Args:
            **kwargs: Arbitrary keyword arguments for filtering the user

        Returns:
            User: The first user found matching the criteria

        Raises:
            NoResultFound: If no user is found
            InvalidRequestError: If an invalid query argument is passed
        """
        try:
            return self._session.query(User).filter_by(**kwargs).one()
        except NoResultFound:
            raise NoResultFound("No user found with the provided arguments.")
        except InvalidRequestError:
            raise InvalidRequestError("Invalid query argument(s) provided.")

    def update_user(self, user_id: int, **kwargs) -> None:
        """Update a user's attributes

        Args:
            user_id (int): The user's ID
            **kwargs: Arbitrary keyword arguments for attributes to update

        Raises:
            ValueError: If any argument does not correspond to a valid attribute
        """
        user = self.find_user_by(id=user_id)

        for key, value in kwargs.items():
            if not hasattr(user, key):
                raise ValueError(f"'{key}' is not a valid attribute of User")
            setattr(user, key, value)

        self._session.commit()
