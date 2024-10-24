import cv2

# Load the pre-trained Haar Cascade classifier for tree detection
tree_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_tree.xml')

# Prompt the user to input the path to the image
image_path = input("Enter the path to the image: ")

# Load the image
image = cv2.imread(image_path)

if image is None:
    print("Error: Unable to load the image.")
else:
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect trees in the image
    trees = tree_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5)

    # Draw rectangles around detected trees
    for (x, y, w, h) in trees:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the image with detected trees
    cv2.imshow('Detected Trees', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Count the number of detected trees
    num_trees = len(trees)
    print("Number of trees:", num_trees)
