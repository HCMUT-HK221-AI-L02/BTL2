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
+ Hoàn thành nốt kiến trúc
+ Giải thích các thuật ngữ sử dụng trong code.

## Giải thích một số thuật ngữ:
+ map: array 2D sẽ nhập vào hàm move
+ position, moveTuple: tọa độ và nước đi đều dưới dạng tuple (a, b) với a là chỉ số hàng, b là chỉ số cột.
+ Phân biệt posibleMove và legalMove. legalMove là hằng số cho toàn bộ game, tức chỉ những đường nối giữa 2 ô trên bàn cờ. posibleMove là danh sách legalMove của một ô, trừ đi những ô đã bị quân cờ khác chiếm.
+ board là obj có thể coi là một node trong giải thuật. Mỗi board có chứa danh sách các piece riêng của mình. Giữa các board KHÔNG DÙNG CHUNG PIECE. Khi copy board ra phải tạo piece mới.

## Log
### 221130
+ Khởi tạo Repos, readme.
+ Thiết kế kiến trúc app.