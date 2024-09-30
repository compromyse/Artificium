def can_win(words, current_word, used_words, memo):
    state = (current_word, tuple(used_words))
    if state in memo:
        return memo[state]
    
    last_char = current_word[-1] if current_word else None
    
    for i, word in enumerate(words):
        if not used_words[i] and (last_char is None or word[0] == last_char):
            used_words[i] = True
            if not can_win(words, word, used_words, memo):
                used_words[i] = False
                memo[state] = True
                return True
            used_words[i] = False
    
    memo[state] = False
    return False

def determine_winner(words):
    n = len(words)
    used_words = [False] * n
    memo = {}
    
    if can_win(words, None, used_words, memo):
        return "Alice"
    else:
        return "Bob"

# Read input
n = int(input())
words = [input().strip() for _ in range(n)]

# Determine the winner
print(determine_winner(words))
