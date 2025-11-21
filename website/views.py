from flask import Blueprint, render_template
from flask_login import login_required, current_user
import pandas as pd

# importing dataset for housing prices
def load_data():
    path_to_file = "/Users/yashmac/Documents/WebApp (Python)/website/data/housing_dataset.csv"
    housing = pd.read_csv(path_to_file)

    return housing.to_dict(orient='records')
views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    data = load_data()
    return render_template("home.html", user=current_user, data=data)
