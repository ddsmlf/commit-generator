from itertools import permutations

def solve_cryptarithmetic(puzzle):
    words = puzzle.split()
    left = words[:len(words)-1]
    right = words[-1]
    
    letters = set()
    for word in left:
        for c in word:
            if c != ' ':
                letters.add(c)
    for word in right:
        for c in word:
            if c != ' ' and c not in letters:
                letters.add(c)
                
    words_sorted = sorted(letters)
    n = len(words_sorted)
    
    def is_valid(assignment):
        try:
            left_num = 0
            for i, letter in enumerate(left):
                num = assignment[letter]
                if num == 0 and (i == 0 or letter in right):
                    return False
                if letter != ' ':
                    left_num += int(num) * 10**(len(letter)-1)
            right_num = int(assignment[right])
            return left_num + permutation_sum(left, assignment) == permutation_sum(right, assignment)
        except KeyError as e:
            return False
    
    def permutation_sum(word, assignment):
        total = 0
        for c in word:
            if c not in assignment or assignment[c] is None:
                return -1
            total += int(assignment[c]) * 10**(len(c)-1)
        return total
    
    from itertools import permutations
    letters_list = list(words_sorted)
    for perm in permutations('0123456789', n):
        if is_valid(dict(zip(words_sorted, perm))):
            print(f"Solution trouvée : {dict(zip(words_sorted, perm))}")
            return
    print("Aucune solution trouvée.")

puzzle = input().strip()
solve_cryptarithmetic(puzzle)