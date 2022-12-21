# Import thư viện và định nghĩa hằng số
from app.state import State
from math import log, sqrt
from random import choice
UCT_CONST = 0.5


# Định nghĩa class node
class Node:
    # Biến static cho toàn cây nhằm xác định cây đang muốn tính điểm cho ai thắng
    player = 0
    # Hàm khởi tạo một node
    def __init__(self, state, turnOf, parent, fromMove):
        self.Q = 0
        self.N = 0
        self.state = state
        self.turnOf = turnOf
        self.parent = parent
        self.next = []
        self.fromMove = fromMove


# Viết các hàm của thuật toán MCST
def resources_left(remain_time_x, remain_time_o):
    return True


def transverse(root: Node):
    # Rút thông tin từ root
    rootState: State = root.state
    # Nếu chưa có lá thì tạo lá
    if len(root.next) == 0:
        posibleMoveList = rootState.posibleMoveListTeam(root.turnOf)
        for move in posibleMoveList:
            leafState = State(rootState.prev_board, rootState.board)
            leafState.boardMove(move)
            leaf = Node(leafState, root.turnOf * (-1), root, move)
            root.next.append(leaf)
    # Nếu có lá thì lấy lá chưa được duyệt
    child: Node
    for child in root.next:
        if child.N == 0: return child
    # Nếu mọi lá đều đã duyệt thì transverse tiếp theo luật UCT
    uctList = []
    for child in root.next:
        uct = child.Q / child.N + UCT_CONST*sqrt(log(root.N) / child.N)
        uctList.append(uct)
    idxNext = uctList.index(max(uctList))
    nodeNext = root.next[idxNext]
    return transverse(nodeNext)


def backpropagate(node: Node, simulation_result):
    if node.parent == None: return 
    node.Q += simulation_result[0]
    node.N += simulation_result[1]
    backpropagate(node.parent)


def best_child(root: Node):
    # Chọn child có số lần được chọn nhiều nhất
    child: Node
    NList = []
    for child in root.next: NList.append(child.N)
    idxBest = NList.index(max(NList))
    return root.next[idxBest]


def non_terminal(state: State):
    if state.victor == 0: return True
    else: return False


# Hàm chọn một posible move
def rollout_policy(state: State, turnOf):
    posibleMoveList = state.posibleMoveListTeam(turnOf)
    return choice(posibleMoveList)


# Hàm trả ra kết quả rollout
def result(state: State):
    if state.victor == Node.player: return (1, 1)
    elif state.victor == 0: return (0,1)
    elif state.victor == Node.player * (-1): return (-1, 1)


def rollout(node: Node):
    # Tạo một state đệm để mô phỏng
    nodeState: State = node.state
    tState = State(nodeState.prev_board, nodeState.board)
    turnOf = node.turnOf
    # Khi còn trong điều kiện giá lập thì cho tState thực hiện bước đi
    while non_terminal(tState):
        moveTupple = rollout_policy(tState, turnOf)
        tState.boardMove(moveTupple)
        turnOf *= (-1)
    # Trả ra kết quả
    return result(tState)


def monte_carlo_tree_search(root, remain_time_x, remain_time_o):
    while resources_left(remain_time_x, remain_time_o):
        leaf = transverse(root)
        # Mô phỏng kết leaf, kết quả là Tuple (Q, N)
        simulation_result = rollout(leaf)
        backpropagate(leaf, simulation_result)
    return best_child(root)