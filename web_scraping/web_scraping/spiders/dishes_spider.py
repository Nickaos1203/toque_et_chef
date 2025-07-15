from pathlib import Path

import scrapy
import re

class MarmiteSpider(scrapy.Spider):
    name= "dishes_spider"
    allowed_domains = ["marmiton.org"]
    start_urls = ["https://www.marmiton.org/recettes?type=platprincipal&page=" + str(x) for x in range(1, 10)]


    def parse(self, response):
        recipe_cards = response.css("div.recipe-card")

        for card in recipe_cards:
            link = card.css("a.recipe-card-link::attr(href)").get()
            image_url = card.css("a.recipe-card-link div.recipe-card__picture img::attr(data-src)").get()

            if link:
                yield response.follow(
                    link,
                    callback=self.parse_recipe,
                    cb_kwargs={'image_url': image_url}
                )

    
    def parse_recipe(self, response, image_url):
        title = response.css("div.recipe-header__title div.main-title h1::text").get()

        categories = response.css("div.recipe-header__title div.main-title div.show-more__modal div.modal__tags span.modal__tag *::text").getall()
        season = categories[0]
        category = categories[1]

        pre_tags = response.css("div.recipe-header__title div.main-title div.show-more__modal div.modal__tags a.modal__tag *::text").getall()
        tags = [t.strip() for t in pre_tags]
        tags_clean = ";".join(tags)
    

        duration = response.css("div.recipe-primary div.recipe-primary__item span::text").get()
        level = response.css("div.recipe-primary div.recipe-primary__item span::text")[1].get()
        cost = response.css("div.recipe-primary div.recipe-primary__item span::text")[2].get() 

        number = response.css("div.mrtn-recette_ingredients div.mrtn-recette_ingredients-counter::attr(data-servingsnb)").get()
        unit = response.css("div.mrtn-recette_ingredients div.mrtn-recette_ingredients-counter::attr(data-servingsunit)").get()
        persons_number = number + " " + unit

        ingredients = []
        for ingredient in response.css("div.mrtn-recette_ingredients div.mrtn-recette_ingredients-content div.mrtn-recette_ingredients-items div.card-ingredient div.card-ingredient-content span.card-ingredient-title"):
            texts = ingredient.css("*::text").getall()
            clean_text = ' '.join(t.strip() for t in texts if t.strip())
            ingredients.append(clean_text)

        # conversion en texte avec ";" en séparateur
        ingredients_clean = ";".join(ingredients)

        steps = []
        for step in response.css("div.recipe-preparation div.recipe-step-list div.recipe-step-list__container p"):
            texts = step.css("*::text").getall()
            strip_text = ' '.join(t.strip() for t in texts if t.strip())
            clean_text = re.sub(r'[\n\r]+', '', strip_text)                     # supprimer de tous types d'espaces invisibles

            steps.append(clean_text)

        # conversion en texte avec ";" en séparateur
        steps_clean = ";".join(steps)


        yield {
            'title':title,
            'image_url': image_url,
            'season': season,
            'category': category,
            'tags': tags_clean,
            'duration': duration,
            'level': level,
            'cost': cost,
            'number': number,
            'persons_number': persons_number,
            'ingredients': ingredients_clean,
            'steps': steps_clean,
        }

