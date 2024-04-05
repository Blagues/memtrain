from memory.memoryTrainer import *
from memory.numbersQAGenerator import *

rand_nrs = generate_number_rows_and_qa(5, 5, 5)
display_memory_sequence(rand_nrs[0], rand_nrs[1], 5, 60)