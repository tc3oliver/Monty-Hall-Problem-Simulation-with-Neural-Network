import random
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

def open_door(player_choice, car_location):
    # The host opens a door with a goat
    # The host cannot open the door chosen by the player or the door with the car
    if player_choice == car_location:
        # If the player's initial choice is the door with the car, randomly open one of the other two doors
        opened_door = random.choice([door for door in range(1, 4) if door != player_choice])
    else:
        # If the player's initial choice is a door with a goat, the host opens the remaining door with a goat
        opened_door = [door for door in range(1, 4) if door != player_choice and door != car_location][0]
    return opened_door

def simulate_three_door_problem(switch_door): 
    # Simulate the three-door problem, switch_door indicates whether to switch doors
    # Randomly choose a door as the player's initial choice
    player_choice = random.randint(1, 3)  

    # The location of the car is also random
    car_location = random.randint(1, 3)  

    # Open a door with a goat
    opened_door = open_door(player_choice, car_location)

    # Make the final choice based on whether to switch doors
    if switch_door: 
        player_choice = [door for door in range(1, 4) if door != player_choice and door != opened_door][0]

    # Check if the final choice wins (i.e., choosing the door with the car)
    win = (player_choice == car_location)

    # Output the result
    if win:
        return 1
    else:
        return 0

# Collect training data
data = []
for i in range(100000):
    player_choice = np.random.randint(1, 3)
    car_location = np.random.randint(1, 3)
    switch_door = np.random.choice([0, 1])
    if switch_door:
        player_choice = [c for c in range(1, 4) if c != player_choice][0]
    result = simulate_three_door_problem(switch_door)
    data.append([player_choice, car_location, switch_door, result])

# Build and train the network
model = Sequential()
model.add(Dense(10, input_dim=3, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])
model.fit(np.array(data)[:,:3], np.array(data)[:,-1], epochs=10)

# Predict new input data with switching doors
test_data_switch_door = [1, 3, 1]
pred = model.predict(np.array([test_data_switch_door]))
print(f"Winning probability with switching doors: {pred[0][0]:.5f}")

# Predict new input data without switching doors
test_data_no_switch_door = [1, 3, 0]
pred = model.predict(np.array([test_data_no_switch_door]))
print(f"Winning probability without switching doors: {pred[0][0]:.5f}")