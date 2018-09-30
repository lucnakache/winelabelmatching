import numpy as np
import cv2

def detect_and_draw_sift_features(imagepath):

	# Import image and preprocessing
	image = cv2.imread(imagepath)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	#Create SIFT Feature Detector object
	sift = cv2.SIFT()

	#Detect key points
	keypoints = sift.detect(gray, None)

	# Draw rich key points on input image
	image = cv2.drawKeypoints(image, keypoints, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

	return keypoints,image






def compute_keypoints_matching(new_image_path, image_template_path):
    # Function that compares input image to template
    # It then returns the number of SIFT matches between them
    
    image2 = cv2.imread(image_template_path, 0)
    image1 = cv2.imread(new_image_path, 0)
    
    # Create SIFT detector object
    sift = cv2.SIFT()

    # Obtain the keypoints and descriptors using SIFT
    keypoints_1, descriptors_1 = sift.detectAndCompute(image1, None)
    keypoints_2, descriptors_2 = sift.detectAndCompute(image2, None)

    # Define parameters for our Flann Matcher
    FLANN_INDEX_KDTREE = 0
    index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 3)
    search_params = dict(checks = 100)

    # Create the Flann Matcher object
    flann = cv2.FlannBasedMatcher(index_params, search_params)

    # Obtain matches using K-Nearest Neighbor Method
    # the result 'matchs' is the number of similar matches found in both images
    matches = flann.knnMatch(descriptors_1, descriptors_2, k=2)

    # Store good matches using Lowe's ratio test
    good_matches = []
    for m,n in matches:
        if m.distance < 0.7 * n.distance:
            good_matches.append(m) 

    return len(good_matches)