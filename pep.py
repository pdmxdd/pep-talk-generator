from random import choice
from csv import reader

def load_piece(filepath):
    data = []
    with open(filepath, 'r') as read_file:
        rows = reader(read_file, delimiter='\t')
        for row in rows:
            data.append(row[0])
    return data

PIECE_ONE = load_piece('data/piece_one.csv')
PIECE_TWO = load_piece('data/piece_two.csv')
PIECE_THREE = load_piece('data/piece_three.csv')
PIECE_FOUR = load_piece('data/piece_four.csv')



def random_pep():
    pep = "{} {} {} {}".format(choice(PIECE_ONE), choice(PIECE_TWO), choice(PIECE_THREE), choice(PIECE_FOUR))
    return pep