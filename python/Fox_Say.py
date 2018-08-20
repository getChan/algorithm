from sys import stdin
read = stdin.readline

def animalsay(sound):
    for i in sound:
        yield i.split()[-1]

def foxsay(recorded, sound):
    for i in animalsay(sound):
        recorded = list(filter(lambda x: x!=i, recorded))
    for i in recorded:
        print(i, end=' ')

if __name__ == '__main__':
    for _ in range(int(read().rstrip())):
        recorded = list(read().split())
        sound = list()
        sound.append(read().rstrip())
        
        while sound[-1] != 'what does the fox say?':
            sound.append(read().rstrip())
        foxsay(recorded, sound[:-1])
        