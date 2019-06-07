from SublimeLinter.lint import ComposerLinter

class Tlint(ComposerLinter):
    cmd = ('tlint', 'lint', '${file}', '--json')
    regex = r'{\"line\":(?P<line>[0-9]+),\"message\":\"(?P<message>.*?)\",\"source\":\"(?P<source>.*?)\"}'
    multiline = True
    defaults = {
        'selector': 'source.php, text.blade, text.html.basic'
    }
