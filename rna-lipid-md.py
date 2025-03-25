import random
import string

# Define L- and D- amino acids using standard 1-letter codes
L_amino_acids = [
    'A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G',
    'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S',
    'T', 'W', 'Y', 'V'
]

# For simplicity, represent D-amino acids with lowercase letters (mock representation)
D_amino_acids = [aa.lower() for aa in L_amino_acids]

# Combined set of L and D amino acids
LD_amino_acids = L_amino_acids + D_amino_acids

def generate_random_peptide(length=80):
    """Generate a single random peptide of given length with L and D amino acids."""
    return ''.join(random.choices(LD_amino_acids, k=length))

def generate_peptide_library(num_peptides=10000, length=80):
    """Generate a library of LD-random peptides."""
    return [generate_random_peptide(length) for _ in range(num_peptides)]

def save_peptide_library(peptides, filename="ld_peptide_library.fasta"):
    """Save the peptide library to a FASTA file."""
    with open(filename, 'w') as f:
        for i, seq in enumerate(peptides):
            f.write(f">peptide_{i+1}\n{seq}\n")

# Example usage
if __name__ == "__main__":
    print("Generating LD-random peptide library...")
    peptide_library = generate_peptide_library(num_peptides=1000, length=80)
    save_peptide_library(peptide_library)
    print("Saved 1000 LD-random peptides to 'ld_peptide_library.fasta'")

