import statistics as st
import math

dataset = [98.8, 98.4, 105.2, 97.8, 104.0, 98.8, 111.2, 98.3, 103.2, 98.8]
# MAD(Dataset) = median( | dataset - median(dataset) |)
# Median ± 2 * MAD
median = st.median(dataset)
print(st.mean(dataset))
print(st.stdev(dataset))
# print(median)

# d2 = []
# for d in dataset:
#     d2.append(abs(d - median))
# mad = st.median(d2)
# print(d2)
# print(mad)

