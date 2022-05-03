import cv2
import re
import pytesseract

def scan_img(image):
	config = r'--oem 3 --psm 6'
	return pytesseract.image_to_string(img, config=config)

def get_digit(s):
    return re.search(r'\d+',s).group()

def get_sn_carriage(image):
    return get_digit(scan_img(image))

img = cv2.imread('text.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

print(get_sn_carriage(img))




# import cv2
# import pytesseract
# import re

# def parseI(img):
# 	config_img = r'--oem 3 --psm 6'
# 	s = pytesseract.image_to_string(img, config=config_img)
# 	sf = re.search(r'\d+',s).group()
# 	print(sf)
# 	data = pytesseract.image_to_data(img, config=config_img)

# def getI(img):
# 	parseI(img)



# img = cv2.imread('text.png')
# print(type(img))
# # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# # getI(img)
# # # Перебираем данные про текстовые надписи
# # for i, el in enumerate(data.splitlines()):
# # 	if i == 0:
# # 		continue

# 	el = el.split()
# 	try:
# 		# Создаем подписи на картинке
# 		x, y, w, h = int(el[6]), int(el[7]), int(el[8]), int(el[9])
# 		cv2.rectangle(img, (x, y), (w + x, h + y), (0, 0, 255), 1)
# 		cv2.putText(img, el[11], (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1)
# 	except IndexError:
# 		print("Операция была пропущена")

# # Отображаем фото
# cv2.imshow('Result', img)
# cv2.waitKey(0)