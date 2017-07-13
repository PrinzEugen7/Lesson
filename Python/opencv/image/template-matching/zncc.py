def ZNCC(image1, image2):
    vec1, vec2 = image1.reshape(-1), image2.reshape(-1)
    vec1, vec2 = vec1 - np.mean(vec1), vec2 - np.mean(vec2)
    numer = np.dot(vec1, vec2.T)
    denom = np.sqrt(np.sum(vec1 ** 2)) / np.sqrt(np.sum(vec2 ** 2))
    if denom == 0: return 0
    return numer / denom

def matching(image1, image2):
    image = image1.astype(np.double)
    pattern = image2.astype(np.double)
    height1, width1 = image.shape
    height2, width2 = pattern.shape
    output = np.zeros(image.shape)

    for i in range(height2 / 2, height1 - height2 / 2):
        for j in range(width2 / 2, width1 - width2 / 2):
            score = ZNCC(image[i-height2/2:i+height2/2+1, j-width2/2:j+width2/2+1], pattern)
            output[i,j] = score

    output /= np.max(output)
    maxidx = np.unravel_index(output.argmax(), output.shape)

    result = cv2.cvtColor(image1, cv2.COLOR_GRAY2RGB)
    cv2.rectangle(result, (maxidx[1] - width2 / 2, maxidx[0] - height2 / 2), (maxidx[1] + width2, maxidx[0] + height2), (0,255,0), 1)
    cv2.imshow("matching", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
