# Kits Challenge

Kidney Segmentation in CT scans

## Dataset

1. KiTs Challenge ( MICCAI 2019 )

#### Characteristics of images

1. CT images ==> HU units

2. **Voxel Spacing varies among patients BUT slice WIDTH, HEIGHT are same** ( 512, 512 except for one case ( case_00160 | (512, 796)))

   

## Models

1. 3D Unet 

   * 3d 를 사용할거면 voxel spacing 을 맞춰주는 것이 좋을 것 같다? ( z 축으로 사이즈가 일정하지 않으니까 / 대신에 ㅑisotropic-Resampling 을 거쳐야 하는데 오래걸릴수도 있다.. )

   1. V-net ( Code available )

2. 2D Segmentation

   1. DeepLABv3+ ( code available )
   2. Unet++ ( code available )
   3. Attention Unet
   4. Modified-Unit [ https://arxiv.org/pdf/1802.10508.pdf ] -> 1등 ?



## Loss Functions

https://lars76.github.io/neural-networks/object-detection/losses-for-segmentation/



**Loss Function** 에 대해서 생각해 볼 필요가 있다.

Due to highly unbalanced dataset ( little Tumor, Kidney region + Too much Background Values )



## Rules

### Score

1. > Teams will be awarded a score for each of the 90 test cases equal to the (Kidney Sørensen–Dice + Tumor Sørensen–Dice)/2.

   **Label 1 의 Kidney 의 Sørensen–Dice score 와 Label 2 의 Tumor 의 Sørensen–Dice score 의 산술 평균 값을 보고하는 점수**로 사용한다.

##### Sorensen-Dice Score [ [wiki](https://en.wikipedia.org/wiki/S%C3%B8rensen%E2%80%93Dice_coefficient) ]



## Results



## Reference

​	[1] https://kits19.grand-challenge.org/rules/

