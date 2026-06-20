import cv2
import pytesseract

image_path = input("Enter image file name: ")

img = cv2.imread(image_path)

if img is None:
    print("Image not found")
else:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    text = pytesseract.image_to_string(gray)

    print("\nDetected Text:")
    print(text)

    cv2.imshow("Input Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()