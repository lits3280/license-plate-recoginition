# coding=utf-8
"""
@Author:lts
@Time:2024/3/4 16:07
@description:
"""
import os, datetime, time
from typing import Union
import numpy as np
import cv2
import math, random
from PIL import Image, ImageDraw
import glob
from torchvision import transforms
from shapely.geometry import Polygon
import my_randomAffine

from data.config_gen import cfg
from gen_data import GenData


def draw_points(img, points_list: 'list'):
    new_img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

    for i, (x, y) in enumerate(points_list):
        # cv2.putText(new_img,str(i+1),(x,y), cv2.FONT_HERSHEY_SIMPLEX,0.75, (0, 0, 255), 2) #红色
        cv2.putText(new_img, f'A{i + 1}', (x + 20, y + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)  # 蓝色

    return Image.fromarray(cv2.cvtColor(new_img, cv2.COLOR_BGR2RGB))


def is_intersects(box1, box2):
    """计算区域是否有重叠
    """
    polygon1 = Polygon([(x, y) for x, y in box1])
    polygon2 = Polygon([(x, y) for x, y in box2])

    return polygon1.intersects(polygon2)


def random_paste_pic_to_background_pic(bg_img: Union[str, Image.Image], src_img: 'Image.Image', ratio=(0.1, 0.99), src_box=None, used_boxes: 'list' = None):
    """随机把图片贴到背景图中

    :param bg_img: 背景图路径，str或者Image.Image对象
    :param src_img: 资源图片
    :param ratio: 资源图片占背景图片大小区间
    :return: 返回结果：(新图片,src_img在新图片中左上角位置,src_img缩放倍数)
    """
    if isinstance(bg_img, str):
        new_img = Image.open(bg_img)
    else:
        new_img = bg_img.copy()

    if new_img.mode != 'RGBA':
        new_img = new_img.convert('RGBA')

    assert isinstance(new_img, Image.Image)
    bg_w, bg_h = new_img.size
    src_w, src_h = src_img.size

    max_retry_num = 20
    loop_i = 0
    is_parse_success = False

    while loop_i < max_retry_num:
        loop_i += 1
        # print(f'    {loop_i}',datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])

        # 资源图片缩放比例
        src_scale = round(random.randint(int(ratio[0] * 100), int(ratio[1] * 100)) / 100 * min(bg_w / src_w, bg_h / src_h), 2)
        new_src_w = int(src_scale * src_w / 2) * 2
        new_src_h = int(src_scale * src_h / 2) * 2

        random_x = random.randint(0, bg_w - new_src_w)
        random_y = random.randint(0, bg_h - new_src_h)

        is_valid_box = True
        if used_boxes:
            real_top_points = [(random_x + math.ceil(src_scale * x[0]), random_y + math.ceil(src_scale * x[1])) for x in src_box]
            for box in used_boxes:
                # 检查区域是否重叠
                is_intersects_area = is_intersects(real_top_points, box)
                if is_intersects_area:
                    is_valid_box = False
                    break

        if is_valid_box:
            is_parse_success = True
            src_img = src_img.resize((new_src_w, new_src_h))

            # mask设置为src_img，以确保使用 src_img 图像的 alpha 通道作为 mask，以便保留其透明效果
            # new_img.paste(src_img, (random_x, random_y), src_img)
            if src_img.mode == 'RGBA':
                new_img.paste(src_img, (random_x, random_y), src_img)
            else:
                new_img.paste(src_img, (random_x, random_y))
            break

    if is_parse_success:
        return True, new_img, (random_x, random_y), src_scale
    else:
        return False, new_img, (0, 0), 1.0


def get_non_blank_vertices(img, angle=None):
    """获取轮廓的4个顶点

    :param img:
    :return:
    """
    if not isinstance(img, np.ndarray):
        img = np.array(img)

    gray = cv2.cvtColor(img, cv2.COLOR_RGBA2GRAY)

    # 使用阈值化将图像转换为二值图像
    _, edges = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY)

    # 查找轮廓
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 找到最大轮廓
    max_contour = max(contours, key=cv2.contourArea)

    # 近似轮廓
    epsilon = 0.04 * cv2.arcLength(max_contour, True)
    approx = cv2.approxPolyDP(max_contour, epsilon, True)

    # 返回近似轮廓的顶点
    _box_tops = [tuple(vertex[0]) for vertex in approx]
    if len(_box_tops) != 4:
        return None
    # box_tops需要转成顺时针
    box_tops = sort_four_points(_box_tops, angle=angle)

    return box_tops


