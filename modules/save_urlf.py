import os


def save_url(url_id, url):
    path = "urls"
    if not os.path.exists(path):
        os.makedirs(path)

    filename = f"{url_id}.json"

    filepath = os.path.join(path, filename)

    with open(filepath, "w") as f:
        f.write(url)
        print(f"Token {url} saved to file {filename}")
