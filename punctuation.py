import re

with open('Corpus.txt', 'r') as content_file:
    content = content_file.read()

replacement_patterns = [
    # "()" => " () "
    (r"\)", ") "),
    (r"\(", " ("),
    # "[]" => " [] "
    (r"\]", '] '),
    (r"\[", ' ['),

    (r"[ ]{2,}", ' '),  # space more than one
    (r"\n\n", '\n'), # omit repeated new lines!

    # " , " or "," => ", "
    (r" ، ", ', '),
    (r" ،", ', '),
    (r"\s\.\s", '. '),
    (r"\s\.(?!\.) ", '. '),  # not .. or ... just .
    (r"\s\.\.\.", '... '), # omit space if space exist before ...
    # ( ) => ()
    (r"\s\)", ')'),
    (r"\(\s", '('),
    # [ ] => []
    (r"\s\]", ']'),
    (r"\[\s", '['),

    (r"\s:", ':'),# omit space if space exist before :
    (r":(?!\s)", ': ') # add space if space exist before ...
]


class RegexpReplacer(object):

    def __init__(self, patterns=replacement_patterns):
        # Fixed this line - "patterns", not "pattern"
        self.patterns = [(re.compile(regex), repl) for (regex, repl) in patterns]

    def replace(self, text):
        s = text
        for (pattern, repl) in self.patterns:
            (s, count) = re.subn(pattern, repl, s)
        return s

rep=RegexpReplacer()
content = rep.replace(content)

with open('new.txt', 'w') as the_file:
    the_file.write(content)