def sort_four_points(points, clockwise=True, angle=None):
    # 计算四个点的质心
    centroid = np.mean(points, axis=0)
    ndarray_points = np.array(points)
    # 计算四个点相对于质心的角度
    angles = np.arctan2(ndarray_points[:, 1] - centroid[1], ndarray_points[:, 0] - centroid[0])
    # 按照角度进行排序
    sorted_indices = np.argsort(angles)
    if not clockwise:
        sorted_indices = sorted_indices[::-1]
    # sorted_points = points[sorted_indices]
    sorted_points = [points[x] for x in sorted_indices]

    first_point = calc_first_point(sorted_points, angle=angle)
    i = sorted_points.index(first_point)

    sorted_points = sorted_points[i:] + sorted_points[0:i]

    return sorted_points


def calc_first_point(sorted_points, angle=None):
    if angle is not None:
        # 把原始左上角做为第一个点，
        def point_distance(p1, p2):
            return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

        def compare_point(i, _points):

            x = _points[i]
            before_point = _points[i - 1]
            after_point = _points[(i + 1) % (len(_points))]
            d1 = point_distance(before_point, x)
            d2 = point_distance(x, after_point)
            return d1 < d2

        def calc_origin_left_top_point(p1, p2, _angle):
            """根据角度计算原始左上顶点

            :param p1:
            :param p2:
            :param _angle:
            :return:
            """
            _angle = _angle if _angle >= 0 else 360 + _angle
            x1, y1 = p1[0], p1[1]
            x2, y2 = p2[0], p2[1]
            if _angle <= 90:
                return p1 if y1 < y2 else p2
            elif _angle <= 180:
                return p1 if x1 > x2 else p2
            elif _angle <= 270:
                return p1 if y1 > y2 else p2
            else:
                return p1 if x1 < x2 else p2

        # 由于矩形是宽大于高，因此可以用下面方法取到原始的左上，右下顶点
        top_bottom_points = []
        for i, x in enumerate(sorted_points):
            if compare_point(i, sorted_points):
                top_bottom_points.append(x)

                top_bottom_points.append(sorted_points[(i + 2) % len(sorted_points)])
                break
        # top_bottom_points = [x for i, x in enumerate(sorted_points) if compare_point(i, sorted_points)]

        # 计算原始左上顶点
        first_point = calc_origin_left_top_point(top_bottom_points[0], top_bottom_points[1], angle)

    else:
        centroid = np.mean(sorted_points, axis=0)
        # 取中心点上面x最小的作为第一个点
        upper_points = [x for x in sorted_points if x[1] < centroid[1]]
        upper_points.sort(key=lambda x: x[0])
        first_point = upper_points[0]
    return first_point


def transform_big_img_rgba(img):
    assert isinstance(img, Image.Image)
    if img.mode != 'RGBA':
        img = img.convert('RGBA')
    # math.ceil向上取整
    expand_border_len = math.ceil(math.sqrt(img.size[0] ** 2 + img.size[1] ** 2) + min(img.size) * 0.2)
    expand_border_len = expand_border_len if expand_border_len % 2 == 0 else expand_border_len + 1

    # 透明背景图片
    img_new = Image.new('RGBA', (expand_border_len, expand_border_len), color=0)
    box = (int((expand_border_len - img.size[0]) / 2), int((expand_border_len - img.size[1]) / 2))
    img_new.paste(img, box=box)
    return img_new


