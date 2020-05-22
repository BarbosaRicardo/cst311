# initialize variables 
SampleRTT = 80
SampleRTT1 = 30
SampleRTT2 = 40
SampleRTT3 = 100
SampleRTT4 = 40

# initialize round trip times
EstimatedRTT = SampleRTT
DevRTT = SampleRTT/2
Timeout = 0

# initialize alpha and beta
a = 0.125
b = 0.25

EstimatedRTT = (1-a)*EstimatedRTT + a*SampleRTT
DevRTT = (1-b)*DevRTT + b*abs(SampleRTT - EstimatedRTT)
print("\nEstimatedRTT1: ", EstimatedRTT)
print("DevRTT1: ", DevRTT)
print("\n")

EstimatedRTT = (1-a)*EstimatedRTT + a*SampleRTT1
DevRTT = (1-b)*DevRTT + b*abs(SampleRTT1 - EstimatedRTT)
print("EstimatedRTT2: ", EstimatedRTT)
print("DevRTT2: ", DevRTT)
print("\n")

EstimatedRTT = (1-a)*EstimatedRTT + a*SampleRTT2
DevRTT = (1-b)*DevRTT + b*abs(SampleRTT2 - EstimatedRTT)
print("EstimatedRTT3: ", EstimatedRTT)
print("DevRTT3: ", DevRTT)
print("\n")

EstimatedRTT = (1-a)*EstimatedRTT + a*SampleRTT3
DevRTT = (1-b)*DevRTT + b*abs(SampleRTT3 - EstimatedRTT)
print("EstimatedRTT4: ", EstimatedRTT)
print("DevRTT4: ", DevRTT)
print("\n")


EstimatedRTT = (1-a)*EstimatedRTT + a*SampleRTT4
DevRTT = (1-b)*DevRTT + b*abs(SampleRTT4 - EstimatedRTT)
print("EstimatedRTT FINAL: ", EstimatedRTT)
print("DevRTT FINAL: " , DevRTT)

Timeout = EstimatedRTT + 4*DevRTT
print("Timeout FINAL: " , Timeout)










