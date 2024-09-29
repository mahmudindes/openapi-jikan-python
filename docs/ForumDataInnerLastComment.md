# ForumDataInnerLastComment

Last comment details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | Last comment URL | [optional] 
**author_username** | **str** | Author MyAnimeList Username | [optional] 
**author_url** | **str** | Author Profile URL | [optional] 
**var_date** | **str** | Last comment date posted ISO8601 | [optional] 

## Example

```python
from jikan_openapi.models.forum_data_inner_last_comment import ForumDataInnerLastComment

# TODO update the JSON string below
json = "{}"
# create an instance of ForumDataInnerLastComment from a JSON string
forum_data_inner_last_comment_instance = ForumDataInnerLastComment.from_json(json)
# print the JSON string representation of the object
print(ForumDataInnerLastComment.to_json())

# convert the object into a dict
forum_data_inner_last_comment_dict = forum_data_inner_last_comment_instance.to_dict()
# create an instance of ForumDataInnerLastComment from a dict
forum_data_inner_last_comment_form_dict = forum_data_inner_last_comment.from_dict(forum_data_inner_last_comment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


