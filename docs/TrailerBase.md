# TrailerBase

Youtube Details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**youtube_id** | **str** | YouTube ID | [optional] 
**url** | **str** | YouTube URL | [optional] 
**embed_url** | **str** | Parsed Embed URL | [optional] 

## Example

```python
from jikan_openapi.models.trailer_base import TrailerBase

# TODO update the JSON string below
json = "{}"
# create an instance of TrailerBase from a JSON string
trailer_base_instance = TrailerBase.from_json(json)
# print the JSON string representation of the object
print(TrailerBase.to_json())

# convert the object into a dict
trailer_base_dict = trailer_base_instance.to_dict()
# create an instance of TrailerBase from a dict
trailer_base_form_dict = trailer_base.from_dict(trailer_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


