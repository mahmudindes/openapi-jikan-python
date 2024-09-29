# EntryMeta

Entry Meta data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mal_id** | **int** | MyAnimeList ID | [optional] 
**url** | **str** | MyAnimeList URL | [optional] 
**image_url** | **str** | Image URL | [optional] 
**name** | **str** | Entry Name/Title | [optional] 

## Example

```python
from jikan_openapi.models.entry_meta import EntryMeta

# TODO update the JSON string below
json = "{}"
# create an instance of EntryMeta from a JSON string
entry_meta_instance = EntryMeta.from_json(json)
# print the JSON string representation of the object
print(EntryMeta.to_json())

# convert the object into a dict
entry_meta_dict = entry_meta_instance.to_dict()
# create an instance of EntryMeta from a dict
entry_meta_form_dict = entry_meta.from_dict(entry_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


