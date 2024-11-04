# Web Crawler API

A simple web crawler API built with Flask that retrieves links from a specified root webpage up to a defined depth. This project is intended to demonstrate basic web crawling capabilities and API design using Python.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Technologies Used](#technologies-used)
- [License](#license)

## Features

- Crawls a specified root URL to retrieve links.
- Configurable crawling depth.
- Returns crawled links in JSON format.
- Built with Flask for easy deployment and interaction.

## Installation

To set up the project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your_username/web_crawler_api.git
   cd web_crawler_api
   ```

2. **Set up a virtual environment**:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   # source venv/bin/activate  # On macOS/Linux
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the API**:
   ```bash
   python app.py
   ```

2. **Access the API**: Open your browser or Postman and navigate to `http://127.0.0.1:5000/crawl` to use the API.

3. **Make a request**: Use the following example in Postman or CURL:
   - **POST** request to `http://127.0.0.1:5000/crawl`
   - **Body** (JSON):
     ```json
     {
       "url": "https://example.com",
       "depth": 2
     }
     ```

## API Endpoints

### `/crawl`
- **Method**: `POST`
- **Request Body**:
  - `url` (string): The root webpage to crawl.
  - `depth` (integer): The depth to which to crawl the webpage.
- **Response**:
  - Returns a JSON object containing:
    - `crawled_links`: List of links found.
    - `depth`: The depth used for crawling.
    - `root_url`: The root URL that was crawled.

## Technologies Used

- **Python 3.x**
- **Flask**: For creating the API.
- **BeautifulSoup**: For parsing HTML and extracting links.
- **Requests**: For making HTTP requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```

### Instructions to Use the README.md

1. **Replace `your_username`** in the clone URL with your actual GitHub username.
2. If you have a license file, ensure the link to the `LICENSE` file is correct. If not, you can remove that section.
3. Feel free to add any additional information or sections relevant to your project.

Once you have your `README.md` ready, you can create or edit the file in your local project directory, add it to Git, commit the changes, and push it to your GitHub repository:

```bash
git add README.md
git commit -m "Add README.md for web crawler API"
git push origin main  # or master, depending on your branch name
```
