from random import uniform

SEASON_GAMES = 82
WIN_PROB = 0.8
NUMBER_TRIALS = 100000

# https://math.stackexchange.com/questions/549309/probability-of-not-dropping-two-games-in-row
# by the stack exchange method the answer is 0.058817
# by simulation answer is ~0.0588

def sim_season_is_consec_loss(win_prob):
    won_last_game = True
    is_consec_loss_season = False
    for gamenum in range(0, SEASON_GAMES):
        won_this_game = (uniform(0, 1) <= win_prob)
        if not won_this_game and not won_last_game:
            return True
        won_last_game = won_this_game
    return False

# Slow and naive but most realistically simulating
#
# def simulate_season(win_prob):
#     season = []
#     for game in range(0, SEASON_GAMES):
#         game_won = (uniform(0, 1) <= win_prob)
#         season.append(game_won)
#     return season
#
# def is_consec_loss_season(season):
#     for gamenum in range(1, SEASON_GAMES):
#         if not season[gamenum] and not season[gamenum-1]:
#             return True
#     return False

def main():
    consec_loss_seasons = 0
    for num in range(0, NUMBER_TRIALS):
        if (num % 1000000 == 0 and num > 0):
            prob = float(consec_loss_seasons)/num
            print("")
            print("Finished " + str(num) + " trials ...")
            print("Consecutive Loss Seasons: " + str(consec_loss_seasons))
            print("Probability: " + str(1 - prob))
        if sim_season_is_consec_loss(WIN_PROB):
            consec_loss_seasons += 1
    prob = float(consec_loss_seasons)/NUMBER_TRIALS
    print("")
    print("Finished " + str(NUMBER_TRIALS) + " trials...")
    print("Consecutive Loss Seasons: " + str(consec_loss_seasons))
    print("Probability: " + str(1 - prob))

if __name__ == "__main__":
    main()
