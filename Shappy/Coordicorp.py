import math
import shap

"""
Shapley value calculation basic example from wikipedia with glove game - https://en.wikipedia.org/wiki/Shapley_value#Glove_game
"""

player_list = ['L1','L2','R'] #L1-left glove, L2-second left glove, R-right glove from wikipedia example
coalition_dictionary = {'L1' : 0, 'L2': 0, 'R': 0, 'L1,R': 1, 'L2,R': 1, 'L1,L2': 0, 'L1,L2,R': 1} #characteristic functions of each coalition's payoff
g = shap.Coop_Game(player_list, coalition_dictionary) #shapley calculation
print g.shapley() #one can interpret Shapley values quantitatively either as the power of each player, or as the amount of money each player fairly deserves
#in this case, if we are splitting a $1, then R is entitled to $0.66 and L1,L2 are entitled to $0.16 if they want to be a part of a grand coalition


"""
Shapley value calculations for case A, case B, subgame of case A with 500 people, subgame of case A with 500 people split up into 2, case A with 4 groups of 250 people
"""


print 'Case A - Big game - no core exists - grouped 1000 people into 500 people as players v1,v2 - non stable since Shapley values are below v1,2s characteristic functions'

player_list = ['vc','v1','v2']
coalition_dictionary = {'vc' : 0, 'v1':500000, 'v2':500000, 'v1,v2':1000000, 'vc,v1':1000000, 'vc,v2':1000000, 'vc,v1,v2':1000000}
# vc=0 because Coordicorp can't get anything done by itself
# v1,v2=1,000,000 because all 1000 can just work for $1000 giving in total $1,000,000
# vc,v1,v2 is 1,000,000 because you have the 1000 people just work on a project the return of which is still $1,000,000
# changing vc,v1,v2 above 1,250,000 will start making this game stable and Shapley's v1,v2 >500,000, people may be interested in forming coalitions
g = shap.Coop_Game(player_list, coalition_dictionary)
print g.shapley()


print 'Case B - Big game - no core exists - grouped 1000 players into 500 players of v1,v2'

player_list = ['v1','v2']
coalition_dictionary = { 'v1':500000, 'v2':500000, 'v1,v2': 1000000}
g = shap.Coop_Game(player_list, coalition_dictionary)
print g.shapley()

# One can quantitatively compare the Shapley values v1,v2 of case A with case B!


print 'Case A - subgame 1 player (500 people) + Coordicorp - core present - Shapley value result is $750,000 to 500 people and $250,000 to Coordicorp just as in your post'
# note that this does not factor into account the other 500 people of v2
player_list = ['vc', 'v1']
coalition_dictionary = {'vc' : 0, 'v1':500000, 'vc,v1':1000000}
g = shap.Coop_Game(player_list, coalition_dictionary)
print g.shapley()


print 'Case A - subgame 2 players + Coordicorp - we split up the 500 people of v1 into 2 250 groups v1_1, v1_2 - core present'
# note that this does not factor into account the other 500 people of v2
# the more split up the 500 people are, the more the 500 people demand from Coordicorp since they're more disorganized and Coordicorp has to persuade all of the 500 of v1
# note again that the other 500 people of v2 are not taken into account, which allows all of the disorganized 500 people of v1 to have more leverage as exhibited by Shapley values
player_list = ['vc', 'v1_1','v1_2']
coalition_dictionary = {'vc' : 0, 'v1_1':250000, 'v1_2':250000, 'v1_1,v1_2':500000, 'vc,v1_1':0, 'vc,v1_2':0, 'vc,v1_1,v1_2':1000000}
#vc=0 because Coordicorp alone can't do anything
#v1_1=v1_2=250,000 if 250 people work for $1000 by themselves
#v1_1,v1_2=500,000 if 500 people work for $1000 together
#vc,v1_1=vc,v1_2=0 - vc can't finish a building with 250 people
g = shap.Coop_Game(player_list, coalition_dictionary)
print g.shapley()


print 'Case A - Big game with 4(v1,v2,v3,v4) 250 people groups and 1 corp - non stable grand coalition since Shapley values are below v1,2,3,4s characteristic functions v(1234)=$250,000>Shapley v(1234)=$225,000'
# we now go back to the big game of case A and add 4 groups of 250
# vc needs at least 2 250 people groups to get to $1,000,000
player_list = ['vc','v1','v2','v3','v4']
coalition_dictionary = {'vc' : 0, 'v1':250000, 'v2':250000, 'v3':250000, 'v4':250000,  \
                        'v1,v2':500000, 'v1,v3':500000, 'v2,v3':500000, 'v1,v4':500000, 'v2,v4':500000,  'v3,v4':500000, 'vc,v1':0, 'vc,v2':0, 'vc,v3': 0, 'vc,v4': 0,\
                        'vc,v1,v2':1000000, 'vc,v1,v3':1000000, 'vc,v2,v3':1000000, 'vc,v1,v4':1000000, 'vc,v2,v4':1000000, 'vc,v3,v4':1000000,\
                        'v1,v2,v3':750000, 'v1,v2,v4':750000, 'v1,v3,v4':750000, 'v2,v3,v4':750000,\
                        'vc,v1,v2,v3': 1000000 , 'vc,v1,v2,v4': 1000000, 'vc,v1,v3,v4': 1000000, 'vc,v2,v3,v4': 1000000 , 'v1,v2,v3,v4': 1000000 , \
                        'vc,v1,v2,v3,v4':1000000
                        }
g = shap.Coop_Game(player_list, coalition_dictionary)
print g.shapley()

print 'One can expand the amount of players v1 to v1000, but the size of the characteristic function would be 2**1001 which is why I stopped at 5 players'

#What's also interesting is the Shapley value of Coordicorp (v(c)) is in each example, since if it's above 0, Coordicorp has an incentive to create coalitions, it's just that the other 1000 players may not be interested in joining
