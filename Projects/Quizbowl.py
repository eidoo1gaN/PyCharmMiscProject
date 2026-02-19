import random
import numpy as np
from sentence_transformers import CrossEncoder

#have json/py-dict of quizbowl questions
#get question and answer, then run the answer for the question as a query through the model, and the input of the user as the passage.
#Check if it is correct via model prediction
#IF INCORRECT, SAVE FOR 20 QUESTIONS LATER AND PICK A RANDOM OTHER QUIZBOWL QUESTION

model = CrossEncoder("cross-encoder/ms-marco-MiniLM-L6-v2")

query = "How many people live in Berlin?"
passages = "3,520,031"
    #"Berlin has a yearly total of about 135 million day visitors, making it one of the most-visited cities in the European Union.",
    #"In 2013 around 600,000 Berliners were registered in one of the more than 2,300 sport and fitness clubs.",


scores = model.predict((query, passages))
print(scores)