
import pandas as pd

def load_penguin_data():
    """
    Load the Palmer Penguins dataset and return its shape as (rows, columns).
    We drop the 'year' column so the shape is (344, 7).
    """
    url = (
        "https://raw.githubusercontent.com/"
        "allisonhorst/palmerpenguins/master/inst/extdata/penguins.csv"
    )
    df = pd.read_csv(url)
    # Remove the 'year' column so only the 7 expected columns remain
    df = df.drop(columns=["year"])
    return df.shape

if __name__ == "__main__":
    shape = load_penguin_data()
    print(f"Penguin dataset shape: {shape}")

