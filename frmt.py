from Bio import Entrez, SeqIO

def read_data():
    file = open("data.txt", "r")
    entries = file.readline().split()
    file.close

    return entries

if __name__ == '__main__':
    entries = read_data()

    Entrez.email = "alicewan0426@gmail.com"
    handle = Entrez.efetch(db="nucleotide", id=entries, rettype="fasta")
    records = list(SeqIO.parse(handle, "fasta"))

    idx = 0
    for i, record in enumerate(records):
        if len(record.seq) < len(records[0].seq):
            idx = i

    shortest = records[idx]
    print(f">{shortest.description}")
    print(shortest.seq)

