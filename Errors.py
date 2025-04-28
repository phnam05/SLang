class SLangBaseError(Exception):
    def __init__(self, message, ctx=None):
        self.ctx = ctx
        if ctx and hasattr(ctx, 'start'):
            self.line = ctx.start.line
            self.column = ctx.start.column
            self.text = ctx.start.text
        else:
            self.line = None
            self.column = None
            self.text = "<unknown>"
        super().__init__(self._format_message(message))

    def _format_message(self, msg):
        if self.line is not None:
            return f"{self.__class__.__name__.replace('Error', 'OOPsie')}: {msg} at line {self.line}, column {self.column}: '{self.text}'"
        return f"{self.__class__.__name__.replace('Error', 'OOPsie')}: {msg}"

class SLangSyntaxError(SLangBaseError): pass
class SLangNameError(SLangBaseError): pass
class SLangValueError(SLangBaseError): pass
class SLangTypeError(SLangBaseError): pass
class SLangIndexError(SLangBaseError): pass
