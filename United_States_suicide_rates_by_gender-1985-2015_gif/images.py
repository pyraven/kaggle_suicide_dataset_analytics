import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from moviepy.editor import *
import os

df = pd.read_csv('master.csv')

us = df[df.country == "United States"]
male = us[us.sex == "male"]
female = us[us.sex == "female"]

age_list = ["5-14 years", "15-24 years", "25-34 years", "35-54 years", "55-74 years", "75+ years"]

for n in range(1985, 2016):
	print(f"Year: {n}")

	# males
	male_list = []
	male_year = male[male.year == n]
	for male_age in age_list:
		male_ages = male_year[male_year.age == male_age]
		count = male_ages['suicides_no'].values[0]
		male_list.append(count)
	male_tuple = tuple(male_list)
	print(f"Males: {male_tuple}")

	# females
	female_list = []
	female_year = female[female.year == n]
	for female_age in age_list:
		female_ages = female_year[female_year.age == female_age]
		count = female_ages['suicides_no'].values[0]
		female_list.append(count)
	female_tuple = tuple(female_list)
	print(f"Females: {female_tuple}")
	
	# create images
	N = 6
	ind = np.arange(N) 
	width = 0.35       
	plt.bar(ind, male_tuple, width, label="Males")
	plt.bar(ind + width, female_tuple, width, label="Females")

	plt.ylabel("Suicide Count")
	plt.title(f"United States Suicide by Age Group and Gender ({n})")
	plt.xlabel("Age Ranges")
	
	plt.xticks(ind + width / 2, ('5-14', '15-24', '25-34', '35-54', '55-74', '75+'))
	plt.legend(loc="best")
	plt.savefig(f"images/{n}.png")
	plt.clf()
	print("Images Created")

# build gif
gif_name = "suicide_no.gif"
image_dir = os.listdir("images")
images = sorted([f"images/{x}" for x in image_dir if x.endswith(".png")])
gif = ImageSequenceClip(images, fps=1)
gif.write_gif(gif_name)
print("Gif Created")