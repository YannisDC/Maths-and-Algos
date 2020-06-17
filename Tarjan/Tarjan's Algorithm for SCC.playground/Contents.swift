import Foundation

let unvisited = -1
let n = 8 // number of nodes in the graph
var g = [[Int]]()// adjacency list with directed edges
g = [[1],[2],[0],[4,7],[5],[0,6],[0,2,4],[3,5]]

var id = 0 // Used to give each node an id
var sccCount = 0 // Used to count number of SCCs found

// Index i in these arrays represents node i
var ids: [Int] = Array(repeating: 0, count: n) // Length n
var low = Array(repeating: 0, count: n) // Length n
var onStack = Array(repeating: false, count: n) // Length n
var stack = [Int]()

func dfs(at: Int) {
    
    stack.append(at)
    onStack[at] = true
    print("At: \(at)")
    print("Stack: \(stack)")
    print(onStack)
    
    
    ids[at] = id
    low[at] = id
    id += 1
    
    print("Ids: \(ids)")
    print("Low: \(low)")
    
    
    // Visit all neighbours & min low-link on callback
    for to in g[at] {
        if ids[to] == unvisited {
            print("\(at) has a connection to \(to) and \(to) is unvisited")
            print("\n___\n")
            dfs(at: to)
        }
        if onStack[to] {
            print("\(at) has a connection to \(to) and \(to) is on the stack")
            print("\(low[at]) is low at \(at)")
            print("\(low[to]) is low at \(to)")
            low[at] = min(low[at], low[to])
            print("\(low[at]) is the new low at \(at)")
        }
    }
    
    print("Ids[at]: \(ids[at])")
    print("Low[at]: \(low[at])")
    print("\n")
    // After having visited all the neighbours of 'at'
    // if we're at the start of a SCC empty the seen
    // stack until we're back to the start of the SCC.
    if ids[at] == low[at] {
        print("We're at the beginning of the SCC which is \(at)")
        for item in stack {
            print(item)
            if let node = stack.popLast() {
                print("Popped node \(node) which makes the new stack \(stack)")
                onStack[node] = false
                low[node] = ids[at]
                print(onStack)
                print("Low: \(low)")
                if node == at {
                    break
                }
            }
        }
        print("\nSCC Found\n__________________________________________________________________\n")
        sccCount += 1
    }
}

func findSccs() -> [Int] {
    ids = Array(repeating: unvisited, count: n)
    for (index, _) in ids.enumerated() {
        if ids[index] == unvisited {
            print("\n\nNode \(index) is unvisited - start Depth First Search:\n")
            dfs(at: index)
        }
    }
    return low
}

findSccs()
print("We found \(sccCount) Strongly Connected Components")
