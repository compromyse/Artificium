def determine_winner(N, rounds):
    alice_wins = 0
    bob_wins = 0
    
    for round_info in rounds:
        alice_seq, bob_seq, coin_tosses = round_info.split()
        
        alice_index = coin_tosses.find(alice_seq)
        bob_index = coin_tosses.find(bob_seq)
        
        if alice_index != -1 and (bob_index == -1 or alice_index < bob_index):
            alice_wins += 1
        elif bob_index != -1 and (alice_index == -1 or bob_index < alice_index):
            bob_wins += 1
        
    if alice_wins > bob_wins:
        return "Alice wins!"
    elif bob_wins > alice_wins:
        return "Bob wins!"
    else:
        return "Draw!"

N = int(input().strip())
rounds = [input().strip() for _ in range(N)]

print(determine_winner(N, rounds))
