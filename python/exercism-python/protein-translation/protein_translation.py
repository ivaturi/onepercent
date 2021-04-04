codons_acids = {
    'AUG' : 'Methionine',
    'UUU' : 'Phenylalanine',
    'UUC' : 'Phenylalanine',
    'UUA' : 'Leucine',
    'UUG' : 'Leucine',
    'UCU' : 'Serine',
    'UCC' : 'Serine',
    'UCA' : 'Serine',
    'UCG' : 'Serine',
    'UAU' : 'Tyrosine',
    'UAC' : 'Tyrosine',
    'UGU' : 'Cysteine',
    'UGC' : 'Cysteine',
    'UGG' : 'Tryptophan',
}
codons_stop = ['UAA', 'UAG', 'UGA']

def proteins(strand, codon_size = 3):
    proteins = []
    codons = [strand[i:i+codon_size] for i in range(0, len(strand), codon_size)] 
    for codon in codons:
        if codon in codons_stop:
            break
        elif codon in codons_acids:
            proteins.append(codons_acids[codon])
    return proteins    