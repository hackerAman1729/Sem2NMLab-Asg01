def print_nucleotide_frequency(sequence_name, sequence_data):
  print(sequence_name)
  nucleotide_frequency = {nucleotide: sequence_data.count(nucleotide) for nucleotide in set(sequence_data)}
  for nucleotide, count in sorted(nucleotide_frequency.items()):
      print(f'{nucleotide}: {count}')

def update_sequence_counts(sequence_data, sequence_counts):
  for nucleotide in sequence_data:
      if nucleotide not in sequence_counts:
          sequence_counts[nucleotide] = 0
      sequence_counts[nucleotide] += 1
  return sequence_counts

def read_fasta(filepath):
  with open(filepath, 'r') as file:
      sequence_name = ''
      sequence_data = ''
      total_nucleotide_count = 0
      sequence_counts = {}
      num_sequences = 0

      for line in file:
          line = line.strip()
          if line.startswith('>'):
              if sequence_data:
                  print_nucleotide_frequency(sequence_name, sequence_data)
                  total_nucleotide_count += len(sequence_data)
                  sequence_counts = update_sequence_counts(sequence_data, sequence_counts)
                  num_sequences += 1
                  sequence_data = ''
              sequence_name = line[1:]
          else:
              sequence_data += line

      if sequence_data:
          print_nucleotide_frequency(sequence_name, sequence_data)
          total_nucleotide_count += len(sequence_data)
          sequence_counts = update_sequence_counts(sequence_data, sequence_counts)
          num_sequences += 1

  average_counts = {nucleotide: count / num_sequences for nucleotide, count in sequence_counts.items()}
  print(f'Total nucleotide count: {total_nucleotide_count}')
  print(f'Average base count per sequence:')
  for nucleotide, average in sorted(average_counts.items()):
      print(f'{nucleotide}: {average}')


file_path = 'seq.fa'
read_fasta(file_path)