def draw_outline(img, four_points_list: 'list'):
    new_img = cv2.cvtColor(np.array(img), cv2.COLOR_RGBA2BGR)

    for four_points in four_points_list:

        # # print(points)
        # points=[[ 63 ,27],[93, 33],[18,84],[ 4 ,69]]
        _box = np.array(four_points).astype(np.int32).reshape(-1, 2)
        # print(_box)
        cv2.polylines(new_img, [_box], isClosed=True, color=(0, 0, 255), thickness=2)

        for i, (x, y) in enumerate(four_points):
            # cv2.putText(new_img,str(i+1),(x,y), cv2.FONT_HERSHEY_SIMPLEX,0.75, (0, 0, 255), 2) #红色
            cv2.putText(new_img, str(i + 1), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 0, 0), 2)  # 蓝色

    # cv2.imshow('xx',img)
    # cv2.waitKey()
    # cv2.imwrite(f'pic_affine_outline/{os.path.basename(img_path)}', img)

    return Image.fromarray(cv2.cvtColor(new_img, cv2.COLOR_BGR2RGB))


class RandomAffineParsePic:

    def __init__(self) -> None:
        self._random_affines = [self._create_random_affine(degrees=(0, 360), shear=15), self._create_random_affine(degrees=(-45, 45), shear=None)]
        self._random_perspective = transforms.RandomPerspective(distortion_scale=0.5, p=0.5)

    def transform(self, img, affines_p_15_0=[0.5, 0.5]):
        # transforms.Compose([transform_affine, transform_perspective])
        transf_list = []
        transf_list.append(np.random.choice(self._random_affines, p=affines_p_15_0))
        transf_list.append(self._random_perspective)

        angle = None
        for t in transf_list:
            img = t(img)
            if isinstance(t, my_randomAffine.RandomAffine):
                angle = t.ret[0]

        return img, angle

    def _create_random_affine(self, degrees=(0, 360), shear=15):
        # degrees = (0, 360)
        # shear = 15  # 可从中选择的度数范围。放射变换的角度
        # translate = (0, 0.2)
        translate = None
        # scale=(1, 1) #比例因子区间，例如（a，b），则从范围a<=比例<=b中随机采样比例。默认情况下，将保留原始比例。
        scale = None
        # fillcolor = (0, 0, 255)
        # fill = (0, 125, 0)
        fill = None
        # transform_affine = transforms.RandomAffine(degrees=degrees, translate=None, scale=None, shear=shear, fill=fill, interpolation=transforms.InterpolationMode.BILINEAR)
        transform_affine = my_randomAffine.RandomAffine(degrees=degrees, translate=None, scale=None, shear=shear, fill=fill, interpolation=transforms.InterpolationMode.BILINEAR)
        return transform_affine

    def __call__(self, bg_img, embed_img_list, ratio=(0.1, 0.99), affines_p_15_0=[0.5, 0.5]):
        """
        embed_img_list:格式[(level_type,plat_no,img)] level_type:0-1层，1-双层
        """

        succ_embed_img_info = []
        used_boxes = []
        new_img = bg_img
        for color, plateno, embed_img in embed_img_list:
            # 添加透明背景，以方便做仿射变换，比如图片旋转时保证图片的完整性
            big_embed_img = transform_big_img_rgba(embed_img)

            loop_counter = 0
            while loop_counter < len(embed_img_list) * 5:
                loop_counter += 1
                # print(f'---> {loop_counter}/{len(embed_img_list)}', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])
                src_img, _angle = self.transform(big_embed_img, affines_p_15_0=affines_p_15_0)
                # 使用双线性插值对图像进行抗锯齿处理
                src_img = src_img.resize((src_img.width, src_img.height), Image.BILINEAR)
                top_points_4 = get_non_blank_vertices(src_img, _angle)
                if top_points_4 is None:
                    continue

                x_list = [x[0] for x in top_points_4]
                y_list = [x[1] for x in top_points_4]
                min_box = (min(x_list), min(y_list), max(x_list), max(y_list))
                src_img = src_img.crop(min_box)
                top_points_4 = [(x[0] - min_box[0], x[1] - min_box[1]) for x in top_points_4]
                # draw_outline(src_img,top_points_4).show('xx-crop')

                # 生成的图片贴到背景图中
                is_parse_success, new_img, left_top, img_scale = random_paste_pic_to_background_pic(bg_img=new_img, src_img=src_img, ratio=ratio, src_box=top_points_4, used_boxes=used_boxes)
                if is_parse_success:
                    real_top_points = [(left_top[0] + math.ceil(img_scale * x[0]), left_top[1] + math.ceil(img_scale * x[1])) for x in top_points_4]
                    used_boxes.append(real_top_points)
                    succ_embed_img_info.append((color, plateno, real_top_points, _angle))
                    break

            # draw_outline(new_img, real_top_points).show('xx-crop')
            # 返回新生成的图片，以及src_img在新图片的位置（4个点的坐标）
            # new_img Image.Image实例

        return new_img, succ_embed_img_info


