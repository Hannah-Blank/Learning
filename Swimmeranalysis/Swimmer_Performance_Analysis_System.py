FN = "Darius-13-100m-Fly.txt"
FOLDER = "swimdata/"
with open(FOLDER + FN) as df:
    data = df.readlines()
times = data[0].strip().split(",")