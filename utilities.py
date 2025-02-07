import cv2
import seaborn as sns
import matplotlib.pyplot as plt


def cv_show(name, img):
    # 显示图像
    cv2.imshow(name, img)

    # 将 BGR 转换为 RGB
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # 提取 R, G, B 通道的像素值
    r, g, b = img_rgb[:, :, 0].flatten(), img_rgb[:, :, 1].flatten(), img_rgb[:, :, 2].flatten()

    # 绘制像素值的核密度估计图
    plt.figure(figsize=(8, 5))
    sns.kdeplot(r, color="red", fill=True, alpha=0.5, label="Red")
    sns.kdeplot(g, color="green", fill=True, alpha=0.5, label="Green")
    sns.kdeplot(b, color="blue", fill=True, alpha=0.5, label="Blue")

    # 图表设置
    plt.title(name)
    plt.xlabel("Pixel Value")
    plt.ylabel("Density")
    plt.legend()

    # 显示绘图结果
    plt.show()

    # 等待按键并销毁窗口
    cv2.waitKey(0)
    cv2.destroyAllWindows()
