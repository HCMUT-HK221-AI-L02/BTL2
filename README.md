# BTL2
## Hướng dẫn chung
+ Mỗi khi push một nội dung mới lên, thành viên trong nhóm lưu ý log lại trong readme.
+ Lưu ý tách branch để làm, mỗi khi xong nội dung thì mới push lên main.
+ Các hàm cần sử dụng được đặt trong folder app.
+ Các hàm chính được đặt ngoài dir chính.
+ Viết lại tên mình trong phần readme/Nhận viết hàm để mọi người biết mình đang viết hàm nào.
+ Lý thuyết Monte Carlo Search Tree:
https://int8.io/monte-carlo-tree-search-beginners-guide/?fbclid=IwAR0eFegd3TK9chrbnpCoMkrUGwPpXvlJvw17yfv-IemFeXYONBTyC4WYQ_0




## Giải thích một số thuật ngữ:
+ board và prev_board là array 2D, dùng để nhập vào move
+ position, moveTuple: tọa độ và nước đi đều dưới dạng tuple (a, b) với a là chỉ số hàng, b là chỉ số cột.
+ Phân biệt posibleMove và legalMove. legalMove là hằng số cho toàn bộ game, tức chỉ những đường nối giữa 2 ô trên bàn cờ. posibleMove là danh sách legalMove của một ô, trừ đi những ô đã bị quân cờ khác chiếm.
+ boardState là obj có thể coi là một node trong giải thuật. Mỗi boardState có chứa danh sách các piece riêng của mình. Giữa các boardState KHÔNG DÙNG CHUNG PIECE. Khi copy boardState ra phải tạo piece mới.
+ Trong boardState có piecelist là danh sách các piece trong state, còn boardplacement là array 2D mà mỗi ô trong array trỏ đến 1 quân cờ trong piecelist (có ô sẽ rỗng)

## Version/Branch
+ Branch "Nhan" đang chứa phiên bản có trapMove theo phương pháp chọn cả 4 ô kế bên đích đến.
+ Branch "Nhan2" sẽ chứa phiên bản trapMove đang sử dụng trong main, chỉ lấy vị trí trapMove đi đến tọa độ vừa được chừa ra.
