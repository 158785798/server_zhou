import cv2 as cv
def image_blur(image_path: str):
    """
    图像卷积操作：设置卷积核大小，步距
    :param image_path:
    :return:
    """
    middle_path = './mv_copy1.png'
    img = cv.imread(image_path, cv.IMREAD_COLOR)
    # cv.imshow('input', img)
    # 模糊操作（类似卷积），第二个参数ksize是设置模糊内核大小
    middle_img = cv.GaussianBlur(img, (0, 0), 50)
    # cv.imshow('result', middle_img)
    cv.imwrite(middle_path, middle_img)

    cv.waitKey(0)
    cv.destroyAllWindows()


path = './mv_copy.png'
image_blur(path)