def create_labelme_json(img: 'Image.Image', save_img_path, label_points):
    import labelme, json
    # imageData = labelme.utils.img_arr_to_b64(np.array(img)).decode('utf-8')

    # imageData = labelme.utils.img_arr_to_b64(np.array(img))
    imageData = None

    shapes = []
    for label, points in label_points:
        shapes.append({"label": str(label),
                       "points": [[x, y] for x, y in points],
                       "group_id": None,
                       "description": "",
                       "shape_type": "polygon",
                       "flags": {},
                       "mask": None
                       })

    lab_json = {"version": "5.4.0.post1",
                "flags": {},
                "shapes": shapes,
                "imagePath": save_img_path,
                "imageData": imageData,
                "imageWidth": img.size[0],
                "imageHeight": img.size[1],
                }
    return json.dumps(lab_json, ensure_ascii=False, indent=2)


def get_labtype_by_color(p_color):
    """
    双层车牌color：
        黄: yellow+m
        白  ：white+jdm,white+wjm
        farm:farm+m
    """
    multi_level_color_set = {'yellow+m', 'white+jdm', 'white+wjm', 'farm+m'}
    if p_color is not None and p_color in multi_level_color_set:
        # 双层
        return "1"
    return "0"


def test():
    output_dir = 'random_plate_train-white-jundui-7'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        os.makedirs(f'{output_dir}-outline')

    # img_path = 'F:/t1.jpg'
    # img_path = 'F:/home/hanxiao/data/lp-data/train-blue/20240301-blue-云RNT7RA-1709288627752218.jpg'

    background_pic = Image.open('f:/t1_add_alpha.png')
    # background_pic = Image.open('f:/000000043435.jpg')

    import glob
    # img_paths = glob.glob('F:/home/hanxiao/data/lp-data/train-green-3/*')
    img_paths = glob.glob('F:/home/hanxiao/data/lp-data/train-white-jundui-1/*')

    randomAffineParsePic = RandomAffineParsePic()

    for i in range(100):
        # img_path = 'F:/home/hanxiao/data/lp-data/train-green-1/20240305-green+b-黑U86Q85D-1709623876506096.jpg'
        img_path = random.choice(img_paths)
        plate_no = os.path.basename(img_path).split('-')[2]

        img = Image.open(img_path)
        new_img, box_tops = randomAffineParsePic(bg_img=background_pic, src_img=img, affines_p_15_0=[0, 1.0])

        # new_img.show()
        plate_points_str = '_'.join([f'{x[0]}x{x[1]}' for x in box_tops])
        new_img.save(f'{output_dir}/random_affine_{i}_{plate_no}_{plate_points_str}.png')

        # background_pic=new_img

        new_img_outline = draw_outline(np.array(new_img), [box_tops])
        new_img_outline.save(f'{output_dir}-outline/random_affine_{i}_{plate_no}_{plate_points_str}.png')
        # new_img_outline.show()
        # new_img.show()


def recreate_dirs(dir_path):
    if not dir_path or dir_path == '/':
        return
    # import shutil
    # if os.path.exists(dir_path):
    #     shutil.rmtree(dir_path)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)


