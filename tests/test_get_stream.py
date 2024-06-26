import pytest
@pytest.mark.parametrize("stream_name_to_check", [
    "CAM01"
])

def test_get_stream(api_client, base_url, auth_token, stream_name_to_check):
    response = api_client.get(f"{base_url}streams/all", headers=auth_token)
    assert response.status_code == 200, f"Failed to retrieve data. Status code {response.status_code}"
    data = response.json()['data']
    # import json
    # print(json.dumps(data[0], indent=4))
    stream_name = [name["stream_name"] for name in data]
    for stream_data in data:
        if stream_data["stream_name"] == stream_name_to_check:
            assert isinstance(stream_data["id"], int), "ID should be an integer"
            assert stream_data["stream_name"] == stream_name_to_check, f"Expected stream_name '{stream_name_to_check}'"
            assert isinstance(stream_data["last_alert_time"], int), "last_alert_time should be an integer"

    for stream_data in data:
        if stream_data['stream_name'] == stream_name_to_check:
            print(stream_data['encoderate'])
            assert stream_data['display_name'] == stream_data['display_name']
            assert stream_data["location_info"] == 82.2, "Expected location_info 82.2"
            assert stream_data["addr_zip"] == "049-3342", "Expected addr_zip '049-3342'"
            assert stream_data["addr_pref"] == "北海道", "Expected addr_pref '北海道'"
            assert stream_data["addr_city"] == "山崎", "Expected addr_city '山崎'"
            assert stream_data["addr_town"] == "二海郡八雲町", "Expected addr_town '二海郡八雲町'"
            assert stream_data["uri"] == "nxtp://239.209.66.3:20310", "Expected uri 'nxtp://239.209.66.3:20310'"
            assert stream_data["encoderate"] == "標準ＭＰＥＧ２(6Mbps)", "Expected encoderate '標準ＭＰＥＧ２(6Mbps)'"

    access_and_preset_info = [name["access_and_preset_info"] for name in data]
    for i in access_and_preset_info:
        if i['stream_name'] in {"CAM02","CAM01"}:
            assert i["server_name"] == 'DEB-HYPV-d2aa99dc2d0741ce90a795d791cf58ff'

        if i["stream_name"] == "CAM01":
            assert i["camera_code"] == i["camera_code"]
            assert i['camera_ip'] == i['camera_ip']

