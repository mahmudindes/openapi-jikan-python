# NewsDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mal_id** | **int** | MyAnimeList ID | [optional] 
**url** | **str** | MyAnimeList URL | [optional] 
**title** | **str** | Title | [optional] 
**var_date** | **str** | Post Date ISO8601 | [optional] 
**author_username** | **str** | Author MyAnimeList Username | [optional] 
**author_url** | **str** | Author Profile URL | [optional] 
**forum_url** | **str** | Forum topic URL | [optional] 
**images** | [**CommonImages**](CommonImages.md) |  | [optional] 
**comments** | **int** | Comment count | [optional] 
**excerpt** | **str** | Excerpt | [optional] 

## Example

```python
from jikan_openapi.models.news_data_inner import NewsDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of NewsDataInner from a JSON string
news_data_inner_instance = NewsDataInner.from_json(json)
# print the JSON string representation of the object
print(NewsDataInner.to_json())

# convert the object into a dict
news_data_inner_dict = news_data_inner_instance.to_dict()
# create an instance of NewsDataInner from a dict
news_data_inner_form_dict = news_data_inner.from_dict(news_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


