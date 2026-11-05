from urllib.request import urlopen
def get_sequence(uniprot_id):
    url = f"https://rest.uniprot.org/uniprotkb/{uniprot_id}.fasta"
    fasta_text = urlopen(url).read().decode()
    lines = fasta_text.splitlines()
    return "".join(lines[1:])

def residue_at(sequence, position):
    return sequence[position - 1]  # Convert to 0-based index

orf1 = get_sequence("Q9UN81")
orf2 = get_sequence("O00370")
print("ORF1p length:", len(orf1))
print("ORF2p length:", len(orf2))


print("K129:", residue_at(orf1, 129))
print("K337:", residue_at(orf1, 337))
print("K234:", residue_at(orf2, 234))
print("K793:", residue_at(orf2, 793))
print("K1236:", residue_at(orf2, 1236))
