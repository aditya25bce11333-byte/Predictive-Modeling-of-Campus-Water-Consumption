import numpy as np
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression

X = np.array([
    [20, 100], [25, 200], [30, 150], [35, 300], [40, 250], [32, 400], [28, 120]
])
y = np.array([150, 250, 280, 450, 480, 520, 210])

model = LinearRegression()
model.fit(X, y)

print("CAMPUS WATER PREDICTOR")
try:
    u_temp = float(input("Enter Current Temperature (Celsius): "))
    u_students = float(input("Enter Number of Students on Campus: "))
    
    user_input = np.array([[u_temp, u_students]])
    predicted_liters = model.predict(user_input)[0]
    
    print(f"\nPREDICTION: At {u_temp} Celsius with {u_students} students,")
    print(f"the predicted water usage is {predicted_liters:.2f} Liters.")

except ValueError:
    print("Error: Input must be a numerical value.")
    exit()

x_range = np.linspace(X[:, 0].min(), X[:, 0].max(), 20)
y_range = np.linspace(X[:, 1].min(), X[:, 1].max(), 20)
xx, yy = np.meshgrid(x_range, y_range)
zz = model.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)

fig = go.Figure()

fig.add_trace(go.Scatter3d(
    x=X[:, 0], y=X[:, 1], z=y,
    mode='markers',
    marker=dict(size=8, color=y, colorscale='Viridis'),
    name='Historical Data'
))

fig.add_trace(go.Scatter3d(
    x=[u_temp], y=[u_students], z=[predicted_liters],
    mode='markers',
    marker=dict(size=12, color='red', symbol='diamond'),
    name='User Prediction'
))

fig.add_trace(go.Surface(
    x=x_range, y=y_range, z=zz,
    colorscale='Cividis', opacity=0.5, name='Prediction Plane'
))

fig.update_layout(
    title=f'Water Usage Analysis: {predicted_liters:.2f} Liters',
    scene=dict(
        xaxis_title='Temperature (Celsius)',
        yaxis_title='Student Count',
        zaxis_title='Water Consumption (L)'
    )
)

fig.show()