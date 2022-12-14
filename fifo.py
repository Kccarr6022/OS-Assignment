from queue import Queue

words = [10, 11, 104, 170, 73, 309, 185, 245, 246, 434, 458]

def load_memory(pagesize, memorysize):
    """: Loads the total memory in the form of a queue

    Args:
        memorysize (int): Total amount of words main memory can hold
        pagesize (int): Total amount of words a page can hold

    Returns:
        memory: A queue of pages
    """
    memory = Queue()
    for i in range(memorysize//pagesize):
        memory.put(i)
    return memory


def fofo_page_process(pagesize, memorysize):
    """: Simulates the FIFO page replacement algorithm

    Args:
        memorysize (int): Total amount of words main memory can hold
        pagesize (int): Total amount of words a page can hold
    """
    memory = load_memory(pagesize, memorysize)
    page_faults = 0
    for word in words:
        if word//pagesize in memory.queue:
            print("Word {} is in memory".format(word))
        else:
            print("Word {} is not in memory".format(word))
            page_faults += 1
            memory.get()
            memory.put(word//pagesize)
    print("Page faults: ", page_faults)
    print("Success frequency: ", (len(words)-page_faults)/len(words))

def partA(memorysize):
    print("PART A Page size: 100\n\n")
    fofo_page_process(pagesize = 100, memorysize= memorysize)

def partB(memorysize):
    print("\n\nPART B Page size: 20\n\n")
    fofo_page_process(pagesize = 20, memorysize= memorysize)

def partC(memorysize):
    print("\n\nPART C Page size: 200\n\n")
    fofo_page_process(pagesize = 200, memorysize= memorysize)

def partD(memorysize):
    print("\n\nPART D Page size: 50, 100, and 200\n\n")

    print("Page size: 50")
    fofo_page_process(pagesize = 50, memorysize= memorysize)
    print("\n\n")

    print("Page size: 100")
    fofo_page_process(pagesize = 100, memorysize= memorysize)
    print("\n\n")

    print("Page size: 200")
    fofo_page_process(pagesize = 200, memorysize= memorysize)
    print("\n\n")

    print("Part D conclusion\n")
    print("Doubling the page size or halving the page size",
         "from a default of 100 does not change the success frequency\n\n")

def partE():
    print("\n\nPART E: Advantages of smaller page sizes\n\n")
    text = """The advantage of using smaller pages is that if the range of words\
being called is greater than the maximum memory size then the page size\
can be increased to accomodate the range of words being called. This is not\
possible with larger page sizes because the maximum memory size is fixed.\n\n"""
    print(text)

def partF(memorysize):
    print("\n\nPART F: Memory size of 400 words\n\n")
    partA(memorysize)
    partB(memorysize)
    partC(memorysize)

def partG():
    print("\n\nPART G: Advantages of more memory\n\n")
    text = """The advantages of more memory included less page faults and a higher capability to store\
    more words in memory. This is because the more memory the more pages can be stored in memory."""
    print(text)

def partH():
    print("\n\nPART H: Could this request list happen during the execution of a real program?\n\n")
    text = """Yes, this request list could happen during the execution of a real program. This is because\
the request list simulates an actual program that calls from memory. These processes occur frequently.\
"""
    print(text)

def partI():
    print("\n\nPART I: Would you expect the success rate of an actual program under similar conditions\
to be higher or lower than the one in this problem?\n\n")
    text = """Under similar conditions I expect the success rate to be identical to the ones simulated\
in these algorithms"""
    print(text)



def main():
    print("FIFO page replacement algorithm\n\n")

    partA(memorysize = 200)
    partB(memorysize = 200)
    partC(memorysize = 200)
    partD(memorysize = 200)
    partE()
    partF(memorysize = 400)
    partG()
    partH()
    partI()




if __name__ == '__main__':
    main()