def read_data():
    file = open("data.txt", "r")
    line = file.readline()
    file.close

    return line

def count_bases(dna):
    return dna.count("A"), dna.count("C"), dna.count("G"), dna.count("T")

if __name__ == '__main__':
    dna = read_data()
    A_count, C_count, G_count, T_count = count_bases(dna)
    print(A_count, C_count, G_count, T_count)