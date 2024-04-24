class SLL_Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        if self.next == None:
            return str(self.data)
        return str(self.data) + " " + str(self.next)

def size(head):
    if head == None:
        return 0
    return size(head.next) + 1

def nth_from_end(head, n):
    s = size(head)
    if s-1 == n:
        return head.data
    return nth_from_end(head.next, n)

class SentenceTreeNode:
    def __init__(self, word):
        self.word = word
        self.children = []

class SentenceTree:
    def __init__(self):
        self.root = SentenceTreeNode("")

    def ss_recur(self, sentence_list, node):
        if sentence_list == []:
            return
        for n in node.children:
            if node.word == sentence_list[0]:
                self.ss_recur(sentence_list[1:], n)
                return
        new_node = SentenceTreeNode(sentence_list[0])
        node.children.append(new_node)
        self.ss_recur(sentence_list[1:], new_node)
    
    def store_sentence(self, sentence):
        sentence_list = sentence.split()
        self.ss_recur(sentence_list, self.root)

    def contains_recur(self, sentence_list, node):
        if sentence_list == []:
            return True
        if sentence_list[0] != node.word:
            return False
        if len(node.children) == 0 and len(sentence_list) == 1:
            return True
        for n in node.children:
            if self.contains_recur(sentence_list[1:], n) == True:
                return True
        return False


    def contains_sentence(self, sentence):
        sentence_list = sentence.split()
        sentence_list = [""] + sentence_list
        return self.contains_recur(sentence_list, self.root)

if __name__ == "__main__":
    print("testing nth from end")
    sllhead = SLL_Node(6, SLL_Node(1, SLL_Node(5, SLL_Node(4, SLL_Node(9, SLL_Node(8))))))
    print(nth_from_end(sllhead, 0))
    sllhead = SLL_Node(6, SLL_Node(1, SLL_Node(5, SLL_Node(4, SLL_Node(9, SLL_Node(8))))))
    print(nth_from_end(sllhead, 1))
    sllhead = SLL_Node(6, SLL_Node(1, SLL_Node(5, SLL_Node(4, SLL_Node(9, SLL_Node(8))))))
    print(nth_from_end(sllhead, 2))
    sllhead = SLL_Node(6, SLL_Node(1, SLL_Node(5, SLL_Node(4, SLL_Node(9, SLL_Node(8))))))
    print(nth_from_end(sllhead, 3))
    sllhead = SLL_Node(6, SLL_Node(1, SLL_Node(5, SLL_Node(4, SLL_Node(9, SLL_Node(8))))))
    print(nth_from_end(sllhead, 4))
    print("testing sentence tree")
    sentences = SentenceTree()
    #you might want to comment out some of these temporarily when testing
    sentences.store_sentence("my name is jeff")
    print("1", sentences.contains_sentence("my name"))
    print("2", sentences.contains_sentence("my dog"))
    sentences.store_sentence("my dog is happy")
    print("3", sentences.contains_sentence("my dog"))
    print("4", sentences.contains_sentence("my jeff"))
    sentences.store_sentence("my name doesn't concern you")
    sentences.store_sentence("my name is jeff also")
    print("5", sentences.contains_sentence("concern you"))
    print("6", sentences.contains_sentence("my name is"))
    print("7", sentences.contains_sentence("my name is jeff also"))
    print("8", sentences.contains_sentence("jeff"))
    sentences.store_sentence("jeff is happy")
    sentences.store_sentence("jeff is a dog")
    print("9", sentences.contains_sentence("jeff"))
    print("10", sentences.contains_sentence("jeff is dog"))
    print("11", sentences.contains_sentence("jeff is a dog"))
    print("12", sentences.contains_sentence("jeff is a happy dog"))
    print("13", sentences.contains_sentence("jeff is happy"))
    print("14", sentences.contains_sentence("jeff is a dog also"))


    sentences.store_sentence("my name is jeff")
    sentences.store_sentence("my dog is happy")
    sentences.store_sentence("my name is jeff also")
    sentences.store_sentence("my name doesn't concern you")