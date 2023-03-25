import cv2
import os
import streamlit as st
import plotly.express as px

# Set the path to the directory containing font images
fonts_path = "font_patch/"

# Initialize an empty dictionary to hold the font images
font_images = {}

# Loop over the list of files in the fonts_path directory
for font in os.listdir(fonts_path):
    font_path = os.path.join(fonts_path, font)
    # Loop over the list of files in the font directory
    for image in os.listdir(font_path):import cv2
import os
import plotly.graph_objects as go

# Set the path to the directory containing font images
fonts_path = "font_patch/"

# Initialize an empty dictionary to hold the font images
font_images = {}

# Loop over the list of files in the fonts_path directory
for font in os.listdir(fonts_path):
    font_path = os.path.join(fonts_path, font)
    # Loop over the list of files in the font directory
    for image in os.listdir(font_path):
        image_path = os.path.join(font_path, image)
        # If the current font is not already a key in the font_images dictionary, then initialize an empty list for that font
        if font not in font_images:
            font_images[font] = []
        # Append the font image to the list for that font in the font_images dictionary
        font_images[font].append(cv2.imread(image_path))

# Read in the sample image using cv2.imread()
sample_path = "sample/smp3.jpg"
sample_image = cv2.imread(sample_path)

# Initialize a variable to hold the best matching font
best_font = None

# Initialize a variable to hold the highest matching score
best_score = 0

# Initialize a dictionary to hold the matching scores for each font
font_scores = {}

# Loop over the font_images dictionary
for font, images in font_images.items():
    # Loop over the list of font images for the current font
    for font_image in images:
        # Compute the matching score between the sample image and the current font image using cv2.matchTemplate() with the cv2.TM_CCOEFF_NORMED method
        score = cv2.matchTemplate(sample_image, font_image, cv2.TM_CCOEFF_NORMED)[0][0]
        # If the current score is higher than the previous best score, then update the best_font and best_score variables
        if score > best_score:
            best_font = font
            best_score = score
        # Add the matching score to the font_scores dictionary
        if font not in font_scores:
            font_scores[font] = []
        font_scores[font].append(score)

# Print the best matching font name
print("The font in the sample image is: " + best_font)

# Create a Plotly bar chart showing the matching scores for each font
fig = go.Figure([go.Bar(x=list(font_scores.keys()), y=[max(scores) for scores in font_scores.values()])])
fig.update_layout(title="Matching Scores for Fonts")
fig.update_xaxes(title="Fonts")
fig.update_yaxes(title="Matching Score")
fig.show()
