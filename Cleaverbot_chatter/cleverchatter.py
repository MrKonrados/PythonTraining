import random
import time
from cleverwrap import CleverWrap

API_KEY_1 = "CC22xhxFPYAVVMo9i7hPn8bZxpw"
API_KEY_2 = "CC232J2D3dL0YQjF2i8HkPRj92w"

jas = CleverWrap(API_KEY_1)
malgosia = CleverWrap(API_KEY_2)


ans = input("Reset speach ID? [Y/N]: ")
if ans.lower() == 'y':
    jas.reset()
    malgosia.reset()
    print("Done...")
malgosia_talk="Hi"
for i in range(500):
    jas_talk = jas.say(malgosia_talk)
    print("[jas] >> ", jas_talk)
    malgosia_talk = malgosia.say(jas_talk)
    print("[{}][malgosia_talk] >> ".format(i), malgosia_talk)
    time.sleep(1)


# response = []
# with open('questions.txt', 'r', encoding='utf8') as f:
#     response = f.read().splitlines()
#
# for i in range(100):
#     talk = random.choice(response)
#     print(talk)
#     response.append(jas.say(talk))
#     print("[{}/100]>>>".format(i), response[-1])
#     i += 1
#     time.sleep(2)
#
# with open("questions.txt", "w", encoding="utf8") as f:
#     for r in response:
#         f.write(r)
#         f.write("\n")