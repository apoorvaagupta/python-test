from algs4.stdlib.stdrandom import uniform, shuffle
from algs4.stdlib.stdstats import mean, stddev
# from algs4.stdlib.stdio import eprint
import sys, random


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


class RandomQueue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def __len__(self):
        return len(self.items)

    def enqueue(self, item):
        self.items.insert(len(self.items),item)

    def sample(self):
        return self.items[random.randint(0, len(self.items)-1)]

    def dequeue(self):
        return self.items.pop(0)

    def __iter__(self):
        """
        Returns an iterator that iterates over the items in this RandomQueue in random order.
        :returns: an iterator that iterates over the items in this RandomQueue in random order.
        """
        temp = self.items
        mine = []
        while len(temp):
            i = random.randint(0, len(temp) - 1)
            item = temp[i]
            temp[i] = temp[-1]
            temp.pop()
            mine.insert(0,item)
        # create the right mine
        for x in mine:
            yield x


# This  "main method" tests your implementation. Do not change it.
if __name__ == '__main__':
    Q = RandomQueue()
    # build a randomQueue with 1,2,..,6
    for i in range(1, 7):
        Q.enqueue(i)

    # print 30 die rolls
    eprint(' '.join([str(Q.sample()) for i in range(30)]))

    # Let's be more serious: do they really behave like die rolls?
    rolls = [Q.sample() for i in range(1000)]
    eprint("Mean (should be around 3.5): {:5.4f}".format(mean(rolls)))
    eprint("Standard deviation (should be around 1.7): {:5.4f}".format(stddev(rolls)))

    # removing 3 random values
    eprint("Removing {}".format(' '.join([str(Q.dequeue()) for i in range(3)])))

    # Add 7,8,9
    for i in range(7, 10):
        Q.enqueue(i);
        # Empty the queue in random order
    while not Q.isEmpty():
        eprint(Q.dequeue(), end=' ');
    eprint()

    # Let s look at the iterator. First, we make a queue of colours:
    C = RandomQueue()
    C.enqueue("red");
    C.enqueue("blue");
    C.enqueue("green");
    C.enqueue("yellow");

    I = iter(C)
    J = iter(C)

    eprint("Two colours from first shuffle: {} {}".format(next(I), next(I)))

    eprint("Entire second shuffle: {}".format(' '.join([i for i in J])));

    eprint("Remaining two colours from first shuffle: {} {}".format(next(I), next(I)))

    # for i in range(3):
    #     eprint(list( Q))
    # for i in range(6):
    #     eprint(Q.dequeue())
