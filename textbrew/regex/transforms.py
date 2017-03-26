import re
from .utils import extract_sub_args


class BaseRegex:
    '''
    Base Class to Define Regular Expressions.
    The idea of using classes to implement Regexes is to provide an abstraction
    which would allow users to control the operation of regex.
    re.find , re.findall are some direct operations one can do , but at times
    user might want a further level of cleaning.
    The abstraction would just allow the user to define custom regex
    functionality simply by:

    from textbrew.regex import BaseRegex

    class MyRegex():
            regex_string = #user re string

            def processor(self , data , **kwargs):
                    #This function, if not implemented , by default
                    # returns re.sub()
                    return #Do something

    Any internal usage would involve just involve :
    if isinstance( SomeRegex , BaseRegex) : return SomeRegex.process(data)
    '''
    @classmethod
    def __check(self, *args, **kwargs):
        assert hasattr(self, 'regex_string'), (
            'Regular Expression %s does not have a regex_string ' % (
                self.__name__)
        )

    @classmethod
    def process(self, data, *args, **kwargs):
        self.__check()
        if hasattr(self, 'processor'):
            return self.processor(**kwargs)
        return re.sub(self.regex_string, kwargs.get("replace", ''), data)

    @classmethod
    def findall(self, data):
        return re.findall(self.regex_string, data)


class URL(BaseRegex):
    regex_string = 'https*\S*|www.\S*.\S|([a-z]*\.[a-z]+\.?[a-z]{2,4}?)'


class HashTag(BaseRegex):
    regex_string = '(?<=\s)#\S+|(?<=^)#\S+'


class UserName(BaseRegex):
    regex_string = '@[^\s@]+'


class InParenthesis(BaseRegex):
    regex_string = '.*(\(.*?\))'


class MergeSpaces(BaseRegex):
    regex_string = '\s\s+'
    
class EmailID(BaseRegex):
    regex_string = '(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)'