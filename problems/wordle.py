def get_wordle_result(solution, guess):
    result = ['_'] * 5
    solution_counts = {}
    guess_counts = {}

    for i in range(5):
        if guess[i] == solution[i]:
            result[i] = 'G'
        else:
            solution_counts[solution[i]] = solution_counts.get(solution[i], 0) + 1
            guess_counts[guess[i]] = guess_counts.get(guess[i], 0) + 1

    for i in range(5):
        if result[i] == '_':
            if guess[i] in solution_counts and solution_counts[guess[i]] > 0:
                if guess_counts[guess[i]] > 0:
                    result[i] = 'Y'
                    solution_counts[guess[i]] -= 1

    return ''.join(result)

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    solution = data[0]
    n = int(data[1])
    guesses = data[2:2 + n]
    
    results = []
    for guess in guesses:
        results.append(get_wordle_result(solution, guess))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
