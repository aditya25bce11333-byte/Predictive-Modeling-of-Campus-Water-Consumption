Campus Water Predictor (ML Project)
This is my 2nd-semester project for the AIML course. It uses Multiple Linear Regression to calculate how much water a university campus might use based on two main factors: the weather and the number of people on site.

Why I built this
A simple straight-line graph usually isn't enough for real-world problems. If it's a hot day but the campus is empty, water usage stays low. If it's a cool day but the campus is packed, usage goes up. I wanted to build a model that looks at Temperature and Student Count at the same time to get a more accurate prediction.

What you need to run it
You will need Python installed on your system. Before running the script, you need to install these specific libraries:

Bash
pip install numpy scikit-learn plotly
NumPy: Handles the data arrays and coordinate grids.

Scikit-Learn: This is the main machine learning tool used to build and train the regression model.

Plotly: Used for the 3D graphics because it is interactive and allows the user to rotate the view.

How to use it
Run the script: Open your terminal and run python "Water usage.py".

Input Phase: The terminal will ask for two things:

Current Temperature (in Celsius)

Number of Students currently on campus

The Result: The program will instantly print the predicted Liters in the terminal window.

The 3D Graph: A browser tab will open showing a 3D map.

The Dots represent historical data points.

The Colorful Surface is the Prediction Plane created by the model.

The Red Diamond shows exactly where your specific input sits on that map relative to the past trends.

How the math works
Instead of just a 2D line, this model creates a 3D plane. It calculates a weight for the temperature and a weight for the student count.

When you enter your data, the model places a point on that 3D surface to give you the most logical answer based on the patterns it learned from the training data.

Final thoughts
This project taught me that data visualization is just as important as the code itself. Seeing the Prediction Plane in 3D makes it much easier to explain the results to someone else. In the future, I would like to add variables like Humidity or Day of the Week to see if the predictions can be refined even further
