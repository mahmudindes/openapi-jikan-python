# MangaNews

Manga News Resource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationPagination**](PaginationPagination.md) |  | [optional] 
**data** | [**List[NewsDataInner]**](NewsDataInner.md) |  | [optional] 

## Example

```python
from jikan_openapi.models.manga_news import MangaNews

# TODO update the JSON string below
json = "{}"
# create an instance of MangaNews from a JSON string
manga_news_instance = MangaNews.from_json(json)
# print the JSON string representation of the object
print(MangaNews.to_json())

# convert the object into a dict
manga_news_dict = manga_news_instance.to_dict()
# create an instance of MangaNews from a dict
manga_news_form_dict = manga_news.from_dict(manga_news_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


