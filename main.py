import pandas
import os
import numpy as np
import folium
from sklearn.utils import shuffle






if __name__ == "__main__":
    ptrDataset = open("./Dataset/Trafik0701.txt")

    count = 0

    a = np.array([])

    mainArray = []

    for eachLine in ptrDataset:
        withoutNewLine = eachLine.split("\n")
        newList = withoutNewLine[0].split(";")
        mainArray.append(newList)

    df = pandas.DataFrame(data=mainArray)

    # df.sample(frac=1)
    df = shuffle(df)
    # print(count)
    #
    #
    # print("Finished")


    ## Nine color for altitude

    colours = ['red', 'blue', 'green', 'purple', 'orange', 'darkred',"lightgray", "gray" ,"black"]






    m = folium.Map(location=[df[3][0], df[4][0]])
    count = 0
    for (idx,row) in df.iterrows():


        if count == 1500:
            break

        print(idx)
        # print(row)
        popupString = "ID: " + row[0] + "\n" + "Date: " + row[1]
        # indexForColour = int(int(row[2])/200)
        # print(indexForColour)

        if row[2] == '':
            altitudeIndex = 0
        else:
            altitudeIndex = int(int(row[2])/300)
        folium.Marker(
            location=[row[3], row[4]],
            popup=popupString,
            icon=folium.Icon(icon='glyphicon-arrow-up',color=colours[altitudeIndex],angle=row[6])
        ).add_to(m)
        count += 1

    m.save("index.html")



