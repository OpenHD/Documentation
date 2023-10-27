import os
import requests
from bs4 import BeautifulSoup
from markdown2pdf import convert
from urllib.parse import urlparse, urljoin

# GitHub repository URL and branch
github_repo_url = "https://github.com/OpenHD/Documentation"
branch = "evo"

# Function to download a file
def download_file(url, local_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(local_path, 'wb') as f:
            f.write(response.content)

# Function to process links in a markdown file
def process_markdown_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    soup = BeautifulSoup(content, 'html.parser')
    for link in soup.find_all('a'):
        href = link.get('href')
        if href:
            parsed_url = urlparse(href)
            if not parsed_url.netloc:
                link_url = urljoin(github_repo_url, f'{branch}/{href}')
                download_file(link_url, os.path.join(download_dir, href))
                link['href'] = href

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(str(soup))

# Directory to store downloaded files
download_dir = "downloaded_files"
os.makedirs(download_dir, exist_ok=True)

# Download and process SUMMARY.md
summary_md_url = f"{github_repo_url}/blob/{branch}/SUMMARY.md"
download_file(summary_md_url, os.path.join(download_dir, 'SUMMARY.md'))
process_markdown_file(os.path.join(download_dir, 'SUMMARY.md'))

# Recursively process linked markdown files
with open(os.path.join(download_dir, 'SUMMARY.md'), 'r', encoding='utf-8') as f:
    summary_content = f.read()
    for line in summary_content.splitlines():
        if line.startswith('- ['):
            file_name = line.split('](', 1)[1].split(')', 1)[0]
            file_url = urljoin(github_repo_url, f'{branch}/{file_name}')
            download_file(file_url, os.path.join(download_dir, file_name))
            process_markdown_file(os.path.join(download_dir, file_name))

# Convert the modified SUMMARY.md to PDF
convert(os.path.join(download_dir, 'SUMMARY.md'), os.path.join(download_dir, 'summary.pdf'))
