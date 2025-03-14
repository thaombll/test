def calculate_ship(A, B):
    if not (0 <= A <= 50) or not (0 <= B <= 40):
        return "không hợp lệ"
    elif 0 <= A <= 10 and 0 <= B < 20:  # CORRECT: 0 <= B <= 20
        return "thấp"
    elif 30 < A <= 50 or 30 <= B <= 40:  # CORRECT: 30 <= A <= 50
        return "cao"
    return "trung bình"

print(calculate_ship(A = 60, B = 21.5 ))
print(calculate_ship(A = 5.35, B = 20))
print(calculate_ship(A = 30, B = 22.76 ))
print(calculate_ship(A = 15, B = 15 ))
