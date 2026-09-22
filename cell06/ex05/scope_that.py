def add_one(a) :
    a += 1      # อันนี้ Local ถ้าสั่ง print ใน def จะได้ 43

what = 42       # อันนี้เป็น Global
print(what)
add_one(what)
print(what)