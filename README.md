# The Monty Hall Problem Simulation with Neural Network

This project aims to simulate and solve the Monty Hall Problem using a neural network approach. The Monty Hall Problem, also known as the Three-Door Problem, is a famous probability puzzle that demonstrates a counterintuitive result.

## Problem Description

The Monty Hall Problem scenario involves the following steps:

1. There are three doors, behind one of which is a valuable prize (e.g., a car), while the other two doors hide less desirable prizes (e.g., goats).
2. The player chooses one door as their initial choice.
3. The host, who knows what is behind each door, opens one of the remaining two doors to reveal a goat.
4. At this point, the player has the option to stick with their initial choice or switch to the other unopened door.
5. Finally, the player's selected door is opened, and they receive the prize behind it.

The paradox arises from the fact that, counterintuitively, switching doors after the host reveals a goat significantly increases the player's chances of winning the car. This project aims to explore and demonstrate this phenomenon using a neural network.

## Project Overview

The project involves the following components:

1. **Simulation**: The `simulate_three_door_problem` function simulates the Monty Hall Problem by randomly generating the initial door choice, the car's location, and the decision to switch or stick with the initial choice. The function returns a binary value (1 for a win, 0 for a loss).

2. **Data Collection**: The simulation function is used to collect training data for the neural network. The data includes the player's initial choice, the car's location, the decision to switch, and the corresponding win/loss outcome.

3. **Neural Network Model**: The project utilizes a multilayer perceptron (MLP) neural network model implemented using TensorFlow and Keras. The model consists of two dense layers with ReLU activation in the first layer and sigmoid activation in the output layer. The model is trained using the collected data to predict the winning probabilities.

4. **Training and Evaluation**: The collected data is split into training and testing sets. The model is trained on the training set and evaluated on the testing set to measure its performance. The accuracy metric is used to evaluate the model's ability to predict the winning probabilities accurately.

5. **Prediction**: The trained model can be used to predict the winning probabilities for new input data. The probabilities are calculated for both switching and not switching doors, providing insights into the optimal strategy.

## Results

After training the neural network model on a large dataset of simulated Monty Hall Problem scenarios, the model is capable of predicting the winning probabilities for different strategies.

The results obtained from the trained model show that:

- When the player chooses to switch doors, the predicted winning probability is approximately 0.65724.

- When the player chooses not to switch doors, the predicted winning probability is approximately 0.34175.

These probabilities align with the counterintuitive solution of the Monty Hall Problem, highlighting the advantage of switching doors.

## Usage

To run the project, follow these steps:

1. Install the necessary dependencies, including TensorFlow and NumPy.
2. Run the code to collect the training data, build the neural network model, and train it on the collected data.
3. Use the trained model to predict the winning probabilities for different scenarios by providing the input data, including the initial door choice, the car's location, and the decision to switch or stick with the initial choice.

Feel free to modify the parameters, such as the number of training instances or the neural network architecture, to further explore and experiment with the Monty Hall Problem.

## Conclusion

The Monty Hall Problem is a fascinating probability puzzle that challenges our intuitions. This project demonstrates the effectiveness of neural networks in simulating and solving the problem. The trained model accurately predicts the winning probabilities for different strategies, showcasing the advantage of switching doors. By exploring and experimenting with this project, users can gain a deeper understanding of conditional probabilities and the counterintuitive nature of the Monty Hall Problem.