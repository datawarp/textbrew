from __future__ import absolute_import

import re
from .transforms import BaseRegex, MergeSpaces


def process_regex(data, regex):
    return regex.process(data)


class RegexStudio(object):
    u"""
    Common Regex operations for text cleaning and matching.
    """

    def __init__(self, spl_chars=u''):
        u"""
        Constructor for RegexStudio, sets up regex patterns

        :param spl_chars: str: special characters to ignore for cleaning purposes(eg: '_|$')
        """

    def add_escape_chars(self, text):
        u"""
        Adds escape characters in a string
        to make it regex complaint

        :param text: str

        :returns text
        """
        # Get a list of all unique special characters
        spl_chars = list(set(re.findall(u"[^A-Za-z0-9,\s]", text)))

        # Append special characters with escape characters
        for char in spl_chars:
            text = text.replace(char, u'\\' + char)

        return text

    def extract_substrings(self, text, start=u'^', end=u'$'):
        u"""
        Extracts sub strings between two words.

        By default the initial sub-string is set to start
        of string and end sub-string is set to end of string.

        :param text: str: Input String
        :param start: Start word/character for substring
        :param end: End word/character for substring

        :returns: list: of str: list of matches
        """
        start = self.add_escape_chars(start)
        end = self.add_escape_chars(end)

        substring_regex = u'.*' + start + u'(.*?)' + end
        matches = re.findall(substring_regex, text)

        return matches

    def cleaner(self, text, regexes=[MergeSpaces]):
        u"""
        Removes charactes with 'True' values in the argument
        from the input string.

        :param text: str: Input text
        :param url: bool: Removes urls
        :param hashtag:  bool: Removes hashtags
        :param username: bool: Removes Usernames(starting with '@')
        :param alpha_only: bool: Keep Alphabets
        :param alnum: bool: Keep Alphanumerics
        :param in_parenthesis: bool: Removes text within parenthesis
        :param merge_spaces: bool: Merge consecutive white spaces

        :returns text: str: Filtered text
        """
        # Removes urls, on by default
        # if url == False:
        #     text = re.sub(self.regex_url,'',text)

        # # Removes hashtags, on by default
        # if hashtag == False:
        #     text = re.sub(self.regex_hashtag,'',text)

        # # Removes username (starting with '@'), on by default
        # if username == False:
        #     text = re.sub(self.regex_username,'',text)

        # # Returns only alphabets, off by default
        # if alpha_only == True:
        #     text = " ".join(re.findall(self.regex_alpha_only,text))

        # # Returns only alphanumerics, on by default
        # if alnum == True:
        #     text = " ".join(re.findall(self.regex_alnum,text))

        # # Removes text within parenthesis, on by default
        # if in_parenthesis == False:
        #     text = re.sub(self.regex_in_parenthesis,'',text)

        # # Replaces consecutive whitespaces, tab spaces
        # # & new-line characters with a single space
        # # FIX THIS!!!
        # if merge_spaces == True:
        #     text = re.sub(self.regex_merge_spaces,' ',text)
        if isinstance(regexes, BaseRegex):
            regexes = [regexes]
        return reduce(process_regex, regexes, text)

    def findall(self, regex, text):
        u"""
        Finds all regex matches in a text string

        :param regex: str: regex pattern to be searched for
        :param text: str

        :returns matches: list: of str: matched patterns
        """
        matches = re.findall(regex, text)
        return matches

    def matcher(self, text):
        u"""
        Create a dictionary for all the properties(parts of text) and matches in constructor

        :param text: str
        :return matches: dict: dictionary of part of text and matches
        """

        matches = dict()

        # Iterate through all the properties on this class(see constructor)
        for arg, regex in self.__dict__.items():
            key = u"_".join(arg.split(u"_")[1:])
            matches[key] = self.findall(regex, text)

        # Pop 'merge_spaces' from the dictionary
        matches.pop(u'merge_spaces')

        return matches