def test_gen_plate_embed_bg(bg_img_path, output_dir, gen_num=100, p=[0., 0., 0., 0., 1., 0., 0.], pic_embed_plate_num_max=5, affines_p_15_0=[0.5, 0.5],
                            is_save_plate_no=True, is_save_plate_embed=True, is_save_plate_embed_show_boxes=True, is_save_labelme_json=True):
    SMU_PATH = 'data/sum_imgs'
    BG_PATH = 'data/env_imgs'
    # cfg.p = [0., 0., 0., 0., 1., 0., 0.]  # [black_plate,blue_plate,yellow_plate,green_plate,white_plate,farm_plate,airport]
    # cfg.p = [0.15,0.15,0.15,0.15,0.15,0.15,0.1] #[black_plate,blue_plate,yellow_plate,green_plate,white_plate,farm_plate,airport]
    cfg.p = p
    gen = GenData(sum_path=SMU_PATH, bg_path=BG_PATH, cfg=cfg)

    bg_imgs = glob.glob(f'{bg_img_path}/*')

    output_dir_plate_no = f'{output_dir}_plate_no'
    output_dir_plate_embed = f'{output_dir}_plate_embed'
    output_dir_plate_embed_show_boxes = f'{output_dir}_plate_embed_show_boxes'
    if is_save_plate_no:
        recreate_dirs(output_dir_plate_no)
    if is_save_plate_embed:
        recreate_dirs(output_dir_plate_embed)
    if is_save_plate_embed_show_boxes:
        recreate_dirs(output_dir_plate_embed_show_boxes)

    randomAffineParsePic = RandomAffineParsePic()

    import time
    time1 = time.time()
    for i in range(gen_num):
        embed_plate_num = random.randint(1, pic_embed_plate_num_max)

        plate_no_list = []
        for k in range(embed_plate_num):
            img, lab, color = gen(embed=False, p=0.98)
            print('{:15s}{:12s}{:10s}'.format(f"{i + 1}/{gen_num}({k + 1}/{embed_plate_num})", color, lab))

            plate_img = Image.fromarray(img)
            # plate_img.show()
            if is_save_plate_no:
                # 保存车牌
                lab_type = get_labtype_by_color(color)
                lab_type = '双' if lab_type == '1' else '单'
                plate_img.save(f'{output_dir_plate_no}/{i + 1}_{lab}_{color}_{lab_type}.jpg')

            plate_no_list.append([plate_img, lab, color])

        bg_pic = Image.open(random.choice(bg_imgs))
        # (color, plat_no, img)
        embed_img_list = [(color, _plate_no, _img) for _img, _plate_no, color in plate_no_list]
        new_img, embed_img_infos = randomAffineParsePic(bg_img=bg_pic, embed_img_list=embed_img_list, ratio=(0.2, 0.99), affines_p_15_0=affines_p_15_0)

        assert isinstance(new_img, Image.Image)

        label_points = [(get_labtype_by_color(p_color), points) for p_color, plate_no, points, angle in embed_img_infos]

        filename = f'{i + 1}'

        # for obj in embed_img_infos:
        #     print(f'{filename}-->{obj}')

        if new_img.mode != 'RGB':
            new_img = new_img.convert('RGB')

        # plate_points_str = '_'.join([f'{x[0]}x{x[1]}' for x in box_tops])
        # filename = f'{i + 1}_{lab}_{plate_points_str}'
        if is_save_plate_embed:
            # 保存车牌嵌入背景图片
            new_img.save(f'{output_dir_plate_embed}/{filename}.jpg')

        if is_save_labelme_json:
            # 生成labelme格式的json文件
            label_json_str = create_labelme_json(new_img, f'{filename}.jpg', label_points)

            with open(file=f'{output_dir_plate_embed}/{filename}.json', mode='w', encoding='utf-8') as f:
                f.write(label_json_str)

        if is_save_plate_embed_show_boxes:
            # 画框
            boxes = [points for label, plate_no, points, angle in embed_img_infos]
            new_img_outline = draw_outline(np.array(new_img), boxes)
            new_img_outline.save(f'{output_dir_plate_embed_show_boxes}/{filename}.jpg')

        # cv2.imwrite(filename, cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        # cv2.imencode(".png", cv2.cvtColor(img, cv2.COLOR_BGR2RGBA))[1].tofile(filename)
    print('viz time: {:.3f}s'.format(time.time() - time1))


