# peptide_membrane_sim/simulation.py

import random
import numpy as np

class PeptideMembraneSimulator:
    def __init__(self, peptide_length=10, membrane_size=50, interaction_prob=0.1):
        self.peptide_length = peptide_length
        self.membrane_size = membrane_size
        self.interaction_prob = interaction_prob
        self.peptide = self.generate_peptide()
        self.membrane = self.generate_membrane()
    
    def generate_peptide(self):
        # Generate a random peptide sequence (string of amino acids)
        amino_acids = "ACDEFGHIKLMNPQRSTVWY"
        return ''.join(random.choices(amino_acids, k=self.peptide_length))
    
    def generate_membrane(self):
        # Represent membrane as a 2D NumPy array
        return np.zeros((self.membrane_size, self.membrane_size))
    
    def interact(self):
        # Simulate interactions by placing peptide randomly on membrane
        x, y = random.randint(0, self.membrane_size - 1), random.randint(0, self.membrane_size - 1)
        if random.random() < self.interaction_prob:
            self.membrane[x, y] += 1  # Simplified interaction representation
    
    def run_simulation(self, steps=1000):
        for _ in range(steps):
            self.interact()
    
    def display_membrane(self):
        print(self.membrane)

if __name__ == "__main__":
    sim = PeptideMembraneSimulator()
    sim.run_simulation()
    sim.display_membrane()

