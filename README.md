#AVA review downloader

**AVA: A Large-Scale Database for Aesthetic Visual Analysis**



**Bibtex:**
```
@article{,
title= {AVA: A Large-Scale Database for Aesthetic Visual Analysis},
keywords= {images, aesthetics, semantic, quality, AVA, DPChallenge},
journal= {},
author= {Naila Murray and Luca Marchesotti and Florent Perronnin},
year= {},
url= {},
license= {},
abstract= {Aesthetic Visual Analysis (AVA) contains over 250,000 images along with a rich variety of meta-data including a large number of aesthetic scores for each image, semantic labels for over 60 categories as well as labels related to photographic style for high-level image quality categorization.},
superseded= {},
terms= {}
}
```
```
@inproceedings{wang2018collaborative,
  title={Collaborative and Attentive Learning for Personalized Image Aesthetic Assessment.},
  author={Wang, Guolong and Yan, Junchi and Qin, Zheng},
  booktitle={IJCAI},
  pages={957--963},
  year={2018}
}
```

[http://www.lucamarchesotti.com/](http://www.lucamarchesotti.com/) contains the download link

AVA is a large-Scale database for aesthetic visual analysis containing 250000+ photos from dpchallenge.com.

However, the downloaded pakage only contains image list and annotations. You may need the script to download AVA images and corresponding reviews from website.

~~- Known Issue~~

~~With this script keep sending requests to dpchallenge.com, **the website would block your ip address for some time.**
I use a proxy to temporally avoid this block
Contact me if you have any good ideas. Thank you!
2017-1-17~~

~~## Usage~~

~~1. Download multiprocess.py getreviews.py xslt_lib.py to any directory you like.~~

~~2. Make sure you have downloaded AVA Database (zip, 4.2 MB) from the [site](http://www.lucamarchesotti.com/ava/download/start_download.html).~~

~~3. Unzip AVA_dataset.zip and place AVA.txt under the same directory as the script. Also create a folder 'image'~~

~~4. Run the script with command $python multiprocess.py *beginIndex endIndex*~~

~~5. **Tips:** Note that *beginIndex* and *endIndex* both range from 1 to 25553. Downloading all the images would **consume a lot of time**. It is recommended you download a small amount once a time.~~

Happy downloading~ :sunglasses:

Fing

2017-1-17
