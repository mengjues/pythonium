class _None:

    def __and__(self, other):
        if other is True:
            return True
        return False

    def __or__(self, other):
        if other is True:
            return True
        return False        

    def __is__(self, other):
        if JS('other === self'):
            return True
        return False

    def __neg__(self):
        return True


__NONE = _None()
