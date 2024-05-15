# coding=utf-8
"""
@Author:lts
@Time:2024/3/22 15:39
@description:
"""
import numpy as np
import cv2

from PIL import Image

def overlay_pixel(img, img_over, img_over_x, img_over_y):
    """
    粘贴图像
    :param img: 背景图像
    :param img_over: 前景图像
    :param img_over_x: 前景图像在背景图像上的横坐标
    :param img_over_y: 前景图像在背景图像上的纵坐标
    :return: 粘贴“前景图像”后的“背景图像”
    """
    img_h, img_w, img_p = img.shape # 背景图像宽、高、通道数
    img_over_h, img_over_w, img_over_c = img_over.shape # 前景图像高、宽、通道数
    img_over = cv2.cvtColor(img_over, cv2.COLOR_BGR2BGRA) # 转换成4通道图像
    for w in range(0, img_over_w): # 遍历列
        for h in range(0, img_over_h): # 遍历行
            if img_over[h, w, 3] != 0: # 如果不是全透明的像素
                for c in range(0, 3): # 遍历三个通道
                    x = img_over_x + w # 覆盖像素的横坐标
                    y = img_over_y + h # 覆盖像素的纵坐标S
                    if x >= img_w or y >= img_h: # 如果坐标超出最大宽高
                        break # 不做操作
                    img[y, x, c] = img_over[h, w, c] # 覆盖像素
    return img # 粘贴“前景图像”后的“背景图像”


def create_wj_07_bg():
    demo_wuj_plate_img_path= r'../wujing_bg_conf/警-旧-单行-正常比例.png'
    img = cv2.imdecode(np.fromfile(demo_wuj_plate_img_path, dtype=np.uint8), -1)

    # img=cv2.cvtColor(img,cv2.COLOR_BGRA2GRAY)
    img=cv2.cvtColor(img,cv2.COLOR_BGRA2BGR)
    img_copy=img.copy()
    logo=img_copy[20:60,129:164]
    print(img)
    # imgcrop=img[30:113,12:103].copy()
    # imgcrop_gray=cv2.cvtColor(imgcrop,cv2.COLOR_BGRA2GRAY)
    # imgcrop[imgcrop_gray>150]=[255,255,255]
    fill_line_img = img[30:53, 170:190]
    # big_file_img=cv2.resize(fill_line_img,(488-189,120-18))

    # img[18:120,189:488]=cv2.resize(fill_line_img,(488-189,120-18))
    # img[60:117,105:189]=cv2.resize(fill_line_img,(189-105,117-60))

    img[15:128,8:488]=[255,255,255]
    wj_chars_img=cv2.imread('../wujing_bg_conf/666_1.png')
    # img[30:113, 12:102] = cv2.resize(wj_chars_img, (102 - 12, 113 - 30),interpolation=cv2.INTER_LANCZOS4)
    # img[30:112, 12:102] = cv2.resize(wj_chars_img, (102 - 12, 113 - 30),interpolation=cv2.INTER_LANCZOS4)
    img[30:112, 12:102] = wj_chars_img
    img[20:60,129:164] = logo



    # cv2.imwrite('wujing_bg_conf/wj_07_bg_0.png',img)
    cv2.imshow(f'xxx',img)
    cv2.waitKey()
    cv2.destroyAllWindows()

    img_bg_2 = img.copy()
    point_pic = get_embed_point_pic()
    img_bg_2[14:30, 102:118] = cv2.resize(point_pic, (16, 16))
    img_bg_2[14:30, 354:370] = cv2.resize(point_pic, (16, 16))

    cv2.imwrite('../wujing_bg_conf/wj_07_bg_1.png', img_bg_2)

    cv2.imshow(f'xxx', img_bg_2)
    cv2.waitKey()
    cv2.destroyAllWindows()


def create_wj_07_m_bg():

    img_bg=cv2.imread('../wujing_bg_conf/wj_07_m_blank.png')
    wj_chars=get_wj_chars_m_07(output_size=(108,72))
    img_bg[27:99,81:189]=wj_chars

    logo=get_wj_logo_07()
    logo=cv2.resize(logo,(44,44))
    img_bg[40:84,206:250]=logo


    # cv2.imwrite('wujing_bg_conf/wj_07_bg_m_0.png',img_bg)
    cv2.imshow(f'xxx',img_bg)
    cv2.waitKey()
    cv2.destroyAllWindows()

    img_bg_2 = img_bg.copy()
    point_pic = get_embed_point_pic()
    img_bg_2[22:38, 59:75] = cv2.resize(point_pic, (16, 16))
    img_bg_2[22:38, 411:427] = cv2.resize(point_pic, (16, 16))

    cv2.imwrite('../wujing_bg_conf/wj_07_bg_m_1.png', img_bg_2)

    cv2.imshow(f'xxx', img_bg_2)
    cv2.waitKey()
    cv2.destroyAllWindows()
