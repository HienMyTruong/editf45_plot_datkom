
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv("data/top50.csv")


def len_extractor(row):
    row = str(row)
    row = row.split(" ")
    row = [c for c in row if "Len=" in c][0]
    row = [c for c in row if c.isnumeric()]
    row = "".join(row)
    row = int(row)
    return row


def bit_rate():
    times = data["Time"].tolist()
    lengths_bytes = data["Length"].tolist()
    lengths_bytes = np.array(lengths_bytes)
    lengths_bits = lengths_bytes * 8
    #c = np.cumsum(lengths_bits)

    assert len(times) > 0
    tot_time = times[-1]

    assert tot_time > 0
    return lengths_bits.sum() / tot_time




print(bit_rate())


breakpoint()

data["package_size"] = data["Info"].map(len_extractor)
print(data["package_size"])
data = data[data['Protocol'] == 'TCP']
data = data[data["Info"].str.contains("4070", regex=False)]
data.to_csv(r'/Users/hientruong/PycharmProjects/dataanalys/data20.csv', index=False, header=True)

lengths_over_hundred = data[data["package_size"] >= 100]
print(sum(lengths_over_hundred["package_size"]) / lengths_over_hundred.shape[0])



#hur många paket som skickas
#hur många ack det finns
#requestsAndAck = data[data['Info'].str.contains("[PSH, ACK]") & data['Info'].str.contains("[ACK]")]

requests = data[data['Info'].str.contains("[PSH, ACK]", regex=False)]

ack = data[data['Info'].str.contains("[ACK]", regex=False)]
print(sum_tobits()/tot_time)
#data.info()

print(ack.shape)
print(requests.shape)
#print(requests)

#requests.to_csv(r'/Users/hientruong/PycharmProjects/dataanalys/requests0.csv', index=False, header=True)




plt.yscale('log', base=10)
plt.plot(requests["Time"], requests["Length"])
#plt.plot(data["Time"], data["Length"])
plt.xlabel('Seconds Since First Captured Packet')
plt.ylabel('byte Length')
plt.tight_layout()
plt.gca().yaxis.set_major_formatter(lambda x, pos: str(int(round(x))))

#plt.figure(figsize=(5, 2))
plt.show()




