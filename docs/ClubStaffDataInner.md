# ClubStaffDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | User URL | [optional] 
**username** | **str** | User&#39;s username | [optional] 

## Example

```python
from jikan_openapi.models.club_staff_data_inner import ClubStaffDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of ClubStaffDataInner from a JSON string
club_staff_data_inner_instance = ClubStaffDataInner.from_json(json)
# print the JSON string representation of the object
print(ClubStaffDataInner.to_json())

# convert the object into a dict
club_staff_data_inner_dict = club_staff_data_inner_instance.to_dict()
# create an instance of ClubStaffDataInner from a dict
club_staff_data_inner_form_dict = club_staff_data_inner.from_dict(club_staff_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


