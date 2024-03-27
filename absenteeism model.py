{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "8ac83762-9791-4d75-b7b2-3f8e437c7a22",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Accuracy: 0.625\n",
      "              precision    recall  f1-score   support\n",
      "\n",
      "           0       0.00      0.00      0.00         2\n",
      "           1       0.71      0.83      0.77         6\n",
      "\n",
      "    accuracy                           0.62         8\n",
      "   macro avg       0.36      0.42      0.38         8\n",
      "weighted avg       0.54      0.62      0.58         8\n",
      "\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.linear_model import LogisticRegression\n",
    "from sklearn.metrics import accuracy_score, classification_report\n",
    "\n",
    "# Load your dataset, assuming it's in a CSV file named 'late_data.csv'\n",
    "data = pd.read_csv('C:\\\\Users\\\\DELL\\\\Documents\\\\train.csv')\n",
    "\n",
    "# Assuming 'late' is the target variable you want to predict\n",
    "X = data[['Reason_1', 'Reason_2','Reason_3','Reason_4','Month Value','Day of the Week','Transportation Expense','Distance to Work','Age','Daily Work Load Average','Body Mass Index','Education','Children','Pets']]\n",
    "y = data['absent']\n",
    "\n",
    "# Split the data into training and testing sets\n",
    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)\n",
    "\n",
    "# Initialize and train the logistic regression model\n",
    "model = LogisticRegression(max_iter=100000)\n",
    "model.fit(X_train, y_train)\n",
    "\n",
    "# Make predictions on the test set\n",
    "y_pred = model.predict(X_test)\n",
    "\n",
    "# Evaluate the model\n",
    "accuracy = accuracy_score(y_test, y_pred)\n",
    "print(\"Accuracy:\", accuracy)\n",
    "\n",
    "# You can also print classification report for more detailed evaluation\n",
    "print(classification_report(y_test, y_pred))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "441be110-98dd-431f-8dea-5d324b52a2b0",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "081cceef-c4f6-48e5-8771-9cfe67bd7d5b",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4190e323-42e8-49fa-9463-5b670f5f2cdc",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3937f619-c591-459d-98cb-b3c8ef79284f",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7f89912c-308d-4fa9-bb8c-e3182a2e3198",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1a716e58-46c3-49ce-9a75-1ef9c13a5af5",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e0e0932a-aabf-4168-b28d-70044da1626d",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b135963d-f8a9-4043-85c2-0ec992590fce",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d13285c9",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
