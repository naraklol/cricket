print("\n\n*********************************")
print("IPL 2019 FANTASY SCORE CALCULATOR")
print("*********************************\n\n")

score = 0

def batsman():
    print("\n")
    runs = float(raw_input("Enter runs: "))
    sr = float(raw_input("Enter strike rate (min. 10 balls): "))

    score = (float(sr)/float(10)) * float(1.5)
    score += runs

    return score

def bowler():
    print("\n")
    wickets = float(raw_input("Enter wickets taken: "))
    econ = float(raw_input("Enter bowling economy (<=10 only): "))

    score = (float(100)/float(econ)) * float(1.5)
    score += wickets * 20

    return score

def catchesro():
    print("\n")
    catches = float(raw_input("Enter catches taken: "))
    ro = float(raw_input("Enter run outs: "))

    score = catches * 15
    score += ro * 15

    return score

type = int(raw_input("Choose player type\n1. Batsman\n2. Bowler\n3. Both\n\nEnter choice: "))

if type == 1:
    score += batsman()
if type == 2:
    score += bowler()
if type == 3:
    score += batsman()
    score += bowler()

score += catchesro()

print("Player score = " + str(score))
