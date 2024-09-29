# StreamingLinks

Streaming links

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AnimeFullExternalInner]**](AnimeFullExternalInner.md) |  | [optional] 

## Example

```python
from jikan_openapi.models.streaming_links import StreamingLinks

# TODO update the JSON string below
json = "{}"
# create an instance of StreamingLinks from a JSON string
streaming_links_instance = StreamingLinks.from_json(json)
# print the JSON string representation of the object
print(StreamingLinks.to_json())

# convert the object into a dict
streaming_links_dict = streaming_links_instance.to_dict()
# create an instance of StreamingLinks from a dict
streaming_links_form_dict = streaming_links.from_dict(streaming_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


