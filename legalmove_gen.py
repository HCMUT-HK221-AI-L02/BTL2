# Code tạo ra list legal move từ một ô bắt đầu và danh sách các ô cho phép
# import string

# Nhập vào tọa độ ban đầu
start_str = input("Input start position (0,0): ")
start = eval(start_str)
print("Start position: ", start)

# Nhập vào string các ô cho phép
legal_str = input("Input list of legal position (LU,U,RU,L,R,LD,D,RD): ")
legal = list(legal_str.split(","))
print("Legal position: ", legal)

# Tạo list các moveTuple
ans = list()
for m in legal:
    # Tính tuple đích đến
    if m == 'LU': des = (start[0] - 1, start[1] - 1)
    elif m == 'U': des = (start[0] - 1, start[1])
    elif m == 'RU': des = (start[0] - 1, start[1] + 1)
    elif m == 'L': des = (start[0], start[1] - 1)
    elif m == 'R': des = (start[0], start[1] + 1)
    elif m == 'LD': des = (start[0] + 1, start[1] - 1)
    elif m == 'D': des = (start[0] + 1, start[1])
    elif m == 'RD': des = (start[0] + 1, start[1] + 1)
    # Tạo tuple move
    moveTuple = (start, des)
    # Add vào list
    ans.append(moveTuple)

# In kết quả
print("List of legal move: ", ans)