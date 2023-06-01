import copy

# way_point_dict = {
#             "coordinates" : {"x": "1", "y": "1", "z": "1"}, 
#             "id" : "1", 
#             "name" : "1", 
#             "tasktype" : "point",
#             "taskState" : "running"
#             }

# msg_dict = {
#     "id": "1", 
#     "name": "1", 
#     "missionState" : "running",
#     "waypoints": [
#         ]
#     }

# i = 0
# for i in range(3):
#     i += 1
#     way_point_dict["id"] = str(i)
#     msg_dict["waypoints"].append(copy.copy(way_point_dict))

# print(msg_dict)

msg_received = eval("{'id': '1', 'name': '1', 'missionState': 'running', 'waypoints': [{'coordinates': {'x': '1', 'y': '1', 'z': '1'}, 'id': '1', 'name': '1', 'tasktype': 'point', 'taskState': 'running'}, {'coordinates': {'x': '1', 'y': '1', 'z': '1'}, 'id': '2', 'name': '1', 'tasktype': 'point', 'taskState': 'running'}, {'coordinates': {'x': '1', 'y': '1', 'z': '1'}, 'id': '3', 'name': '1', 'tasktype': 'point', 'taskState': 'running'}]}")