# create_wujing_bg_1()


def create_wj_12_bg():

    img_bg=cv2.imread('../wujing_bg_conf/wj_12_blank.png')
    wj_chars=get_wj_chars_m_07(output_size=(92,82))
    img_bg[32:114,20:112]=wj_chars

    logo=get_wj_logo_12()
    # logo=cv2.resize(logo,(44,44))
    img_bg[54:90, 186:214]=logo


    # cv2.imwrite('wujing_bg_conf/wj_12_bg_0.png',img_bg)
    cv2.imshow(f'xxx',img_bg)
    cv2.waitKey()
    cv2.destroyAllWindows()

    img_bg_2 = img_bg.copy()
    point_pic = get_embed_point_pic()
    img_bg_2[15:31, 155:171] = cv2.resize(point_pic, (16, 16))
    img_bg_2[15:31, 367:383] = cv2.resize(point_pic, (16, 16))

    cv2.imwrite('../wujing_bg_conf/wj_12_bg_1.png', img_bg_2)

    cv2.imshow(f'xxx', img_bg_2)
    cv2.waitKey()
    cv2.destroyAllWindows()


def create_wj_12_m_bg():

    img_bg=cv2.imread('../wujing_bg_conf/wj_12_m_blank.png')
    wj_chars=get_wj_chars_m_07(output_size=(92,66))
    img_bg[32:98,108:200]=wj_chars

    logo=get_wj_logo_12()
    logo=cv2.resize(logo,(32,42))
    img_bg[44:86, 232:264]=logo


    # cv2.imwrite('wujing_bg_conf/wj_12_bg_m_0.png',img_bg)
    cv2.imshow(f'xxx',img_bg)
    cv2.waitKey()
    cv2.destroyAllWindows()

    img_bg_2=img_bg.copy()
    point_pic=get_embed_point_pic()
    img_bg_2[23:43,61:81]=cv2.resize(point_pic,(20,20))
    img_bg_2[23:43,400:420]=cv2.resize(point_pic,(20,20))

    cv2.imwrite('../wujing_bg_conf/wj_12_bg_m_1.png', img_bg_2)

    cv2.imshow(f'xxx', img_bg_2)
    cv2.waitKey()
    cv2.destroyAllWindows()


def get_wj_char():
    from  PIL import Image
    # img=Image.open(r'C:\Users\litianshui\Desktop\武警/CAFP_2012_type_vehicle_plate_simple_sample_figure_.png')
    # assert isinstance(img, Image.Image)
    # img.save('wujing_bg_conf/666.png',quality=95, subsampling=0, dpi=(300, 300), optimize=True)
    # img.show()
    # assert  isinstance(img,Image.Image)
    # img=img.convert(mode='RGB')
    # img_wj = np.array(img)
    # img_wj = cv2.cvtColor(img_wj, cv2.COLOR_RGB2BGR)


    # # img_wj = cv2.imdecode(np.fromfile(r'C:\Users\litianshui\Desktop\武警/CAFP_2012_type_vehicle_plate_simple_sample_figure_.png', dtype=np.uint8), -1)
    img_wj = cv2.imread('../wujing_bg_conf/CAFP_2012_type_vehicle_plate_simple_sample_figure_.png')
    # img_wj = cv2.cvtColor(img_wj, cv2.COLOR_BGRA2BGR)
    img_wj = img_wj[354:1366, 2010:3440]
    h,w,_=img_wj.shape
    resize_h=152
    resize_w=int(resize_h*w/h)
    # img_wj=cv2.resize(img_wj,(resize_w,resize_h))


    # img_wj1 = cv2.cvtColor(img_wj, cv2.COLOR_BGRA2RGB)
    # img_wj1=Image.fromarray(img_wj1)
    # cv2.imwrite('wujing_bg_conf/666.png',img_wj,[int(cv2.IMWRITE_JPEG_QUALITY), 100])
    cv2.imwrite('../wujing_bg_conf/666.png', img_wj)
    # img_wj1.show()

    img=Image.open('../wujing_bg_conf/666.png')
    assert isinstance(img, Image.Image)
    # img=img.resize((resize_w,resize_h))
    img=img.resize((90,82))
    img=img.convert(mode='RGB')
    img.show()
    img.save('wujing_bg_conf/666_1.png')
    #
    # cv2.imwrite('wujing_bg_conf/666.png',img_wj, [int(cv2.IMWRITE_JPEG_QUALITY), 90])
    # cv2.imwrite('wujing_bg_conf/666.png',img_wj, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
    # img_wj=img_wj[354:1366,2010:3440]
    cv2.namedWindow('win', cv2.WINDOW_NORMAL)
    cv2.imshow('win',img_wj)
    cv2.waitKey()
    cv2.destroyAllWindows()
    return None

