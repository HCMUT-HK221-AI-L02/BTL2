# import thư viện
from app.mcst import *

# Định nghĩa giải thuật đưa ra move dựa trên Monte Carlo
def move(prev_board, board, player, remain_time_x, remain_time_o):
    # Tạo root cho cây
    Node.player = player
    rootState = State(prev_board, board)
    root = Node(rootState, player, None, None)
    # Xác định người chơi đang xét sử dụng thời gian nào
    if player == 1: remain_time = remain_time_o
    else: remain_time = remain_time_x
    # Gọi giải thuật chọn move
    ansLeaf: Node
    ansLeaf = monte_carlo_tree_search(root, remain_time)
    # xuất move được chọn ra
    return ansLeaf.fromMove