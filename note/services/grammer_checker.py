import atexit
import threading

import language_tool_python

_tool = None
_tool_lock = threading.Lock()


def get_grammar_tool():
    global _tool

    with _tool_lock:
        if _tool is None:
            _tool = language_tool_python.LanguageTool("en-US")

    return _tool


def check_grammar(text):
    tool = get_grammar_tool()

    with _tool_lock:
        return tool.check(text)


def close_grammar_tool():
    global _tool

    with _tool_lock:
        if _tool is not None:
            _tool.close()
            _tool = None


atexit.register(close_grammar_tool)