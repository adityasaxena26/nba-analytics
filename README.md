# NBA Analytics


## Authors
- **Nicholas Cantalupa** - [ncantalupa](https://github.com/ncantalupa)
- **Sean Duffy** - [sean-r-duffy](https://github.com/sean-r-duffy)
- **Aditya Saxena** - [1adityasaxena](https://github.com/1adityasaxena)
- **Pazin Taransombat** - [tarasansombat-p](https://github.com/tarasansombat-p)


## Overview
Utilizing NBA and combine data to predict player/team performance and improve drafting


## Features
- Player style analysis
- Predictive modeling for game outcomes


## Table of Contents
- [Project Organization](#project-organization)
- [Installation](#installation)
- [Usage](#usage)
- [Data Sources](#data-sources)
- [License](#license)


## Project Organization

```
├── .streamlit         <- Streamlit config
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   └── processed      <- The final, canonical data sets for modeling.
│
├── docs               <- View docs by opening index.html
│
├── models             <- Trained models
│
├── notebooks          <- Jupyter notebooks
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis 
│   └── figures        <- Generated graphics
│
├── requirements.txt   <- File for reproducing environment with pip
│
├── environment.yml    <- File for reproducing environment with conda
│
├── build.py           <- Run to collect and clean all data (along with college_player_comps.ipynb)
│
├── main.py            <- Run to use application
│
└── nba_analytics                <- Source code for use in this project.
    │
    ├── __init__.py    <- Makes nba_analytics a Python module
    │
    ├── data           <- Scripts to download and clean data
    │   ├── load.py
    │   └── clean.py
    │
    ├── models         <- Scripts to train models and make predictions
    │   ├── nn_search.py
    │   └── win_prediction.py
    │
    └── ui  <- Scripts to run UI applidation
        ├── radar_plots.py
        └── dashboard.py
```


## Installation
Follow these steps to set up the project locally:

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/NBA-Analytics.git
    cd NBA-Analytics
    ```

2. (Optional) Create a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
   or
   ```sh
    conda create --name nba-analytics python=3.8
    conda activate nba-analytics
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```
   or
   ```sh
    conda install --file requirements.txt
    ```

4. Set up any necessary environment variables or configuration files as specified in [Geting Started](./docs/docs/getting-started.md).


## Usage
To use this project, follow these steps:

1. Run the main script:
    ```sh
    python main.py
    ```

2. Access the analysis and visualizations:
    - Open `index.html` in your web browser to view the dashboard.
    - Use the command line interface to run specific analyses.

For detailed usage instructions, please refer to [Geting Started](./docs/docs/getting-started.md).


## Data Sources
- [Stathead Basketball](https://stathead.com/basketball/) - Courtesy of Sports Reference (https://www.sports-reference.com/)
- [NBA Data API](https://github.com/swar/nba_api)

## License
This project is licensed under the terms of the [MIT License](./LICENSE).

--------
