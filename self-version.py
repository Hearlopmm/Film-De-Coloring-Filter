import cv2
# import matplotlib.pyplot as plt
from opencv_init import initial as init
import utilities as ut
from time import time
from pathlib import Path
# import matplotlib.pyplot

SAMPLE_NAME: str = "0.tiff"
start_t = time()
img = cv2.imread(f"test-photos/{SAMPLE_NAME}")
print(f"DONE. Elapsed time:{time() - start_t:.2f}s")
img = init.imgResize(img, 640*2)
ut.cv_show("raw", img)

save_dir = Path("doc")
save_path = str(save_dir / f"{SAMPLE_NAME}_raw.png")
cv2.imwrite(save_path, img)
print("DONE. Saved PNG COPY")


