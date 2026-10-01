# def msg(act, name):
#     if act == "Enter":
#         return name+"님이 들어왔습니다."
#     else:  # act == "Leave"
#         return name+"님이 나갔습니다."
    

# def solution(record):
#     answer = []
#     users = {}
    
#     for r in record:
#         splitRecord = r.split()
#         command = splitRecord[0]
#         userId = splitRecord[1]
#         if command == "Leave":
#             if userId in users:
#                 users[userId].append((command, ""))
#             else:
#                 users[userId] = [(command, "")]
#         else:
#             if userId in users:
#                 users[userId].append((command, splitRecord[2]))
#             else:
#                 users[userId] = [(command, splitRecord[2])]

#     nicknames = {}

#     for userId, action in users.items():
#         for command, name in reversed(action):
#             if command == "Enter" or command == "Change":
#                 nicknames[userId] = name
#                 break
    
#     for output in record:
#         splitOutput = output.split()
#         if splitOutput[0] != "Change":
#             answer.append(msg(splitOutput[0], nicknames[splitOutput[1]]))
            
#     return answer

def solution(record):
    users = {}  # (uid: 닉네임)
    history = []  # 들어가고 나가는 기록
    result = []
    
    for r in record:
        com_list = r.split()
        
        # 나감
        if len(com_list) == 2:
            com, uid = com_list[0], com_list[1]
        else:  # 닉네임 변경 / 들어감
            com, uid, nickname = com_list[0], com_list[1], com_list[2]
        
        if com == "Change":  # 닉네임 변경
            users[uid] = nickname  
        elif com == "Enter":  # 들어감
            history.append(("Enter", uid))
            users[uid] = nickname
        elif com == "Leave":  # 나감
            history.append(("Leave", uid))
    
    for com, uid in history:
        if com == "Enter":  # 들어감
            result.append(f"{users[uid]}님이 들어왔습니다.")
        elif com == "Leave":  # 나감
            result.append(f"{users[uid]}님이 나갔습니다.")
    
    return result