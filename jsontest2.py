import json
import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)


# Map of userIds to number of completed TODOS for each user
todos_by_user = {}

#Increment complete TODOs count for each user
for todo in todos:
    if todo["completed"]:
        try:
            #increase users count
            todos_by_user[todo["userId"]] +=1
        except KeyError:
            #this user has not yet been seen - set count to 1
            todos_by_user[todo["userId"]] = 1

#create a sorted list of userIds and num_completed pairs
top_users = sorted(todos_by_user.items(), key = lambda x:x[1], reverse=True)
print(top_users)

max_complete = top_users[0][1]


users = []
for user, num_complete in top_users:
    if num_complete < max_complete:
        break
    users.append(str(user))

max_users = " and ".join(users)


def keep(todo):
    is_complete = todo["completed"]
    has_max_count = str(todo["userId"]) in users
    return is_complete and has_max_count



filtered_todos = list(filter(keep, todos))

print(filtered_todos)
