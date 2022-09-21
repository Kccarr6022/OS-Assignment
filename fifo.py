from queue import Queue

MEMORYSIZE = 200

def load_memory(pagesize):
    """: Loads the total memory in the form of a queue

    Args:
        memorysize (int): Total amount of words main memory can hold
        pagesize (int): Total amount of words a page can hold

    Returns:
        memory: A queue of pages
    """
    memory = Queue()
    for i in range(MEMORYSIZE//pagesize):
        memory.put(i)
    return memory


def fofo_page_process(pagesize, words):
    """: Simulates the FIFO page replacement algorithm

    Args:
        memorysize (int): Total amount of words main memory can hold
        pagesize (int): Total amount of words a page can hold
        words (list): A list of words to be processed
    """
    memory = load_memory(pagesize = pagesize)
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

def partA(words):
    print("PART A Page size: 100\n\n")
    memory = load_memory(pagesize = 100)
    print("Memory: ", memory.queue)
    fofo_page_process(pagesize = 100, words= words)

def partB(words):
    print("\n\nPART B Page size: 20\n\n")
    memory = load_memory(pagesize = 20)
    print("Memory: ", memory.queue)
    fofo_page_process(pagesize = 20, words= words)

def partC(words):
    print("\n\nPART C Page size: 200\n\n")
    memory = load_memory(pagesize = 200)
    print("Memory: ", memory.queue)
    fofo_page_process(pagesize = 200, words= words)

def partD(words):
    print("\n\nPART D Page size: 50, 100, and 200\n\n")
    
    print("Page size: 50")
    memory = load_memory(pagesize = 50)
    print("Memory: ", memory.queue)
    fofo_page_process(pagesize = 50, words= words)
    print("\n\n")

    print("Page size: 100")
    memory = load_memory(pagesize = 100)
    print("Memory: ", memory.queue)
    fofo_page_process(pagesize = 100, words= words)
    print("\n\n")

    print("Page size: 200")
    memory = load_memory(pagesize = 200)
    print("Memory: ", memory.queue)
    fofo_page_process(pagesize = 200, words= words)
    print("\n\n")

    print("Part D conclusion\n")
    print("Doubling the page size or halving the page size",
         "from a default of 100 does not change the success frequency\n\n")

def partE(words):
    pass


def main():
    words = [10, 11, 104, 170, 73, 309, 185, 245, 246, 434, 458]

    print("FIFO page replacement algorithm\n\n")

    partA(words)
    partB(words)
    partC(words)
    partD(words)




if __name__ == '__main__':
    main()