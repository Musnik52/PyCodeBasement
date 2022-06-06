# ייבוא הספריה מוגדר כך
from PIL import Image
# הדבקת תמונות אחת על השניה
# הגדרת 2 תמונות
pic = Image.open('example.jpg')
pic2 = Image.open('example2.jpg')
# הגדרת שקיפות התמונות
pic2.putalpha(200)
pic.putalpha(100)
# הגדרת הדבקה והצגת התמונה החדשה
pic.paste(im=pic2, box=(0,0), mask=pic2)
pic.show()
# שמירת התמונה החדשה שנוצרה
pic.save('new_example.png')
