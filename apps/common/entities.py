''' This file provides abstract classes and methods
    related to entities development
'''
import abc


class AbstractEntity(abc.ABC):
    ''' This class represents an abstract class of entities '''

    @abc.abstractmethod
    def __init__(self):
        ''' Entity constructor method '''

    @abc.abstractmethod
    @classmethod
    def set_params(cls, **params) -> 'AbstractEntity':
        ''' This method sets the parameters of the entity '''
