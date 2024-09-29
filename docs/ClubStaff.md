# ClubStaff

Club Staff Resource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ClubStaffDataInner]**](ClubStaffDataInner.md) |  | [optional] 

## Example

```python
from jikan_openapi.models.club_staff import ClubStaff

# TODO update the JSON string below
json = "{}"
# create an instance of ClubStaff from a JSON string
club_staff_instance = ClubStaff.from_json(json)
# print the JSON string representation of the object
print(ClubStaff.to_json())

# convert the object into a dict
club_staff_dict = club_staff_instance.to_dict()
# create an instance of ClubStaff from a dict
club_staff_form_dict = club_staff.from_dict(club_staff_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


