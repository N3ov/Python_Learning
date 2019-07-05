class Link_list:

    def __init__(self, num=None, next=None):
        self.num = num
        self.next = next
        self.curr = self

    def prase(self):

        while(self.curr != None):

            print(self.curr.num)
            self.curr = self.curr.next



C = Link_list({"AAA": 80 }, None)

B = Link_list({"BBB": 50}, C)

A = Link_list({"CCC": 55}, B)

A.prase()
