straight_directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]    # ทิศการเดิน (row,col) row=1 จะลงข้างล่าง 1 ช่อง
diagonal_directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]  # (row,col) col=1 จะมาขวา 1 ช่อง

def find_first_piece(board_rows, r, c, step_r, step_c): # จุดที่ king อยู่คือ (r,c) ทิศที่จะก้าวคือ (step_r,step_c)
  r, c = r + step_r, c + step_c
  while 0 <= r < len(board_rows) and 0 <= c < len(board_rows):
    if board_rows[r][c] in "PBRQK":  # บนกระดานที่ r,c มีตัวพวกนี้อยู่หรือไม่
      return board_rows[r][c]        # ถ้ามี ให้ return ตัวนั้นออกมา
    r, c = r + step_r, c + step_c
  return None

def checkmate(board):
  board_rows = board.splitlines() # ตัดแบ่งข้อความเป็นแถว ๆ ใน list

  if not board_rows or any(len(row) != len(board_rows) for row in board_rows): # ว่างหรือมีสักแถวไม่เท่าหลัก
    print("Error")                                                         # r=ค่าใน list แต่ละแถว
    return # ออกจากฟังก์ชัน checkmate

  king_count = sum(row.count("K") for row in board_rows) # ตรวจ King
  if king_count != 1:
    print("Error")
    return

  k_row = next(i for i, row in enumerate(board_rows) if "K" in row)  # enumerate แปะเลขแถวไว้กับข้อมูลแถว
  k_col = board_rows[k_row].index("K")                               # i เก็บเลขแถว row เก็บข้อความในแถว
  # index หาตำแหน่ง                                                  # next ดึง i ที่ผ่านเงื่อนไขมา

  pawn_positions = [                # พิกัดของเบี้ยที่สามารถกิน K ได้ ยืนอยู่ล่าง K เท่านั้น
      (k_row + 1, k_col - 1),       # ล่างซ้าย
      (k_row + 1, k_col + 1),       # ล่างขวา
  ]
  is_checked = any(
      0 <= r < len(board_rows)
      and 0 <= c < len(board_rows)
      and board_rows[r][c] == "P"
      for r, c in pawn_positions
  )

  
  for step in straight_directions: # *step คือแกะ step จาก (-1,0) เป็น -1 , 0
    if find_first_piece(board_rows, k_row, k_col, *step) in ("R", "Q"):
      is_checked = True

  
  for step in diagonal_directions:
    if find_first_piece(board_rows, k_row, k_col, *step) in ("B", "Q"):
      is_checked = True

 
  if is_checked:
    print("Success")
  else:
    print("Fail")