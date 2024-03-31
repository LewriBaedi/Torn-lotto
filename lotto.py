import pandas as pd
import random as rng

n = int(input('Please enter number of winners:')   # Enter number of prizes here
path = raw_input('Please enter the system path to the chain report csv:') # Enter csv path between quote marks
limit = 100 #minimum number of attacks

df = pd.read_csv(path, sep = ';',skiprows=1)
entries = df.Attacks[df.Attacks > limit] - limit

picks = []
sub = 0
for i in entries:
    sub += i
    picks.append(sub)

if sub < n:
    print('Error: more prizes than entries.')
    raise SystemExit()

draws = rng.sample(range(1, sub+1), n)
winners = []
for draw in draws:
    winner = next(filter(lambda pick: pick >= draw, picks))
    winners.append(winner)

persons = []
for winner in winners:
    persons.append(df.Members[picks.index(winner)])

print(persons)
