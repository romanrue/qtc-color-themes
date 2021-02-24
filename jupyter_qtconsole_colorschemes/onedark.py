"""
A Pygments_ style based on the dark background variant of Solarized_.

.. _Pygments: http://pygments.org/
.. _Solarized: http://ethanschoonover.com/solarized
"""
from pygments.style import Style
from pygments.token import Token, Comment, Name, Keyword, Generic, Number
from pygments.token import Operator, String, Text, Error

BASE03 = '#282C34'
BASE02 = '#2E3642'
BASE01 = '#B5C2D9'
BASE00 = '#BBC2E0'
BASE0 = '#526488'
BASE1 = '#899AB8'
BASE2 = '#B5C2D9'
BASE3 = '#D8DCEE'
YELLOW = '#E5C07B'
ORANGE = '#FEA47F'
RED = '#E06C75'
MAGENTA = '#C678DD'
VIOLET = '#6C71C4'
BLUE = '#61AFEF'
CYAN = '#56B6C2'
GREEN = '#98C379'

class SolarizeddarkStyle(Style):
    color = BASE1
    background_color = BASE03
    highlight_color = BASE01

    styles = {
        Text: BASE1,

        Keyword: GREEN,
        Keyword.Constant: ORANGE,
        Keyword.Declaration: BLUE,
        #Keyword.Namespace
        #Keyword.Pseudo
        Keyword.Reserved: BLUE,
        Keyword.Type: RED,

        Name: BASE1,
        Name.Attribute: BASE1,
        Name.Builtin: YELLOW,
        Name.Builtin.Pseudo: BLUE,
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
        String: CYAN,
        String.Backtick: BASE01,
        String.Char: CYAN,
        String.Doc: CYAN,
        #String.Double
        String.Escape: ORANGE,
        String.Heredoc: BASE1,
        #String.Interpol
        #String.Other
        String.Regex: RED,
        #String.Single
        #String.Symbol

        Number: CYAN,
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
        Generic.Deleted: CYAN,
        Generic.Emph: 'italic',
        Generic.Error: RED,
        Generic.Heading: ORANGE,
        Generic.Inserted: GREEN,
        #Generic.Output
        #Generic.Prompt
        Generic.Strong: 'bold',
        Generic.Subheading: ORANGE,
        #Generic.Traceback

        Token: BASE1,
        Token.Other: ORANGE,
    }
