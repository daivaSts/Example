# FSM Simulation
edges = {(1, 'a') : 2,
         (2, 'a') : 2,
         (2, '1') : 3,
         (3, '1') : 3}
accepting = [3]
def fsmsim(string, current, edges, accepting):
    if string == "":
        print "current in accepting"
        return True
    else:
        letter = string[0]
       
    if edges[current, letter] in edges.values():
        current  = edges[current, letter]
        string = string[1:]
        fsmsim(string, current, edges, accepting)
        if edges[current, letter] == accepting:
            print "accepting state"
            return True
    else:
        return False

        # QUIZ: You fill this out!
        # Is there a valid edge? 
        # If so, take it.
        # If not, return False.
        # Hint: recursion.

print fsmsim("aaa111",1,edges,accepting)
# >>> True