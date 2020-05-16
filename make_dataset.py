import os


os.mkdir('./dataset')
#os.chdir('./datasetRaw')
print(os.getcwd)

train = 0.7
test = 0.17
val = 0.13

def make_set(method, dir_name, num, class_dir):
    dir_name_method = './dataset/%s/%s' % (dir_name,method)
    os.mkdir(dir_name_method)
    for i in range(num):
        os.rename(class_dir + '/%s/%s%d.jpg' % (dir_name,dir_name,i),)

os.mkdir('./dataset/train')
os.mkdir('./dataset/test')
os.mkdir('./dataset/val')

for i, dir_name in enumerate(os.listdir('./datasetRaw')):
    class_dir = './datasetRaw/%s' % dir_name
    tot = len(os.listdir(class_dir))
    train_ = int(tot * train)
    test_ = int(tot * test)
    val_ = tot - train_ - test_
    print(train_, test_, val_)

    

    os.mkdir('./dataset/train/%s' % dir_name)
    for i in range(1,train_+1):
        os.rename(class_dir+'/%s%d.jpg'%(dir_name,i),'./dataset/train/%s/%s%d.jpg' % (dir_name,dir_name,i))
        print("moved "+class_dir+'/%s/%s%d.jpg'%(dir_name,dir_name,i))
        
    os.mkdir('./dataset/test/%s' % dir_name)
    for i in range(train_+1,train_+test_+1):
        os.rename(class_dir+'/%s%d.jpg'%(dir_name,i),'./dataset/test/%s/%s%d.jpg' % (dir_name,dir_name,i-train_))
        print("moved "+class_dir+'/%s/%s%d.jpg'%(dir_name,dir_name,i))
        
    os.mkdir('./dataset/val/%s' % dir_name)
    for i in range(train_+test_+1,train_+test_+val_+1):
        os.rename(class_dir+'/%s%d.jpg'%(dir_name,i),'./dataset/val/%s/%s%d.jpg' % (dir_name,dir_name,i-train_-test_))
        print("moved "+class_dir+'/%s/%s%d.jpg'%(dir_name,dir_name,i))