def test_create_pic_and_labelme_json():
    bg_img = Image.open('D:/临时文件夹/val2017/000000000785.jpg')
    img_paths = glob.glob('F:/github_code/license-plate-recoginition/random_plat_white_军牌_字母_3_plate_no/*')
    embed_img_num = 5

    output_dir = 'labelme_data'
    # embed_img_list = [(os.path.basename(x).split('.')[0], Image.open(random.choice(img_paths))) for x in range(embed_img_num)]
    random_choice_imgs = [random.choice(img_paths) for x in range(embed_img_num)]
    src_img_list = [('0', os.path.basename(x).split('.')[0], Image.open(x)) for x in random_choice_imgs]
    randomAffineParsePic = RandomAffineParsePic()
    new_img, embed_img_infos = randomAffineParsePic(bg_img, src_img_list, ratio=(0.1, 0.99))
    assert isinstance(new_img, Image.Image)

    label_points = [(label, points) for label, plate_no, points in embed_img_infos]

    save_new_img_path = f'{output_dir}/1.png'
    new_img.save(save_new_img_path)
    label_json_str = create_labelme_json(new_img, "1.png", label_points)
    with open(file=f'{output_dir}/1.json', mode='w') as f:
        f.write(label_json_str)

    print(embed_img_infos)
    new_img.show()


def test_main_v1():
    # p = [0., 0., 0., 0., 1., 0., 0.]  # [black_plate,blue_plate,yellow_plate,green_plate,white_plate,farm_plate,airport]

    params_list = [
        # ----------------白色车牌
        # (1000,'F:/tmp/plate/random_plate_white_军牌_单层_字母_1(正常)',[0., 0., 0., 0., 1., 0., 0.],[0.,1.]),
        # (1000,'F:/tmp/plate/random_plate_white_军牌_单层_字母_1',[0., 0., 0., 0., 1., 0., 0.],[1.,0.]),

        # (1000,'F:/tmp/plate/random_plate_white_军牌_单层_汉字_1(正常)',[0., 0., 0., 0., 1., 0., 0.],[0.,1.]),
        # (1000,'F:/tmp/plate/random_plate_white_军牌_单层_汉字_1',[0., 0., 0., 0., 1., 0., 0.],[1.,0.]),

        # (1000,'F:/tmp/plate/random_plate_white_军牌_双层_字母_1(正常)',[0., 0., 0., 0., 1., 0., 0.],[0.,1.]),
        # (1000,'F:/tmp/plate/random_plate_white_军牌_双层_字母_1',[0., 0., 0., 0., 1., 0., 0.],[1.,0.]),

        # (1000, 'F:/tmp/plate/random_plate_white_军牌_双层_汉字_1(正常)', [0., 0., 0., 0., 1., 0., 0.], [0., 1.]),
        # (1000, 'F:/tmp/plate/random_plate_white_军牌_双层_汉字_2', [0., 0., 0., 0., 1., 0., 0.], [1., 0.]),
    ]

    bg_img_path = 'D:/临时文件夹/val2017'

    for gen_num, output_dir, p, affines_p_15_0 in params_list:
        print(gen_num, output_dir, p, affines_p_15_0)
        test_gen_plate_embed_bg(bg_img_path=bg_img_path, output_dir=output_dir, gen_num=gen_num, p=p, pic_embed_plate_num_max=4, affines_p_15_0=affines_p_15_0)


from enum import Enum


class ArgsPlateType(Enum):
    blue = '蓝牌', None
    black = '黑牌', None
    yellow_single = '黄牌_单层', [1.0, 0.]  # [SINGLE, MULTI]
    yellow_multi = '黄牌_双层', [0., 1.]  # [SINGLE, MULTI]
    green = '绿牌', None
    farm = '农用牌', None
    white_jingcha = '白_警察', [0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0.]  # [COMMON,JINGCHA,JUNDUI,JUNDUI_M,WUJIN,WUJIN_M,YINGJI]
    white_jundui = '白_军牌_单层_字母', [0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0.]
    white_jundui_m = '白_军牌_双层_字母', [0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0.]
    white_wujing = '白_武警_单层', [0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0.]
    white_wujing_m = '白_武警_双层', [0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0.]
    white_yingji = '白_应急', [0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0.]
    white_wj_07 = '白_武警07版_单层', [0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0.]
    white_wj_07_m = '白_武警07版_双层', [0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0.]
    white_wj_12 = '白_武警12版_单层', [0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0.]
    white_wj_12_m = '白_武警12版_双层', [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1.]
    airport = '空军', None


