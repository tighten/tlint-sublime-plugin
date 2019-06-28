from SublimeLinter.lint import ComposerLinter

class Tlint(ComposerLinter):
    cmd = ('tlint', 'lint', '${file_on_disk}', '--json')
    tempfile_suffix = '-'
    regex = r'{\"line\":(?P<line>[0-9]+),\"message\":\"(?P<message>.*?)\",\"source\":\"(?P<source>.*?)\"}'
    multiline = True
    defaults = {
        'selector': 'source.php, text.blade, text.html.basic'
    }
