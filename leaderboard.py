import requests  # Import the requests library to make HTTP requests to the API
import csv       # Import the csv library to handle CSV file operations
import os        # Import os for operating system functionalities, like file and directory handling

# Define the base URL for the MultiversX API
BASE_URL = "https://api.multiversx.com"

def get_tokens():
    """
    Fetch all tokens and filter those starting with 'WINTER-'.
    
    Returns:
        A list of token identifiers that start with 'WINTER-'.
    """
    # Make a GET request to the /tokens endpoint of the API
    response = requests.get(f"{BASE_URL}/tokens")
    # Raise an error if the request was unsuccessful
    response.raise_for_status()
    # Parse the JSON response to get the list of tokens
    tokens = response.json()
    # Return a list of token identifiers that start with 'WINTER-'
    return [token['identifier'] for token in tokens if token['identifier'].startswith('WINTER-')]

def get_token_holders(token_identifier):
    """
    Fetch holders for a specific token.
    
    Args:
        token_identifier: The identifier of the token for which to fetch holders.
        
    Returns:
        A list of account holders and their balances for the specified token.
    """
    # Make a GET request to the /tokens/{identifier}/accounts endpoint of the API
    response = requests.get(f"{BASE_URL}/tokens/{token_identifier}/accounts")
    # Raise an error if the request was unsuccessful
    response.raise_for_status()
    # Parse and return the JSON response containing the account holders
    return response.json()

def create_leaderboard():
    """
    Create a leaderboard for token holders, writing the results to a CSV file.
    """
    # Fetch all 'WINTER-' tokens
    tokens = get_tokens()
    
    # Ensure the 'output' directory exists to store the CSV file
    os.makedirs('output', exist_ok=True)
    
    # Open a new CSV file in the 'output' directory for writing
    with open('output/leaderboard.csv', mode='w', newline='') as file:
        # Create a CSV writer object
        writer = csv.writer(file)
        # Write the header row to the CSV file
        writer.writerow(['Token', 'Rank', 'Address', 'Balance'])
        
        # Iterate over each 'WINTER-' token
        for token_identifier in tokens:
            # Fetch the holders for the current token
            holders = get_token_holders(token_identifier)
            
            # Sort the holders by their balance in descending order
            holders_sorted = sorted(holders, key=lambda x: int(x['balance']), reverse=True)
            
            # Write each holder's information to the CSV file
            for rank, holder in enumerate(holders_sorted, start=1):
                writer.writerow([token_identifier, rank, holder['address'], holder['balance']])

# This block ensures that the script executes only if it is run as a standalone program
if __name__ == "__main__":
    # Generate the leaderboard and save it to 'output/leaderboard.csv'
    create_leaderboard()
    # Print a message indicating successful creation of the leaderboard
    print("Leaderboard has been created and saved to 'output/leaderboard.csv'.")