def reset_cfg(plate_type: 'ArgsPlateType'):
    sub_types_p = plate_type.value[1]
    global_p = [0., 0., 0., 1, 0., 0., 0.]  # [black_plate,blue_plate,yellow_plate,green_plate,white_plate,farm_plate,airport]
    if plate_type.name.startswith('yellow_'):
        cfg.yellow_plate.p = sub_types_p
        global_p = [0., 0., 1., 0., 0., 0., 0.]
    elif plate_type.name.startswith('white_'):
        cfg.white_plate.p = sub_types_p
        global_p = [0., 0., 0., 0., 1., 0., 0.]
    elif plate_type == ArgsPlateType.black:
        global_p = [1., 0., 0., 0., 0., 0., 0.]
    elif plate_type == ArgsPlateType.blue:
        global_p = [0., 1., 0., 0., 0., 0., 0.]
    elif plate_type == ArgsPlateType.green:
        global_p = [0., 0., 0., 1., 0., 0., 0.]
    elif plate_type == ArgsPlateType.farm:
        global_p = [0., 0., 0., 0., 0., 1., 0.]
    elif plate_type == ArgsPlateType.airport:
        global_p = [0., 0., 0., 0., 0., 0., 1.]
    return global_p


def test_main():

    is_save_plate_no = False
    is_save_plate_embed_show_boxes = True
    is_save_labelme_json = True

    bg_img_path = 'D:/临时文件夹/val2017'
    output_dir_prefix = 'F:/tmp/plate/tmp20'

    # bg_img_path = '/data/车牌识别/bg_images'
    # output_dir_prefix = '/data/车牌识别/自动生成的车牌'

    for plate_type in ArgsPlateType:

        is_skip = plate_type not in {ArgsPlateType.white_wj_07, ArgsPlateType.white_wj_07_m, ArgsPlateType.white_wj_12, ArgsPlateType.white_wj_12_m}
        if is_skip:
            continue
        print(f'----------------------------->{plate_type}<-----------------------------------------(正常)')
        global_p = reset_cfg(plate_type)

        short_name = plate_type.name.split('_')[0]
        gen_num = 10
        output_dir = f'{output_dir_prefix}/random_plate_{short_name}_{plate_type.value[0]}_3(正常)'
        test_gen_plate_embed_bg(bg_img_path=bg_img_path, output_dir=output_dir, gen_num=gen_num, p=global_p, pic_embed_plate_num_max=4, affines_p_15_0=[0., 1.],
                                is_save_plate_no=is_save_plate_no, is_save_plate_embed_show_boxes=is_save_plate_embed_show_boxes, is_save_labelme_json=is_save_labelme_json)

        print(f'----------------------------->{plate_type}<-----------------------------------------(随机倾斜)')
        output_dir = f'{output_dir_prefix}/random_plate_{short_name}_{plate_type.value[0]}_3'
        test_gen_plate_embed_bg(bg_img_path=bg_img_path, output_dir=output_dir, gen_num=gen_num, p=global_p, pic_embed_plate_num_max=4, affines_p_15_0=[1., 0.],
                                is_save_plate_no=is_save_plate_no, is_save_plate_embed_show_boxes=is_save_plate_embed_show_boxes, is_save_labelme_json=is_save_labelme_json)


def resize(img: 'np.ndarray', im_resize_w=100):
    im_w, im_h = img.shape[1], img.shape[0]
    if im_resize_w == max(im_w,im_h):
        return img.copy()
    rate_h = 1.0 * im_resize_w / im_h
    rate_w = 1.0 * im_resize_w / im_w
    rate = min(rate_h, rate_w)

    output_w=int(rate * im_w)
    output_h=int(rate * im_h)

    return cv2.resize(img, (output_w, output_h))


