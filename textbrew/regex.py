import re

class RegexStudio(object):
    """
    Common Regex operations for text cleaning and matching.
    """    
    
    def __init__(self, spl_chars = ''):
        """
        Constructor for RegexStudio, sets up regex patterns

        :param spl_chars: str: special characters to ignore for cleaning purposes(eg: '_|$')
        """
        spl_chars = self.add_escape_chars(spl_chars)
        
        self.regex_url = 'https*\S*|www.\S*.\S'
        self.regex_hashtag = '(?<=\s)#\S+|(?<=^)#\S+'
        self.regex_username = '@[^\s@]+' 
        self.regex_alpha_only = "[A-Za-z"+spl_chars+"]+"
        self.regex_alnum = "[A-Za-z0-9"+spl_chars+"]+"
        self.regex_in_parenthesis = '.*(\(.*?\))'
        self.regex_merge_spaces = '\s\s+'
                
    def add_escape_chars(self, text):
        """
        Adds escape characters in a string
        to make it regex complaint
        
        :param text: str
        
        :returns text
        """        
        # Get a list of all unique special characters
        spl_chars = list(set(re.findall("[^A-Za-z0-9,\s]",text)))
        
        # Append special characters with escape characters
        for char in spl_chars:
            text = text.replace(char,'\\'+char)
            
        return text
    
    def extract_substrings(self, text, start='^', end='$'):
        """
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
        
        substring_regex = '.*'+start+'(.*?)'+end
        matches = re.findall(substring_regex,text)
        
        return matches
    
    def cleaner(self, text, url = False, hashtag = False,
                    username = False, alpha_only = False, alnum = True,
                    in_parenthesis = False, merge_spaces = True):        
        """
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
        if url == False:
            text = re.sub(self.regex_url,'',text)
        
        # Removes hashtags, on by default
        if hashtag == False:
            text = re.sub(self.regex_hashtag,'',text)
        
        # Removes username (starting with '@'), on by default    
        if username == False:
            text = re.sub(self.regex_username,'',text)
        
        # Returns only alphabets, off by default
        if alpha_only == True:
            text = " ".join(re.findall(self.regex_alpha_only,text))
        
        # Returns only alphanumerics, on by default
        if alnum == True:
            text = " ".join(re.findall(self.regex_alnum,text))
        
        # Removes text within parenthesis, on by default
        if in_parenthesis == False:
            text = re.sub(self.regex_in_parenthesis,'',text)
        
        # Replaces consecutive whitespaces, tab spaces
        # & new-line characters with a single space
        # FIX THIS!!!
        if merge_spaces == True:           
            text = re.sub(self.regex_merge_spaces,' ',text)
            
        return text
    
    def findall(self, regex, text):
        """
        Finds all regex matches in a text string

        :param regex: str: regex pattern to be searched for
        :param text: str

        :returns matches: list: of str: matched patterns
        """        
        matches = re.findall(regex, text)
        return matches
        
    def matcher(self, text):
        """
        Create a dictionary for all the properties(parts of text) and matches in constructor

        :param text: str
        :return matches: dict: dictionary of part of text and matches
        """
        
        matches = dict()

        # Iterate through all the properties on this class(see constructor)
        for arg, regex in self.__dict__.items():
            key = "_".join(arg.split("_")[1:])
            matches[key] = self.findall(regex, text)
            
        # Pop 'merge_spaces' from the dictionary
        matches.pop('merge_spaces')
        
        return matches
