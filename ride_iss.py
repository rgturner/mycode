#!/usr/bin/python3
"""Alta3 Research - astros on ISS"""

import urllib.request
import json

MAJORTOM = "http://api.open-notify.org/astros.json"

def main():
    """reading json from api"""
    # call the api
    groundctrl = urllib.request.urlopen(MAJORTOM)

    # strip off the attachment (JSON) and read it
    # the problem here, is that it will read out as a string
    helmet = groundctrl.read()

    # show that at this point, our data is str
    # we want to convert this to list / dict
    print(helmet)

    helmetson = json.loads(helmet.decode("utf-8"))

    # this should say bytes
    print(type(helmet))

    # this should say dict
    print(type(helmetson))

    # display the number of astros currently in space
    print("People in space: ", str(helmetson["number"]))

    # display which craft each astro is on
    for astro in helmetson["people"]:
        print(astro["name"], " on the ", astro["craft"])


if __name__ == "__main__":
    main()

