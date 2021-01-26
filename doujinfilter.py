
#this script is not meant to be run, only imported
if __name__ == "__main__":
    print("Cannot run this script directly!")
    quit()

"""
returns True when it contains blacklisted tags
"""
def CheckBlacklistedTags( doujinTags, blacklistedTags):
    #scan the tags for blacklisted entries
    clearOfBadTags = True
    for i in doujinTags:
        for b in blacklistedTags:
            #skip comments
            if b.startswith("#"):
                continue
            if i == b.strip():
                clearOfBadTags = False
                break
        if not clearOfBadTags:
            break

    return not clearOfBadTags
