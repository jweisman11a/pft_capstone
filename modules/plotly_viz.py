# Load libraries
import pandas as pd
import seaborn as sns

# Import viz
import plotly.graph_objects as go
from plotly.offline import download_plotlyjs, plot, iplot


# Create a dataset for testing
tips = sns.load_dataset('tips')


def plotly_line_plot(data, title, xaxis_label, yaxis_label):
    """Function creates a line plot using plotly

    Notes:
        None

    Args:
        url (str): The URL of the PFT Rumor Mill page to be scraped

    Returns:
        A plotly
    """
