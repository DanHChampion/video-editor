from skvideo.measure import ssim, niqe
import skvideo.io
import numpy as np


VIDEOS = ["sunflower", "dog", "beach"]

print("Colour Correction:")

for video in VIDEOS:
    print("Analysing "+video+"...")
    for i in range(3):
        disVideoPath = video+"_cc"+str(i+1)+".mp4"
        disVideo = skvideo.io.vread(disVideoPath, as_grey=True)
        niqe_scores = niqe(disVideo)
        print("NIQE:")
        print(np.average(niqe_scores))

print("====================================")
print("Colour Transfer:")
for video in VIDEOS:
    print("Analysing "+video+"...")
    refVideoPath = video+"_vid.mp4"
    refVideo = skvideo.io.vread(refVideoPath, as_grey=True)
    for i in range(3):
        disVideoPath = video+"_ct"+str(i+1)+".mp4"
        disVideo = skvideo.io.vread(disVideoPath, as_grey=True)
        niqe_scores = niqe(disVideo)
        print("NIQE:")
        print(np.average(niqe_scores))
        ssim_scores = ssim(refVideo,disVideo)
        print("SSIM:")
        print(np.average(ssim_scores))


print("====================================")
print("Denoise:")
for video in VIDEOS:
    print("Analysing "+video+"...")
    refVideoPath = video+"_vid.mp4"
    refVideo = skvideo.io.vread(refVideoPath, as_grey=True)
    for i in range(3):
        disVideoPath = video+"_dn"+str(i+1)+".mp4"
        disVideo = skvideo.io.vread(disVideoPath, as_grey=True)
        niqe_scores = niqe(disVideo)
        print("NIQE:")
        print(np.average(niqe_scores))
        ssim_scores = ssim(refVideo,disVideo)
        print("SSIM:")
        print(np.average(ssim_scores))
