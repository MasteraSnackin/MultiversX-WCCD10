# MultiversX Token Leaderboard

This project generates a leaderboard for the top holders of tokens prefixed with "WINTER-" on the MultiversX blockchain. It leverages the MultiversX REST API to fetch token and account data, processes the data, and outputs the results into a CSV file.

## Project Overview

The script performs the following tasks:
- Connects to the MultiversX REST API to fetch a list of all tokens.
- Filters tokens to include only those with identifiers that start with "WINTER-".
- Retrieves account holders and their balances for each filtered token.
- Ranks the account holders based on their token balances.
- Saves the leaderboard data to a CSV file for easy viewing and analysis.

## Prerequisites

- Python 3.x is required to run this script. You can download it from the [official Python website](https://www.python.org/downloads/).
- The script uses the `requests` library, which can be installed via pip.

## Setup Instructions

1. **Clone the Repository**:
   Clone the project repository to your local machine using the following command:
   ```bash
   git clone https://github.com/yourusername/multiversx-leaderboard.git
   cd multiversx-leaderboard
Create a Virtual Environment: Set up a virtual environment to manage dependencies:

python -m venv env
Activate the Virtual Environment: Activate the environment to use it for the project:

On Windows:
.\env\Scripts\activate
On macOS and Linux:
source env/bin/activate
Install Dependencies: Install the required Python packages using pip:

pip install -r requirements.txt
Usage
To run the script and generate the leaderboard, execute the following command:

bash
Copy
python leaderboard.py
The script will create a directory named output (if it doesn't already exist) and save the leaderboard as leaderboard.csv within this directory.

Output
The CSV file (leaderboard.csv) includes the following columns:

Token: The identifier of the token.
Rank: The rank of the account holder based on their balance.
Address: The blockchain address of the account holder.
Balance: The token balance held by the account.
Notes
Ensure you have a stable internet connection, as the script requires API access to fetch data.
The script assumes that the API will return results within complexity and pagination limits. Consider implementing pagination if dealing with larger datasets.
Modify the script as needed to accommodate additional functionality or to handle specific edge cases.
Contributing
Contributions to this project are welcome. If you have suggestions or improvements, please fork the repository and submit a pull request. For major changes, open an issue first to discuss what you would like to change.

License
This project is licensed under the MIT License. See the LICENSE file for more details.