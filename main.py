
import matplotlib.pyplot as plt
import pandas as pd


data = pd.read_csv("data/data2.csv")
data1 = pd.read_csv("data/data2.csv")


def len_extractor(row):
    row = str(row)
    row = row.split(" ")
    row = [c for c in row if "Len=" in c][0]
    row = [c for c in row if c.isnumeric()]
    row = "".join(row)
    row = int(row)
    return row


data1["lengths"] = data["Info"].map(len_extractor)
print(data1)

data = data[data['Protocol'] == 'TCP']
data = data[data["Info"].str.contains("4070", regex=False)]
data1.to_csv(r'/Users/hientruong/PycharmProjects/dataanalys/data20.csv', index=False, header=True)

lengths_over_hundred = data1[data1["lengths"] >= 100]
print(sum(lengths_over_hundred["lengths"]))

breakpoint()
#hur många paket som skickas
#hur många ack det finns
requestsAndAck = data[data['Info'].str.contains("[PSH, ACK]") & data['Info'].str.contains("[ACK]")]

requests = data[data['Info'].str.contains("[PSH, ACK]", regex=False)]

ack = data[data['Info'].str.contains("[ACK]", regex=False)]

#data.info()

print(ack.shape)
print(requests.shape)
#print(requests)

requests.to_csv(r'/Users/hientruong/PycharmProjects/dataanalys/requests0.csv', index=False, header=True)




plt.yscale('log', base=10)
plt.plot(requests["Time"], requests["Length"])
#plt.plot(data["Time"], data["Length"])
plt.xlabel('Seconds Since First Captured Packet')
plt.ylabel('byte Length')
plt.tight_layout()
plt.gca().yaxis.set_major_formatter(lambda x, pos: str(int(round(x))))

#plt.figure(figsize=(5, 2))
plt.show()


