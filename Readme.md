To crawl throgh a link and save the data in a json file

```
scrapy crawl course -o course.json
```

To run scrapy shell

```
scrapy shell <Url to scrape>
```

This opens a prompt where you can run commands like

```
response.css('h3 a').get()
```

While inside the shell to fetch response from a url,

```
fetch(url)
```
