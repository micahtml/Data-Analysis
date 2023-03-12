import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Load the dataset
df = pd.read_csv("mood_dataset.csv")

# Preprocess the data
vectorizer = CountVectorizer(stop_words="english")
X = vectorizer.fit_transform(df["text"])
y = df["mood"]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Train a support vector machine (SVM) model on the training data
model = SVC(kernel="linear", C=0.5)
model.fit(X_train, y_train)

# Evaluate the model on the testing data
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Use the model to predict the mood from a new text input
text_input = input("How are you feeling? ")
text_input_vectorized = vectorizer.transform([text_input])
mood_prediction = model.predict(text_input_vectorized)
print("You seem to be feeling", mood_prediction[0])

# Use the predicted mood to provide personalized suggestions
if mood_prediction[0] in mood_behavior_activities:
    suggestions = mood_behavior_activities[mood_prediction[0]]
    suggestion = random.choice(list(suggestions))
    print("If you're feeling", mood_prediction[0], "try", suggestion + "!")
else:
    print("Take a break and do something that makes you happy!")
