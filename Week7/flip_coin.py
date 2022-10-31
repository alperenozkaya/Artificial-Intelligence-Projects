from scipy import stats
from scipy.stats import binom

# assumed that the program shows how many heads have been observed

def flip_coin_fair(states, prob):

    coin_flip = binom.rvs(n=states, p=prob, size=1)  # coin flipped n times and assumed it is fair by giving the
    # probability 0.50
    print('number of heads:', coin_flip)  # number of heads seen in the generated n states
    is_fair = stats.binom_test(coin_flip, n=states, p=0.5, alternative='greater')  # a test function to test whether the coin flip is fair or not p=?
    # if the p value is less than 0.05 it can be concluded that the coin is unfair
    print('In', states, 'states the p value is:', is_fair)


def main():
    print('Enter the number of states for a coin flip:')
    num_states = int(input())
    print('Enter the probability of showing heads ')
    prob_heads = float(input())
    flip_coin_fair(num_states, prob_heads)

main()



