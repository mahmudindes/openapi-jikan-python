# ForumDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mal_id** | **int** | MyAnimeList ID | [optional] 
**url** | **str** | MyAnimeList URL | [optional] 
**title** | **str** | Title | [optional] 
**var_date** | **str** | Post Date ISO8601 | [optional] 
**author_username** | **str** | Author MyAnimeList Username | [optional] 
**author_url** | **str** | Author Profile URL | [optional] 
**comments** | **int** | Comment count | [optional] 
**last_comment** | [**ForumDataInnerLastComment**](ForumDataInnerLastComment.md) |  | [optional] 

## Example

```python
from jikan_openapi.models.forum_data_inner import ForumDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of ForumDataInner from a JSON string
forum_data_inner_instance = ForumDataInner.from_json(json)
# print the JSON string representation of the object
print(ForumDataInner.to_json())

# convert the object into a dict
forum_data_inner_dict = forum_data_inner_instance.to_dict()
# create an instance of ForumDataInner from a dict
forum_data_inner_form_dict = forum_data_inner.from_dict(forum_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


