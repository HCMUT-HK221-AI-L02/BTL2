# BTL2
## Hướng dẫn chung
+ Mỗi khi push một nội dung mới lên, thành viên trong nhóm lưu ý log lại trong readme.
+ Lưu ý tách branch để làm, mỗi khi xong nội dung thì mới push lên main.
+ Các hàm cần sử dụng được đặt trong folder app.
+ Các hàm chính được đặt ngoài dir chính.
+ Note của mỗi người (nếu muốn viết) đặt chung trong folder note.
+ Viết lại tên mình trong phần readme/Nhận viết hàm để mọi người biết mình đang viết hàm nào.

## Nhận viết hàm
+ Làm kiến trúc, init git: Nhân
+ Chuẩn bị việc build file cuối cùng để nộp:

## TODO
+ Hoàn thành nốt kiến trúc (done)
+ Giải thích các thuật ngữ sử dụng trong code (process)
+ Hoàn thanh pvp (process)
+ Cập nhật updatePosibleMove có thế cờ mở

## Giải thích một số thuật ngữ:
+ board và prev_board là array 2D, dùng để nhập vào move
+ position, moveTuple: tọa độ và nước đi đều dưới dạng tuple (a, b) với a là chỉ số hàng, b là chỉ số cột.
+ Phân biệt posibleMove và legalMove. legalMove là hằng số cho toàn bộ game, tức chỉ những đường nối giữa 2 ô trên bàn cờ. posibleMove là danh sách legalMove của một ô, trừ đi những ô đã bị quân cờ khác chiếm.
+ boardState là obj có thể coi là một node trong giải thuật. Mỗi boardState có chứa danh sách các piece riêng của mình. Giữa các boardState KHÔNG DÙNG CHUNG PIECE. Khi copy boardState ra phải tạo piece mới.
+ Trong boardState có piecelist là danh sách các piece trong state, còn boardplacement là array 2D mà mỗi ô trong array trỏ đến 1 quân cờ trong piecelist (có ô sẽ rỗng)

## Log
### 221130
+ Khởi tạo Repos, readme.
+ Thiết kế kiến trúc app.
### 221206
+ Hoàn thành thiết kế kiến trúc
+ Nhân viết các file liên quan pvp