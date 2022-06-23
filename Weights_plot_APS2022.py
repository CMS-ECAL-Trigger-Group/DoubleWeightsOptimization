##-- Want to plot rejected spike times from a strip with OOT weights for CMS plot approval 
##-- Need input sample, 2 sets of weights to use 
ol = "/eos/user/a/atishelm/www/EcalL1Optimization/APS_2022_AprilMeeting/"
f = "/eos/user/a/atishelm/ntuples/EcalL1Optimization/DoubleWeights/GradientDescent/PU50_1M_Events_3GeVminSpikes/samples/hadded.root"
f_u = uproot.open(f)

##-- Plot weights 

PUoptimized_weights_first_set = [0, 0, -0.546875, -0.546875, 0.265625, 0.484375, 0.34375, 0, 0, 0]

weights_two_0p5 = [0, 0, -0.953125, 0.0, 0.0, 1.0, -0.046875, 0, 0, 0] # including 1.0 which cannot actually be encoded
weights_two_1p0 = [0, 0, -0.890625, 0, -0.125, 1.0, 0.015625, 0, 0, 0]
weights_two_1p5 = [0, 0, -0.84375, 0, -0.265625, 1.0, 0.109375, 0, 0, 0]
weights_two_2p0 = [0, 0, -0.78125, 0, -0.40625, 1, 0.1875, 0, 0, 0]
weights_two_2p5 = [0, 0, -0.703125, 0.0, -0.546875, 0.984375, 0.265625, 0, 0, 0] #modified mindelta 2.5 weights for electronics input
weights_two_3p0 = [0, 0, -0.671875, 0, -0.671875, 1, 0.34375, 0, 0, 0]
weights_two_5p0 = [0, 0, -0.46875, 0.0, -1.0, 1.0, 0.0625, 0, 0, 0] # including 1.0 which cannot actually be encoded
weights_two_10p0 = [0, 0, -0.0625, 0, -1, 1, 0.0625, 0, 0, 0]
weights_two_15p0 = [0, 0, 0, 0.078125, -1.0, -0.078125, 1, 0, 0, 0]

samples = [i for i in range(1,11)]

fig, ax = plt.subplots()
fig.set_dpi(100)

delta_mins = ["0p5", "1p0", "1p5", "2p0", "2p5", "3p0", "5p0", "10p0", "15p0"]

delta_min_label_dict = {
    "0p5" : "0.5",
    "1p0" : "1.0",
    "1p5" : "1.5",
    "2p0" : "2.0",
    "2p5" : "2.5",
    "3p0" : "3.0",
    "5p0" : "5.0",
    "10p0" : "10.0",
    "15p0" : "15.0"
}


plt.plot(samples, PUoptimized_weights_first_set, label = "In-time", marker = '.', linestyle = '-', markersize = 12)

for delta_min in delta_mins:
    exec("weights = weights_two_%s"%(delta_min))
    delta_min_label = delta_min_label_dict[delta_min]
    plt.plot(samples, weights, label = r"$\delta_{min}$ = %s GeV"%(delta_min_label), marker = '.', linestyle = '-', markersize = 12)

# plt.plot(samples, weights_two_0p5, label = r"$\delta_{min}$ = 0.5", marker = '.', linestyle = '-', markersize = 12)
# plt.plot(samples, weights_two_2p5, label = r"$\delta_{min}$ = 2.5", marker = '.', linestyle = '-', markersize = 12)
# plt.plot(samples, weights_two_5p0, label = r"$\delta_{min}$ = 5", marker = '.', linestyle = '-', markersize = 12)

plt.title("Weight values", fontsize = 20)
plt.ylabel("Weight value", fontsize = 15)
plt.xlabel("Sample", fontsize = 15)
plt.grid()
plt.legend(bbox_to_anchor = (1,1))
# plt.show()
fig.set_size_inches(10,5)
fig.tight_layout()
plt.savefig("%s/Weight_Values_APS2022.png"%(ol))
plt.savefig("%s/Weight_Values_APS2022.pdf"%(ol))
plt.close()

print("DONE")
