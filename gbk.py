from Bio import Entrez

if __name__ == '__main__':
    Entrez.email = "alicewan0426@gmail.com"
    term = '("Amphigerontia"[Organism] AND 2005/08/16[PDAT] : 2009/01/18[PDAT]'
    # handle = Entrez.esearch(db="nucleotide", term='"Zea mays"[Organism] AND rbcL[Gene]')
    handle = Entrez.esearch(db="nucleotide", term=term)
    record = Entrez.read(handle)

    print(record["Count"])