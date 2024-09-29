# ClubMemberDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | User&#39;s username | [optional] 
**url** | **str** | User URL | [optional] 
**images** | [**UserImages**](UserImages.md) |  | [optional] 

## Example

```python
from jikan_openapi.models.club_member_data_inner import ClubMemberDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of ClubMemberDataInner from a JSON string
club_member_data_inner_instance = ClubMemberDataInner.from_json(json)
# print the JSON string representation of the object
print(ClubMemberDataInner.to_json())

# convert the object into a dict
club_member_data_inner_dict = club_member_data_inner_instance.to_dict()
# create an instance of ClubMemberDataInner from a dict
club_member_data_inner_form_dict = club_member_data_inner.from_dict(club_member_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


