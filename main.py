from DownloadingReddit import DownloadingReddit as DR
from UploadingPicsVK import UploadingPicsVK as UP
import sys
sys.path.append("../RedditVk/")


def getValuesFromCL(displayString):
    print(displayString)
    return str(input())


if __name__ == "__main__":
    dr = DR()
    client_id = getValuesFromCL("Input your client id: ")
    client_secret = getValuesFromCL("Input your client secret: ")
    username = getValuesFromCL("Input your username: ")
    password = getValuesFromCL("Input your password: ")
    user_agent = getValuesFromCL("Input your user_agent: ")

    dr.initReddit(client_id, client_secret, password, username, user_agent)

    subreddit = getValuesFromCL("Input name subreddit: ")
    dr.setSubreddit(subreddit)

    path = getValuesFromCL("Input path: ")
    limit = int(getValuesFromCL("Input limit pics: "))

    dr.download(path, limit)

    print("Done!")

    up = UP()
    token = getValuesFromCL("Input your token: ")
    up.initVK(token)

    group_id = getValuesFromCL("Input your group id: ")
    up.initServer(group_id)

    path = getValuesFromCL("Input your uploading path: ")
    startDay = int(getValuesFromCL("Input start day: "))
    startMonth = int(getValuesFromCL("Input start month: "))
    startHour = int(getValuesFromCL("Input start hour: "))
    up.upload(path, startDay, startMonth, startHour)

    print("Done!")
