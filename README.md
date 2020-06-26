# Personal Site

My personal site built with [Pelican](http://getpelican.com) and [GitHub Pages](https://pages.github.com).

## Development
To preview the site during development run the following commands
```shell
pelican /path/to/your/content/
cd output
python -m http.server
```
Once the basic server has been started, you can preview the site at http://localhost:8000/

## Deployment
```shell
git clone https://github.com/w-frank/w-frank.github.io.git
cd w-frank.github.io
-- add/update content --
publish.bat "commit message"
```
