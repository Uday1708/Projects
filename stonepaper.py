import random

def play():
    user = input("What's your choice? 'r' for rock , 'p' for paper , 's' for scissor\n")
    
    computer = random.choice(['r','p','s'])

    if(user == computer):
        return 'Its a tie'
    if is_win(user , computer):
        return 'You Win!!'
    
    return 'You Lost!!'

def is_win(player , opponent):
    #r>s , p>r , s>p
    if (player == 'r' and opponent == 's' or player == 'p' and opponent == 'r' or player == 's' and opponent == 'p'):
        return True
    
if __name__ == '__main__':
    
    res = play()
    
    print(res)