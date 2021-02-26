"""
one light style based on vim-one

.. _vim-one: https://github.com/rakr/vim-one
"""
from pygments.style import Style
from pygments.token import Token, Comment, Name, Keyword, Generic, Number
from pygments.token import Operator, String, Text, Error

BASE03 = '#FAFAFA'
BASE02 = '#A0A0A0'
BASE01 = '#A0A1A7'
BASE00 = '#526EFF'
BASE0 = '#383A42'
BASE1 = '#5B5E6B'
BASE2 = '#696C77'
BASE3 = '#A0A1A7'
YELLOW = '#986801'
ORANGE = '#C18401'
RED = '#E45649'
MAGENTA = '#CA1243'
VIOLET = '#A626A4'
BLUE = '#4078F2'
CYAN = '#0184BC'
GREEN = '#50A14F'

class OneLightStyle(Style):
    color = BASE1
    background_color = BASE03
    highlight_color = BASE00

    styles = {
        Text: BASE1,

        Keyword: VIOLET,
        Keyword.Constant: BLUE,
        Keyword.Declaration: VIOLET,
        #Keyword.Namespace
        #Keyword.Pseudo
        Keyword.Reserved: BLUE,
        Keyword.Type: BLUE,

        Name: BASE1,
        Name.Attribute: BASE1,
        Name.Builtin: RED,
        Name.Builtin.Pseudo: VIOLET,
        Name.Class: BLUE,
        Name.Constant: ORANGE,
        Name.Decorator: BLUE,
        Name.Entity: ORANGE,
        Name.Exception: ORANGE,
        Name.Function: BLUE,
        #Name.Label
        #Name.Namespace
        #Name.Other
        Name.Tag: BLUE,
        Name.Variable: BLUE,
        #Name.Variable.Class
        #Name.Variable.Global
        #Name.Variable.Instance

        #Literal
        #Literal.Date
        String: GREEN,
        String.Backtick: BASE01,
        String.Char: GREEN,
        String.Doc: GREEN,
        #String.Double
        String.Escape: ORANGE,
        String.Heredoc: BASE1,
        #String.Interpol
        #String.Other
        String.Regex: RED,
        #String.Single
        #String.Symbol

        Number: YELLOW,
        #Number.Float
        #Number.Hex
        #Number.Integer
        #Number.Integer.Long
        #Number.Oct

        Operator: GREEN,
        #Operator.Word

        #Punctuation: ORANGE,

        Comment: BASE01,
        #Comment.Multiline
        Comment.Preproc: GREEN,
        #Comment.Single
        Comment.Special: GREEN,

        #Generic
        Generic.Deleted: VIOLET,
        Generic.Emph: 'italic',
        Generic.Error: RED,
        Generic.Heading: ORANGE,
        Generic.Inserted: BLUE,
        #Generic.Output
        #Generic.Prompt
        Generic.Strong: 'bold',
        Generic.Subheading: ORANGE,
        #Generic.Traceback

        Token: BASE1,
        Token.Other: ORANGE,
    }