def get_wj_logo_07():
    demo_wuj_plate_img_path = r'../wujing_bg_conf/警-旧-单行-正常比例.png'
    img = cv2.imdecode(np.fromfile(demo_wuj_plate_img_path, dtype=np.uint8), -1)

    # img=cv2.cvtColor(img,cv2.COLOR_BGRA2GRAY)
    img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
    img_copy = img.copy()
    logo = img_copy[20:60, 131:164]

    # logo=cv2.resize(logo,(44,44))
    # # cv2.namedWindow('win', cv2.WINDOW_NORMAL)
    # cv2.imshow('win', logo)
    # cv2.waitKey()
    # cv2.destroyAllWindows()
    return logo

def get_wj_logo_12():
    demo_wuj_plate_img_path = r'../wujing_bg_conf/wj_12_demo.png'
    img = cv2.imdecode(np.fromfile(demo_wuj_plate_img_path, dtype=np.uint8), -1)

    # img=cv2.cvtColor(img,cv2.COLOR_BGRA2GRAY)
    img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
    img_copy = img.copy()
    logo = img_copy[54:90, 186:214]

    # logo=cv2.resize(logo,(44,44))
    # # cv2.namedWindow('win', cv2.WINDOW_NORMAL)
    # cv2.imshow('win', logo)
    # cv2.waitKey()
    # cv2.destroyAllWindows()
    return logo


def get_wj_chars_m_07(output_size=(108,72)):
    """
    07版双层武警
    :param output_size:
    :return:
    """
    return get_wj_chars(output_size)

def get_wj_chars(output_size=(108,72)):
    demo_wuj_plate_img_path = r'../wujing_bg_conf/666.png'
    img=Image.open(demo_wuj_plate_img_path)
    assert isinstance(img, Image.Image)
    # img=img.convert('RGB')
    img=img.resize((output_size[0],output_size[1]))
    return cv2.cvtColor(np.array(img),cv2.COLOR_RGB2BGR)


def get_embed_point_pic():
    demo_wuj_plate_img_path = r'../wujing_bg_conf/wj_12_m_demo.png'
    img = cv2.imdecode(np.fromfile(demo_wuj_plate_img_path, dtype=np.uint8), -1)

    return img[23:43,400:420]

def create_judui_bg():

    img=cv2.imread('../wujing_bg_conf/white_jd_0.png')
    img=cv2.resize(img,(490,140))

    point_pic = get_embed_point_pic()
    img[10:26,112:128] = cv2.resize(point_pic, (16, 16))
    img[10:26, 362:378] = cv2.resize(point_pic, (16, 16))
    cv2.imwrite('../wujing_bg_conf/white_jd_2.png', img)

    cv2.imshow(f'xxx', img)
    cv2.waitKey()
    cv2.destroyAllWindows()

    img_1 = cv2.imread('../wujing_bg_conf/white_jd_1.png')
    img_1 = cv2.resize(img_1, (490, 140))

    point_pic = get_embed_point_pic()
    img_1[10:26, 112:128] = cv2.resize(point_pic, (16, 16))
    img_1[10:26, 362:378] = cv2.resize(point_pic, (16, 16))
    cv2.imwrite('../wujing_bg_conf/white_jd_3.png', img_1)

    cv2.imshow(f'xxx', img_1)
    cv2.waitKey()
    cv2.destroyAllWindows()

def create_judui_m_bg():

    img=cv2.imread('../wujing_bg_conf/white_jd_m_0.png')
    img=cv2.resize(img,(495,240))

    point_pic = get_embed_point_pic()
    img[12:28,100:116] = cv2.resize(point_pic, (16, 16))
    img[12:28, 395:411] = cv2.resize(point_pic, (16, 16))
    cv2.imwrite('../wujing_bg_conf/white_jd_m_1.png', img)

    cv2.imshow(f'xxx', img)
    cv2.waitKey()
    cv2.destroyAllWindows()



# create_wj_07_bg_2()
# get_wj_char()

# img=Image.open('wujing_bg_conf/wj_99_blank.png')
# assert  isinstance(img,Image.Image)
# img=img.resize((485,240))
# img=img.convert(mode='RGB')
# img.save('wujing_bg_conf/wj_12_m_blank.png')

# wj_logo_07()

# cv2.namedWindow('win', cv2.WINDOW_NORMAL)
# cv2.imshow('win', img)
# cv2.waitKey()
# cv2.destroyAllWindows()


# img=get_embed_point_pic()
#
# # cv2.namedWindow('win', cv2.WINDOW_NORMAL)
# cv2.imshow('win', img)
# cv2.waitKey()
# cv2.destroyAllWindows()


# create_wj_12_bg()
# create_wj_12_m_bg()

# create_wj_07_bg()
# create_wj_07_m_bg()

create_judui_bg()
# create_judui_m_bg()