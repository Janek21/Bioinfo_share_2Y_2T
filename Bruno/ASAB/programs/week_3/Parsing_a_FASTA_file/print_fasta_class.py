class Seq(object):
    '''
    >>> record = Seq()
    >>> record.id = "FAST_CAT"
    >>> record.seq = "FASTCAT"
    >>> print(record)
    >FAST_CAT
    FASTCAT
    >>> record = Seq()
    >>> record.id = "MANY_CATS"
    >>> record.seq = "CAT"*100
    >>> print(record)
    >MANY_CATS
    CATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCAT
    CATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCAT
    CATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCAT
    CATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCAT
    CATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCAT
    '''
    def __init__(self):
        self.id = ''
        self.seq = ''
    
    def __str__(self):
        resultado = f'>{self.id}'
        while self.seq != '':
            resultado += '\n'
            resultado += self.seq[:60]
            self.seq = self.seq[60:]
        return resultado


if __name__ == "__main__":
  import doctest
  doctest.testmod(verbose=True)

