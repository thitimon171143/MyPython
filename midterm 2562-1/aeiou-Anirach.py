count = 0
vowel = 'aeiou'
message = " "
msg = input('Enter your string : ')
for i in msg :
    if not (i in vowel) :
        message = message+" "
    else :
        message = message+i

print(msg) #รับค่า
print(message) #ถ้าไม่ใช่ aeiou จะปริ้นออกมาเป็น space  ,ถ้าเป็น aeiou จะปริ้นออกมาเป็น aeiou
print(message.split()) #แยกคำ แล้วตัด space ทิ้ง
print(len(message.split())) #นับคำใน list ของ message.split()