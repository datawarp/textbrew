from __future__ import absolute_import

import re
import numpy as np
from spacy.en import English

PARSER = English()


class Format(object):

    def __init__(self, lower = True):
    	u"""
        Constructor for 'Format' class.

        :param lower: bool: Lowercases the text
        """
        self.lower = lower

    def compound_nouns(self, text, nnp_sep=u"_", nn_sep=u"|"):
        u"""
        Combines Noun Phrases into a single token
        (with separators as provided in arguments)

        :param text: str: String to be formatted
        :param nnp_sep: str: Separator for 'NNP' tokens
        :param nn_sep: str: Separator for 'NN' tokens

        :returns text: str: Formatted string
        """

        # Parse the 'text' through Spacy Parser
        parsed_doc = PARSER(text)

        # Merge noun phrases
        for phrase in parsed_doc.noun_chunks:
            phrase.merge(phrase.root.tag_, phrase.text, phrase.root.ent_type_)

        # Placeholder for formatted text
        text = u""

        for token in parsed_doc:
            # Reformatted phrase
            phrase = u""

            # Replaces white spaces between words in a phrase
            # with appropriate separators
            if token.tag_ == u"NNP":
                phrase = token.text.replace(u" ", nnp_sep)
            elif token.tag_ == u"NN":
                phrase = token.text.replace(u" ", nn_sep)
            else:
                phrase = token.text
            text += phrase + u" "

        # If 'lower' argument is true then lowercase the text
        if self.lower:
            text = text.lower()
        return text
