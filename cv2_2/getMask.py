import queue
import cv2
import requests


def get_mask1(src,src1, x, y):

    q = queue.Queue()
    q2=queue.Queue()
    q.put(x)
    q2.put(y)

    idx=0
    while q.qsize() != 0:

        # print(q.qsize())
        idx=idx+1


        x1=q.get()
        y1=q2.get()
        x=x1
        y=y1
        li=[-1,1,0,2]
        for i in range(0, 2, 1):
            for j in range(0, 2, 1):
                if i == 0 and j == 0 :
                    continue;
                if x1<0 or y1<0 or x1>=800 or y1>=350:
                    continue
                x1 = x + i
                y1 = y + j


                if src1[x1][y1][0] == 0 and src1[x1][y1][1] == 0 and src1[x1][y1][2] == 0:
                    continue
                # print(x,y,src[x][y])
                # print(x1,y1,src[x1][y1])
                dis = 0
                x4=src[x][y][0]
                y4=src[x1][y1][0]
                x2 = src[x][y][1]
                y2 = src[x1][y1][1]
                x3 = src[x][y][2]
                y3 = src[x1][y1][2]
                if x2>y2:
                    dis+=x2-y2
                else:
                    dis+=y2-x2
                if x3>y3:
                    dis+=x3-y3
                else:
                    dis+=y3-x3
                if x4>y4:
                    dis+=x4-y4
                else:
                    dis+=y4-x4

                print(x,y,x1,y1,dis)
                if dis < 30 and src1[x1][y1][0] != 0 and src1[x1][y1][1] != 0 and src1[x1][y1][2] != 0:
                    q.put(x1)
                    q2.put(y1)
                    src1[x1][y1] = [0, 0, 0]
                x1 = x1 - i
                y1 = y1 - j

        # print(x1,y1)
    print(idx)
    cv2.imwrite(f'./1.jpg', src1)
def get_mask2(src,src1, x, y):

    q = queue.Queue()
    q2=queue.Queue()
    q.put(x)
    q2.put(y)

    idx=0
    while q.qsize() != 0:

        # print(q.qsize())
        idx=idx+1


        x1=q.get()
        y1=q2.get()
        x=x1
        y=y1
        li=[-1,1,0,2]
        for i in range(0, 2, 1):
            for j in range(-1, 1, 1):
                if i == 0 and j == 0 :
                    continue;
                if x1<0 or y1<0 or x1>=800 or y1>=350:
                    continue
                x1 = x + i
                y1 = y + j


                if src1[x1][y1][0] == 0 and src1[x1][y1][1] == 0 and src1[x1][y1][2] == 0:
                    continue
                # print(x,y,src[x][y])
                # print(x1,y1,src[x1][y1])
                dis = 0
                x4=src[x][y][0]
                y4=src[x1][y1][0]
                x2 = src[x][y][1]
                y2 = src[x1][y1][1]
                x3 = src[x][y][2]
                y3 = src[x1][y1][2]
                if x2>y2:
                    dis+=x2-y2
                else:
                    dis+=y2-x2
                if x3>y3:
                    dis+=x3-y3
                else:
                    dis+=y3-x3
                if x4>y4:
                    dis+=x4-y4
                else:
                    dis+=y4-x4

                print(x,y,x1,y1,dis)
                if dis < 30 and src1[x1][y1][0] != 0 and src1[x1][y1][1] != 0 and src1[x1][y1][2] != 0:
                    q.put(x1)
                    q2.put(y1)
                    src1[x1][y1] = [0, 0, 0]
                x1 = x1 - i
                y1 = y1 - j

        # print(x1,y1)
    print(idx)
    cv2.imwrite(f'./1.jpg', src1)
def get_mask3(src,src1, x, y):

    q = queue.Queue()
    q2=queue.Queue()
    q.put(x)
    q2.put(y)

    idx=0
    while q.qsize() != 0:

        # print(q.qsize())
        idx=idx+1


        x1=q.get()
        y1=q2.get()
        x=x1
        y=y1
        li=[-1,1,0,2]
        for i in range(-1, 1, 1):
            for j in range(-1, 1, 1):
                if i == 0 and j == 0 :
                    continue;
                if x1<0 or y1<0 or x1>=800 or y1>=350:
                    continue
                x1 = x + i
                y1 = y + j


                if src1[x1][y1][0] == 0 and src1[x1][y1][1] == 0 and src1[x1][y1][2] == 0:
                    continue
                # print(x,y,src[x][y])
                # print(x1,y1,src[x1][y1])
                dis = 0
                x4=src[x][y][0]
                y4=src[x1][y1][0]
                x2 = src[x][y][1]
                y2 = src[x1][y1][1]
                x3 = src[x][y][2]
                y3 = src[x1][y1][2]
                if x2>y2:
                    dis+=x2-y2
                else:
                    dis+=y2-x2
                if x3>y3:
                    dis+=x3-y3
                else:
                    dis+=y3-x3
                if x4>y4:
                    dis+=x4-y4
                else:
                    dis+=y4-x4

                print(x,y,x1,y1,dis)
                if dis < 30 and src1[x1][y1][0] != 0 and src1[x1][y1][1] != 0 and src1[x1][y1][2] != 0:
                    q.put(x1)
                    q2.put(y1)
                    src1[x1][y1] = [0, 0, 0]
                x1 = x1 - i
                y1 = y1 - j

        # print(x1,y1)
    print(idx)
    cv2.imwrite(f'./1.jpg', src1)
def get_mask4(src,src1, x, y):

    q = queue.Queue()
    q2=queue.Queue()
    q.put(x)
    q2.put(y)

    idx=0
    while q.qsize() != 0:

        # print(q.qsize())
        idx=idx+1


        x1=q.get()
        y1=q2.get()
        x=x1
        y=y1
        li=[-1,1,0,2]
        for i in range(-1, 1, 1):
            for j in range(0, 2, 1):
                if i == 0 and j == 0 :
                    continue;
                if x1<0 or y1<0 or x1>=800 or y1>=350:
                    continue
                x1 = x + i
                y1 = y + j


                if src1[x1][y1][0] == 0 and src1[x1][y1][1] == 0 and src1[x1][y1][2] == 0:
                    continue
                # print(x,y,src[x][y])
                # print(x1,y1,src[x1][y1])
                dis = 0
                x4=src[x][y][0]
                y4=src[x1][y1][0]
                x2 = src[x][y][1]
                y2 = src[x1][y1][1]
                x3 = src[x][y][2]
                y3 = src[x1][y1][2]
                if x2>y2:
                    dis+=x2-y2
                else:
                    dis+=y2-x2
                if x3>y3:
                    dis+=x3-y3
                else:
                    dis+=y3-x3
                if x4>y4:
                    dis+=x4-y4
                else:
                    dis+=y4-x4

                print(x,y,x1,y1,dis)
                if dis < 30 and src1[x1][y1][0] != 0 and src1[x1][y1][1] != 0 and src1[x1][y1][2] != 0:
                    q.put(x1)
                    q2.put(y1)
                    src1[x1][y1] = [0, 0, 0]
                x1 = x1 - i
                y1 = y1 - j

        # print(x1,y1)
    print(idx)
    cv2.imwrite(f'./1.jpg', src1)

img2 = cv2.imread('./1.jpg')
img1 = cv2.imread('./output3.jpg')
get_mask1(img1,img2, 350, 201)
get_mask2(img1,img2, 350, 201)
get_mask3(img1,img2, 350, 201)
get_mask4(img1,img2, 350, 201)

