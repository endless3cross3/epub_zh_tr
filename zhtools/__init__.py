from zhtools.langconv import Converter


def simple2tradition(line: str) -> str:
    """將簡體轉換成繁體"""
    line = Converter('zh-hant').convert(line)
    return line


def tradition2simple(line: str) -> str:
    """將繁體轉換成簡體"""
    line = Converter('zh-hans').convert(line)
    return line
