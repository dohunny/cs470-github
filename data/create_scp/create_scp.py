import os, random


train_mix_scp = 'data/scp_ss_8k/tr_mix.scp'
train_s1_scp = 'data/scp_ss_8k/tr_s1.scp'
train_s2_scp = 'data/scp_ss_8k/tr_s2.scp'


train_mix = '../final_dataset/train/mixed_data'
train_s1 = '../final_dataset/train/s1'
train_s2 = '../final_dataset/train/s2'


tr_mix = open(train_mix_scp,'w')
for root, dirs, files in os.walk(train_mix):
    files.sort()
    tr_files = random.sample(files, k=600)
    for file in tr_files:
        tr_mix.write(file+" "+root+'/'+file)
        tr_mix.write('\n')


tr_s1 = open(train_s1_scp,'w')
for root, dirs, files in os.walk(train_s1):
    files.sort()
    for file in tr_files:
        tr_s1.write(file+" "+root+'/'+file)
        tr_s1.write('\n')


tr_s2 = open(train_s2_scp,'w')
for root, dirs, files in os.walk(train_s2):
    files.sort()
    for file in tr_files:
        tr_s2.write(file+" "+root+'/'+file)
        tr_s2.write('\n')

test_mix_scp = 'data/scp_ss_8k/tt_mix.scp'
test_s1_scp = 'data/scp_ss_8k/tt_s1.scp'
test_s2_scp = 'data/scp_ss_8k/tt_s2.scp'

test_mix = '../final_dataset/test/mixed_data'
test_s1 = '../final_dataset/test/s1'
test_s2 = '../final_dataset/test/s2'

tt_mix = open(test_mix_scp,'w')
for root, dirs, files in os.walk(test_mix):
    files.sort()
    tt_files = random.sample(files, k=100)
    for file in tt_files:
        tt_mix.write(file+" "+root+'/'+file)
        tt_mix.write('\n')


tt_s1 = open(test_s1_scp,'w')
for root, dirs, files in os.walk(test_s1):
    files.sort()
    for file in tt_files:
        tt_s1.write(file+" "+root+'/'+file)
        tt_s1.write('\n')


tt_s2 = open(test_s2_scp,'w')
for root, dirs, files in os.walk(test_s2):
    files.sort()
    for file in tt_files:
        tt_s2.write(file+" "+root+'/'+file)
        tt_s2.write('\n')

cv_mix_scp = 'data/scp_ss_8k/cv_mix.scp'
cv_s1_scp = 'data/scp_ss_8k/cv_s1.scp'
cv_s2_scp = 'data/scp_ss_8k/cv_s2.scp'

cv_mix = '../final_dataset/valid/mixed_data'
cv_s1 = '../final_dataset/valid/s1'
cv_s2 = '../final_dataset/valid/s2'

cv_mix_file = open(cv_mix_scp,'w')
for root, dirs, files in os.walk(cv_mix):
    files.sort()
    cv_files = random.sample(files, k=200)
    for file in cv_files:
        cv_mix_file.write(file+" "+root+'/'+file)
        cv_mix_file.write('\n')


cv_s1_file = open(cv_s1_scp,'w')
for root, dirs, files in os.walk(cv_s1):
    files.sort()
    for file in cv_files:
        cv_s1_file.write(file+" "+root+'/'+file)
        cv_s1_file.write('\n')


cv_s2_file = open(cv_s2_scp,'w')
for root, dirs, files in os.walk(cv_s2):
    files.sort()
    for file in cv_files:
        cv_s2_file.write(file+" "+root+'/'+file)
        cv_s2_file.write('\n')