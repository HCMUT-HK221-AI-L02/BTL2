# Import thư viện và định nghĩa hằng số
from app.state import State
from math import log, sqrt
from random import choice
import time
UCT_CONST = 2
# MCST_SIMU_DEEP = 10                     # Chấm offline
MCST_SIMU_DEEP = 5                      # Chấm eln
# MCST_THINK_TIME_PER_TURN = 1.9          # Chấm offline
MCST_THINK_TIME_PER_TURN = 0.027        # Chấm eln


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
def resources_left(remain_time_byTurn, d_time):
    if remain_time_byTurn > d_time: return True
    else: return False


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
    # Nếu sau khi đã tạo lá mà vẫn không có lá thì trả kết quả là node hiện tại
    if len(root.next) == 0: return root
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
    node.Q += simulation_result[0]
    node.N += simulation_result[1]
    if node.parent == None: return 
    backpropagate(node.parent, simulation_result)


def best_child(root: Node):
    # Nếu root không có child nào thì trả kết quả là None
    if len(root.next) == 0: return None
    # Chọn child có số lần được chọn nhiều nhất
    child: Node
    NList = []
    for child in root.next: NList.append(child.N)
    idxBest = NList.index(max(NList))
    return root.next[idxBest]


def non_terminal(state: State, countRollout):
    if state.victor != 0: return False
    if countRollout < MCST_SIMU_DEEP: return True
    else: return False


# Hàm chọn một posible move
def rollout_policy(state: State, turnOf):
    posibleMoveList = state.posibleMoveListTeam(turnOf)
    return choice(posibleMoveList)


# Hàm trả ra kết quả rollout
def result(state: State):
    # Tìm phe có lợi thế
    winner = state.advantageTeam()
    # Trả kết quả có dạng (Q, N), nếu Node.player thắng thì Q = 1
    if winner == Node.player: return (1,1)
    elif winner == Node.player*(-1): return (-1,1)
    else: return (0,1)


def rollout(node: Node):
    # Tạo một state đệm để mô phỏng
    nodeState: State = node.state
    tState = State(nodeState.prev_board, nodeState.board)
    turnOf = node.turnOf
    countRollout = 0
    # Khi còn trong điều kiện giá lập thì cho tState thực hiện bước đi
    while non_terminal(tState, countRollout):
        moveTupple = rollout_policy(tState, turnOf)
        tState.boardMove(moveTupple)
        turnOf *= (-1)
        countRollout += 1
    # Trả ra kết quả
    return result(tState)


def monte_carlo_tree_search(root: Node, remain_time):
    # Xác định thời gian còn lại
    remain_time_byTurn = min(MCST_THINK_TIME_PER_TURN, remain_time)
    d_time = 0
    while resources_left(remain_time_byTurn, d_time):
        s_time = time.time()
        leaf = transverse(root)
        # Mô phỏng kết leaf, kết quả là Tuple (Q, N)
        simulation_result = rollout(leaf)
        backpropagate(leaf, simulation_result)
        e_time = time.time()
        d_time = e_time - s_time
        remain_time_byTurn -= d_time
    return best_child(root)


# Hàm in kết quả (Q, N) để debug
def printQN(root: Node):
    node: Node
    for node in root.next: print("(Q, N) = (", node.Q, ", ", node.N,")")
