# AnimeNews

Anime News Resource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationPagination**](PaginationPagination.md) |  | [optional] 
**data** | [**List[NewsDataInner]**](NewsDataInner.md) |  | [optional] 

## Example

```python
from jikan_openapi.models.anime_news import AnimeNews

# TODO update the JSON string below
json = "{}"
# create an instance of AnimeNews from a JSON string
anime_news_instance = AnimeNews.from_json(json)
# print the JSON string representation of the object
print(AnimeNews.to_json())

# convert the object into a dict
anime_news_dict = anime_news_instance.to_dict()
# create an instance of AnimeNews from a dict
anime_news_form_dict = anime_news.from_dict(anime_news_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


