class LoggableList(list, Loggable):

    def append(self, __object):
        self.log(__object)
        super().append(__object)
