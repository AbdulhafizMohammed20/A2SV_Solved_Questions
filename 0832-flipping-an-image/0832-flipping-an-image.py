class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        
        for img in image :
            img.reverse()

            for indx in range(len(img)):
                img[indx] ^= 1
            
        return image
        
