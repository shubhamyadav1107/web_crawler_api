from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

app = Flask(__name__)

@app.route('/crawl', methods=['POST'])
def crawl():
    data = request.get_json()
    root_url = data.get('root_url')
    depth = data.get('depth')

    crawled_links = []
    if root_url:
        try:
            # Function to crawl links recursively
            def crawl_page(url, current_depth):
                if current_depth == 0:
                    return
                
                response = requests.get(url)
                soup = BeautifulSoup(response.text, 'html.parser')
                
                # Find all links on the page
                for link in soup.find_all('a', href=True):
                    full_url = urljoin(url, link['href'])  # Handle relative URLs
                    if full_url not in crawled_links:
                        crawled_links.append(full_url)
                        # Recursively crawl the next depth
                        crawl_page(full_url, current_depth - 1)

            # Start crawling from the root URL
            crawl_page(root_url, depth)

        except Exception as e:
            return jsonify({"error": str(e)}), 500

    return jsonify({
        "root_url": root_url,
        "depth": depth,
        "crawled_links": crawled_links
    })

if __name__ == '__main__':
    app.run(debug=True)
