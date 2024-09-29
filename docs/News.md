# News


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[NewsDataInner]**](NewsDataInner.md) |  | [optional] 

## Example

```python
from jikan_openapi.models.news import News

# TODO update the JSON string below
json = "{}"
# create an instance of News from a JSON string
news_instance = News.from_json(json)
# print the JSON string representation of the object
print(News.to_json())

# convert the object into a dict
news_dict = news_instance.to_dict()
# create an instance of News from a dict
news_form_dict = news.from_dict(news_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


