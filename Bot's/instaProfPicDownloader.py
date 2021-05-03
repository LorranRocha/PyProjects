#pip3 install instaloader

import instaloader

ig = instaloader.Instaloader()
dp = input("Digite o usuario: ")
ig.download_profile(dp, profile_pic_only=True)

