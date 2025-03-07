import random
random.seed(6)

indices = [1536, 8194, 9730, 7, 1543, 4103, 9231, 3092, 7704, 2078, 1572, 6183, 9786, 6716, 8252, 1598, 7229, 3649, 6222, 3161, 603, 3173, 5232, 8819, 7294, 6783, 4737, 8835, 9859, 10378, 7309, 3214, 9882, 3230, 7326, 10402, 4770, 3245, 9401, 4286, 3262, 205, 2771, 2262, 3291, 9435, 5855, 6376, 748, 9964, 8432, 7925, 4350, 7946, 9995, 5904, 6928, 279, 5920, 4389, 7974, 1320, 5933, 6958, 8007, 8009, 5454, 2385, 358, 8554, 9070, 3438, 881, 4467, 6516, 1914, 5498, 4986, 7040, 9608, 10135, 5015, 8605, 1443, 1959, 9643, 4012, 9138, 10162, 9652, 4019, 1459, 1469, 8640, 465, 3036, 6113, 1525, 6137, 5116]
indices = sorted(indices)
gt = '0 1 0 0 1 0 0 0 0 0 0 1 1 1 1 0 1 1 1 1 0 0 1 1 1 0 0 1 1 0 0 0 0 1 1 1 0 0 0 0 0 0 0 1 0 1 0 0 0 1 0 0 0 0 0 1 0 0 0 1 1 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 1 0 0 0 0 0 0 1 1 0 1 1 0 1 1 0 0 1 1 1 0 1 1'
gt = gt.split(' ')
gt = [int(i) for i in gt]

with open('temp/female_session1_fps20_smoothed.txt', 'r') as file:
    info = file.readlines()
info = [i.split(' ') for i in info]
preds = [i[0] for i in info]
pts = [[(int(i[1].strip()[1:-1]), int(i[2].strip()[:-1])), 
        (int(i[3].strip()[1:-1]), int(i[4].strip()[:-1]))] for i in info]

correct = 0
for i in range(len(indices)):
    pred = preds[indices[i]]
    pt = pts[indices[i]]
    bool_pred = 1 if pred == 'True' else 0
    
    if gt[i] == bool_pred:
        correct += 1

print(correct)
