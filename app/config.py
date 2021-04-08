import sys
import os


try:
    port = int(os.environ.get("PORT", "8080"))
except ValueError:
    port = -1
if not 1 <= port <= 65535:
    print("Please make sure the PORT environment variable is an integer between 1 and 65535")
    sys.exit(1)

try:
    api_id = int(os.environ["1816605"])
    api_hash = os.environ["8f9e9b0867f789de06691ac37e1be25b"]
except (KeyError, ValueError):
    print("Please set the API_ID and API_HASH environment variables correctly")
    print("You can get your own API keys at https://my.telegram.org/apps")
    sys.exit(1)

try:
    chat_id = int(os.environ["-1001315186031"])
except (KeyError, ValueError):
    print("Please set the CHAT_ID environment variable correctly")
    sys.exit(1)

try:
    session_string = os.environ["BQBl34IrmIruC0jBY82StcZ33HKVku74mutuf7QF6OoQyzloCAjlX54OS4FfO2gZ_Cjh4svYE1nWbhOePHcdF5bhskSzNaAT5njjwlaxEMVPP87heOPBK6Rd1gJd81rtjHUfg4tLffiCnP727BgC8hIjTR8pSY8-VO33Aw6qR1LP1QW5NekFn83o4qZOknDsn9Zl2WQCZTC9B3LW--fFsmKxqgH2CHkE6vrH5HAswrg15rkKMuLQ-nK8soMNG8AY4OFdan-GHmc47wKpnbUQnEA7QmGMM8xuC33OGNUvrluyl0kzFoiN6AfuNuglgbGo5qOKgNy4Nk_ZSk0phPH8IPlnTBZQAQA"]
except (KeyError, ValueError):
    print("Please set the SESSION_STRING environment variable correctly")
    sys.exit(1)

host = os.environ.get("HOST", "0.0.0.0")
