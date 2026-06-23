H_Cm="175"
W_Kg="68.5"

H_Cm=int(H_Cm)
W_Kg=float(W_Kg)

H_M=H_Cm/100
BMI=W_Kg/(H_M*H_M)
print("BMI:",round(BMI,2))
