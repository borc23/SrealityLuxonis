# Web Scrape of Sreality.cz

## Task

Use scrapy framework to scrape the first 500 items (title, image url) from sreality.cz (flats, sell) and save it in the Postgresql database. Implement a simple HTTP server in python and show these 500 items on a simple page (title and image) and put everything to single docker-compose command so that I can just run "docker-compose up" in the Github repository and see the scraped ads on http://127.0.0.1:8080 page.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

``` bash
git clone https://github.com/borc23/sreality.git
```

## Usage

Navigate to the root of the directory where you can see "docker-compose.yml"

### Use the following command:
``` bash
docker-compose up
```

## Output

For the output website go to [https://localhost:8080](http://localhost:8080/)

![Website](https://github.com/borc23/SrealityLuxonis/blob/main/image.png?raw=true)
