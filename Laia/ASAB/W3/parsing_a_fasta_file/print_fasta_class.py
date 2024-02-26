class Seq(object):
    '''
    Constructor
    '''
    def __init__(self):
        self.id = ''
        self.seq = ''
    
    def __str__(self):
        header = f'>{self.id}\n'
        seq = []
        for i in range(0, len(self.seq), 60):
            seq.append(self.seq[i:i+60])

        fasta = header + '\n'.join(seq)
        return fasta


def main():
    record = Seq()
    record.id = "FAST_CAT"
    record.seq = "FASTCAT"
    print(record)

    record = Seq()
    record.id = "MANY_CATS"
    record.seq = "CAT" * 100
    print(record)

if __name__ == '__main__':
    main()