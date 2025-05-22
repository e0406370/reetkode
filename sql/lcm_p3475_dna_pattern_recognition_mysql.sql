/*
  LCM 3475. DNA Pattern Recognition
  -> MySQL

  Table: Samples

  +----------------+---------+
  | Column Name    | Type    | 
  +----------------+---------+
  | sample_id      | int     |
  | dna_sequence   | varchar |
  | species        | varchar |
  +----------------+---------+
  - sample_id is the unique key for this table.
  - Each row contains a DNA sequence represented as a string of characters (A, T, G, C) and the species it was collected from.
  
  Biologists are studying basic patterns in DNA sequences. Write a solution to identify sample_id with the following patterns:
  - Sequences that start with ATG (a common start codon)
  - Sequences that end with either TAA, TAG, or TGA (stop codons)
  - Sequences containing the motif ATAT (a simple repeated pattern)
  - Sequences that have at least 3 consecutive G (like GGG or GGGG)
  
  Return the result table ordered by sample_id in ascending order.
*/

SELECT sample_id, dna_sequence, species,
    IF(left(dna_sequence, 3) = 'ATG', 1, 0) AS has_start,
    IF(right(dna_sequence, 3) IN ('TAA', 'TAG', 'TGA'), 1, 0) AS has_stop,
    IF(dna_sequence LIKE '%ATAT%', 1, 0) AS has_atat,
    IF(dna_sequence REGEXP 'G{3,}', 1, 0) AS has_ggg
FROM Samples
ORDER BY 1 ASC