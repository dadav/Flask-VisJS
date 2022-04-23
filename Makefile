VISJS_VERSION := "4.21.0"
VISJS_CDN := "https://cdnjs.cloudflare.com/ajax/libs/vis/$(VISJS_VERSION)"

.PHONY: all
all: fetch-visjs

.PHONY: fetch-visjs
fetch-visjs:
	wget -O flask_visjs/static/vis.min.js $(VISJS_CDN)/vis.min.js
	wget -O flask_visjs/static/vis.min.css $(VISJS_CDN)/vis.min.css
