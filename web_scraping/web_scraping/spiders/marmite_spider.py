from pathlib import Path

import scrapy
import re

class MarmiteSpider(scrapy.Spider):
    name= "appetizer_spider"
    allowed_domains = ["marmiton.org"]
    start_urls = ["https://www.marmiton.org/recettes?page=" + str(x) for x in range(1, 400)]

    def parse(self, response):
        recipe_links = response.css("div.recipe-card a.recipe-card-link::attr(href)").getall()

        for link in recipe_links:
            yield response.follow(link, callback=self.parse_recipe)

    
    def parse_recipe(self, response):
        title = response.css("div.recipe-header__title div.main-title h1::text").get()
        duration = response.css("div.recipe-primary div.recipe-primary__item span::text").get()
        level = response.css("div.recipe-primary div.recipe-primary__item span::text")[1].get()
        cost = response.css("div.recipe-primary div.recipe-primary__item span::text")[2].get() 

        number = response.css("div.mrtn-recette_ingredients div.mrtn-recette_ingredients-counter::attr(data-servingsnb)").get()
        unit = response.css("div.mrtn-recette_ingredients div.mrtn-recette_ingredients-counter::attr(data-servingsunit)").get()
        persons_number = number + " " + unit

        # ingredients = response.css("div.mrtn-recette_ingredients div.mrtn-recette_ingredients-content div.mrtn-recette_ingredients-items div.card-ingredient div.card-ingredient-content span.card-ingredient-title *::text").getall()
        ingredients = []
        for ingredient in response.css("div.mrtn-recette_ingredients div.mrtn-recette_ingredients-content div.mrtn-recette_ingredients-items div.card-ingredient div.card-ingredient-content span.card-ingredient-title"):
            texts = ingredient.css("*::text").getall()
            clean_text = ' '.join(t.strip() for t in texts if t.strip())
            ingredients.append(clean_text)

        steps = response.css("div.recipe-preparation div.recipe-step-list div.recipe-step-list__container p *::text").getall()
        author = response.css("div.recipe-author-note div.recipe-author-note__head div span.recipe-author-note__author-name::text").get()