def test_gen_plate_no(output_dir, gen_num=100, p=[0., 0., 0., 0., 1., 0., 0.], plate_flag=''):
    SMU_PATH = 'data/sum_imgs'
    BG_PATH = 'data/env_imgs'
    # cfg.p = [0., 0., 0., 0., 1., 0., 0.]  # [black_plate,blue_plate,yellow_plate,green_plate,white_plate,farm_plate,airport]
    # cfg.p = [0.15,0.15,0.15,0.15,0.15,0.15,0.1] #[black_plate,blue_plate,yellow_plate,green_plate,white_plate,farm_plate,airport]
    cfg.p = p
    gen = GenData(sum_path=SMU_PATH, bg_path=BG_PATH, cfg=cfg)

    recreate_dirs(output_dir)

    # parent_name = os.path.basename(output_dir)
    import time
    time1 = time.time()
    with open(f'{output_dir}/labels.txt', mode='w', encoding='utf-8')  as  f:
        for i in range(gen_num):
            # img, lab, color = gen(embed=False, p=0.98)
            img, lab, color = gen(embed=False, p=0.98)
            print('{:15s}{:12s}{:10s}'.format(f"{i + 1}/{gen_num}", color, lab))

            lab_type = get_labtype_by_color(color)
            lab_type = '双' if lab_type == '1' else '单'

            # img = resize(img, im_resize_w=100)
            plate_img = Image.fromarray(img)
            file_path = f'{output_dir}/{i + 1}_{lab}_{lab_type}.jpg'
            plate_img.save(file_path)

            f.write(f'{file_path} {lab} {plate_flag}\n')

    print('viz time: {:.3f}s'.format(time.time() - time1))


def test_gen_plate_no_wrap():
    output_dir_prefix = 'F:/tmp/plate/tmp'

    # output_dir_prefix = '/data/车牌识别/自动生成的车牌/纯车牌2'

    for plate_type in ArgsPlateType:

        # is_jundui = plate_type == ArgsPlateType.white_jundui_m or plate_type == ArgsPlateType.white_jundui
        # if not is_jundui:
        #     continue
        is_skip=False
        # is_wj = plate_type in {ArgsPlateType.white_wj_07, ArgsPlateType.white_wj_07_m, ArgsPlateType.white_wj_12, ArgsPlateType.white_wj_12_m}
        # is_skip = plate_type not in {ArgsPlateType.white_wujing,ArgsPlateType.white_wujing_m}
        # is_skip = plate_type not in {ArgsPlateType.white_jundui,ArgsPlateType.white_jundui_m}
        # is_skip = plate_type not in {ArgsPlateType.white_wujing,ArgsPlateType.white_wujing_m}
        # is_skip = plate_type in {ArgsPlateType.blue,ArgsPlateType.black,ArgsPlateType.yellow_single,ArgsPlateType.yellow_multi,ArgsPlateType.green,ArgsPlateType.farm}

        # is_skip = plate_type not in {ArgsPlateType.white_jundui,ArgsPlateType.white_jundui_m}
        # is_skip = plate_type not in {ArgsPlateType.white_wj_07, ArgsPlateType.white_wj_07_m, ArgsPlateType.white_wj_12, ArgsPlateType.white_wj_12_m}
        # is_skip = plate_type not in { ArgsPlateType.white_wj_07_m}

        if  is_skip:
            continue
        print(f'----------------------------->{plate_type.value[0]}<-----------------------------------------')
        global_p = reset_cfg(plate_type)

        gen_num = 10000
        if plate_type in {ArgsPlateType.white_jundui,ArgsPlateType.white_jundui_m}:
            gen_num=50000

        gen_num = 100

        short_name = plate_type.name.split('_')[0]

        # output_dir=f'{output_dir_prefix}/plate_no_{short_name}_{plate_type.value[0]}_天干地支_1'
        output_dir = f'{output_dir_prefix}/plate_no_{short_name}_{plate_type.value[0]}_01_加背景'
        test_gen_plate_no(output_dir=output_dir, gen_num=gen_num, p=global_p, plate_flag=plate_type.value[0])


test_gen_plate_no_wrap()
# test_main()
