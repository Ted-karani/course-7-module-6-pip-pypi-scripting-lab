import requests
from datetime import datetime


def fetch_data():
    """
    Fetch a sample post from JSONPlaceholder API.
    
    Returns:
        dict: The JSON response data, or empty dict on failure.
    """
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    if response.status_code == 200:
        return response.json()
    return {}


def generate_log(data):
    """
    Generate a log file from a list of entries.
    
    Args:
        data (list): A list of strings to write as log entries.
    
    Returns:
        str: The filename of the generated log file.
    """
    if not isinstance(data, list):
        raise ValueError("Input must be a list")

    today = datetime.now().strftime("%Y%m%d")
    filename = f"log_{today}.txt"

    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")

    print(f"Log written to {filename}")
    return filename


if __name__ == "__main__":
    # Fetch data from API
    post = fetch_data()
    title = post.get("title", "No title found")
    body = post.get("body", "No body found")

    # Create log entries
    log_data = [
        f"API Fetch: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"Title: {title}",
        f"Body: {body}"
    ]

    # Write to log file
    generate_log(log_data)