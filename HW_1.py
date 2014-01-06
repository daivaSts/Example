# FSM Simulation
edges = {(1, 'a') : 2,
         (2, 'a') : 2,
         (2, '1') : 3,
         (3, '1') : 3}
accepting = [3]
def fsmsim(string, current, edges, accepting):
    if string == "":
        return current in accepting
        
    else:
        letter = string[0]

        if (current, letter) in edges:
            current  = edges[current, letter]
            string = string[1:]
            return fsmsim(string, current, edges, accepting)
            
        else:
            return False


print fsmsim("aaa111",1,edges,accepting)