import pprint
sample="""
7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
 """

def parse(text):
    lines = text.split('\n')
    while lines[0].split() == []:
        del lines[0]
    numbers = [int(x) for x in lines[0].split(',')]
    i = 1
    boards = []
    while i < len(lines):
        assert lines[i] == ''
        j = 0
        boards.append([])
        while i+j+1 < len(lines) and lines[i+j+1] != '':
            line = lines[i+j+1].split()
            if line:
                boards[-1].append([int(x) for x  in line])
            j += 1
        i += j+1
    return numbers, boards

def play(config, stop=True):
    numbers, boards = config
    already_won = set()
    for round in range(1, len(numbers)):
        for board_num, board in enumerate(boards):
            if board_num in already_won:
                continue
            for rightwards in [True, False]:
                width = len(board[0])
                height = len(board)
                along, across = (width, height) if rightwards else (height, width)
                for i in range(along):
                    allcalled = True
                    for j in range(across):
                        cell = board[j][i] if rightwards else board[i][j]
                        called = cell in numbers[:round]
                        if not called:
                            allcalled = False
                            break
                    if allcalled:
                        remainder = []
                        for line in board:
                            for x in line:
                                if x not in numbers[:round]:
                                    remainder.append(x)
                        score = sum(remainder) * numbers[round-1]
                        print('board', board_num, 'wins on round', round, 'with remainder', remainder, 'score', score)  
                        already_won.add(board_num)
                        if stop or len(already_won) == len(boards):
                            return score                      
    print(numbers)

config = parse(sample)
score = play(config)
assert score == 4512

config2 = parse(open('4/data.txt', 'r').read())
assert play(config2) == 12796
assert play(config2, False) == 18063
