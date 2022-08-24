from apps.blogs.models import Emojis
from utils.db_session import objects

em = [
  {
    "origin_uri": "guonianniu.png",
    "display_name": "[过年牛]",
    "hide": 1,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/5f926da8ff374efbb04f6e55b8bc36e4",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/5f926da8ff374efbb04f6e55b8bc36e4?x-expires=1974358800&x-signature=r4ptCbLYeqwiJ2O2Erk9CgX7bHk%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/5f926da8ff374efbb04f6e55b8bc36e4?x-expires=1974358800&x-signature=%2Bipy0nX6wbxSMPlJHSzgixdv8ZY%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/5f926da8ff374efbb04f6e55b8bc36e4?x-expires=1974358800&x-signature=WMCOZiJtg86wr1N1C29oXstgLCs%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "daikouzhao.png",
    "display_name": "[戴口罩]",
    "hide": 1,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/57dd26bb754d4643b9607623f49d826c",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/57dd26bb754d4643b9607623f49d826c?x-expires=1974358800&x-signature=zUeCqsF2c3KeZb2bTz%2FWPz2aHPE%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/57dd26bb754d4643b9607623f49d826c?x-expires=1974358800&x-signature=9ptpgbmygetobTcIoij3hEAv0Cs%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/57dd26bb754d4643b9607623f49d826c?x-expires=1974358800&x-signature=UjkEEKfnolyJYlVtLi2KTw%2BrJmo%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "qinxishou.png",
    "display_name": "[勤洗手]",
    "hide": 1,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/3fee371f76fa44289393972c198511a9",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/3fee371f76fa44289393972c198511a9?x-expires=1974358800&x-signature=qxy9gYe0SdTCQ3Rsbe64K8jyiFM%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/3fee371f76fa44289393972c198511a9?x-expires=1974358800&x-signature=Vzv0IV17iLufpzeN7FsH7AdoYf0%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/3fee371f76fa44289393972c198511a9?x-expires=1974358800&x-signature=6uYhNb2P87Bme9QSjl69pSBUMsM%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "buxinyaoyan.png",
    "display_name": "[不信谣言]",
    "hide": 1,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/057741569ba047d7a67e5d72d7c07d9c",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/057741569ba047d7a67e5d72d7c07d9c?x-expires=1974358800&x-signature=w0FxHXFpaWucE%2FYIqY0tCfuMJ1U%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/057741569ba047d7a67e5d72d7c07d9c?x-expires=1974358800&x-signature=7tPt01fWpmdoLHRscnP74mRjd1k%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/057741569ba047d7a67e5d72d7c07d9c?x-expires=1974358800&x-signature=BwJvQVaZH8UUnpanLonYA2JUwdU%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "weixiao.png",
    "display_name": "[微笑]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/77a8bd2071b34bb789231d56bd5d254d",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/77a8bd2071b34bb789231d56bd5d254d?x-expires=1974358800&x-signature=04c2WL14ejkXfZBu8MT2rLhcj%2Bg%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/77a8bd2071b34bb789231d56bd5d254d?x-expires=1974358800&x-signature=5rksxv8140HLx4EefDqXmm8jeao%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/77a8bd2071b34bb789231d56bd5d254d?x-expires=1974358800&x-signature=nyYjxircwpjS0DtI6eVL93%2FU3%2Fg%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "aimu.png",
    "display_name": "[色]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/74f4c1582ad94e7d953cc478a82ecb7b",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/74f4c1582ad94e7d953cc478a82ecb7b?x-expires=1974358800&x-signature=O%2BVNhBLhbtcTPDk5Rj8%2BNcZd51Q%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/74f4c1582ad94e7d953cc478a82ecb7b?x-expires=1974358800&x-signature=hS5r3DpCMQYlX21YJbTAIaUWs7o%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/74f4c1582ad94e7d953cc478a82ecb7b?x-expires=1974358800&x-signature=hKkceWhfuGNOuWvZWdUKQDmvGJE%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "aimu.png",
    "display_name": "[爱慕]",
    "hide": 1,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/74f4c1582ad94e7d953cc478a82ecb7b",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/74f4c1582ad94e7d953cc478a82ecb7b?x-expires=1974358800&x-signature=O%2BVNhBLhbtcTPDk5Rj8%2BNcZd51Q%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/74f4c1582ad94e7d953cc478a82ecb7b?x-expires=1974358800&x-signature=hS5r3DpCMQYlX21YJbTAIaUWs7o%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/74f4c1582ad94e7d953cc478a82ecb7b?x-expires=1974358800&x-signature=hKkceWhfuGNOuWvZWdUKQDmvGJE%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "liangdai.png",
    "display_name": "[发呆]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/eab7a364655b469aa6791bb557601733",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/eab7a364655b469aa6791bb557601733?x-expires=1974358800&x-signature=Z9Qyiit5mqNcek7%2FajL%2FF8RVZ7s%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/eab7a364655b469aa6791bb557601733?x-expires=1974358800&x-signature=EBUWebRQCyWueyUr740kkMx9MMg%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/eab7a364655b469aa6791bb557601733?x-expires=1974358800&x-signature=oVy9POZxaMKlWufvNXJOhmTnT6Y%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "liangdai.png",
    "display_name": "[惊呆]",
    "hide": 1,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/eab7a364655b469aa6791bb557601733",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/eab7a364655b469aa6791bb557601733?x-expires=1974358800&x-signature=Z9Qyiit5mqNcek7%2FajL%2FF8RVZ7s%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/eab7a364655b469aa6791bb557601733?x-expires=1974358800&x-signature=EBUWebRQCyWueyUr740kkMx9MMg%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/eab7a364655b469aa6791bb557601733?x-expires=1974358800&x-signature=oVy9POZxaMKlWufvNXJOhmTnT6Y%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "kuye.png",
    "display_name": "[酷拽]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/fe1c3b513a434fb09148e7134b9e52c8",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/fe1c3b513a434fb09148e7134b9e52c8?x-expires=1974358800&x-signature=eFcztM4%2B0M%2BSpT0Tsj8p1HsVQNU%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/fe1c3b513a434fb09148e7134b9e52c8?x-expires=1974358800&x-signature=e7UcIjlRFnC6KZfTOcCiZCB3c28%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/fe1c3b513a434fb09148e7134b9e52c8?x-expires=1974358800&x-signature=BLKyam8pb4UZiYZxEJXLgT5EK1Q%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "koubi.png",
    "display_name": "[抠鼻]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/84232a63b1ba4af2b2250940deed4dd2",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/84232a63b1ba4af2b2250940deed4dd2?x-expires=1974358800&x-signature=BW%2FZEZ9C%2BXSsFTOqTNpEzBVTiM4%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/84232a63b1ba4af2b2250940deed4dd2?x-expires=1974358800&x-signature=K%2BpAJofXecNSqOQI8qBLgzu1xeY%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/84232a63b1ba4af2b2250940deed4dd2?x-expires=1974358800&x-signature=xkRot3ZLxS7IidU3000ceJeVDlw%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "liulei.png",
    "display_name": "[流泪]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/6894074aef1a441b90e8d907f72c1674",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/6894074aef1a441b90e8d907f72c1674?x-expires=1974358800&x-signature=VVaRvXyTPPz98xNNdI74LP3qK5g%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/6894074aef1a441b90e8d907f72c1674?x-expires=1974358800&x-signature=SHS1JceJmIX2JIyj6ra7TJS4vY8%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/6894074aef1a441b90e8d907f72c1674?x-expires=1974358800&x-signature=NoWpuaiwrY7%2BxDyOCEaNB8elnhY%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "wulian.png",
    "display_name": "[捂脸]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/5e76a1b172454807ab4da4fab9e43ac3",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/5e76a1b172454807ab4da4fab9e43ac3?x-expires=1974358800&x-signature=S5jb4uB49X8rUtruim6wTV%2BLESo%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/5e76a1b172454807ab4da4fab9e43ac3?x-expires=1974358800&x-signature=pjkIH0XnV8FghkR214TbfVWsNFA%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/5e76a1b172454807ab4da4fab9e43ac3?x-expires=1974358800&x-signature=mNMg22%2Fb%2Fl%2BncnCyBS5dv4TSzSw%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "fanu.png",
    "display_name": "[发怒]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/7433429016ed46fdb5f831af96e9749d",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/7433429016ed46fdb5f831af96e9749d?x-expires=1974358800&x-signature=fAaXCb6o%2Fgtz6VNYggW518EOXyQ%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/7433429016ed46fdb5f831af96e9749d?x-expires=1974358800&x-signature=6fK6yFXtNjtpi9LJTG6uLIiUwfU%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/7433429016ed46fdb5f831af96e9749d?x-expires=1974358800&x-signature=CFsrHpIzWcS6BD0cWksBt5bQuOU%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "ziya.png",
    "display_name": "[呲牙]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/a1a7085f4a31405c871221bc1c84333a",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/a1a7085f4a31405c871221bc1c84333a?x-expires=1974358800&x-signature=8keq9Nc4J3M1jG8m%2BG2LiI3D1fc%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/a1a7085f4a31405c871221bc1c84333a?x-expires=1974358800&x-signature=WiS5aKrrP55Srx%2Bdj1AanTPQCsE%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/a1a7085f4a31405c871221bc1c84333a?x-expires=1974358800&x-signature=lfevyv4Xdw4HGLQ7UAYv9lmQlb0%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "yiqijiayou.png",
    "display_name": "[一起加油]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/c801f92db6244d6ba194cb332ab4125c",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/c801f92db6244d6ba194cb332ab4125c?x-expires=1974358800&x-signature=GGxjEBSYMOuAp2XezdUQHIQjhqo%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/c801f92db6244d6ba194cb332ab4125c?x-expires=1974358800&x-signature=bAPOMvckWM5ThedPV87g8W2ODIg%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/c801f92db6244d6ba194cb332ab4125c?x-expires=1974358800&x-signature=8Pn6t4As4rT2TZNqCrXAM24Mwfw%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "hanshui.png",
    "display_name": "[睡]",
    "hide": 1,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/f33757843fbc4f7b839d1bf846956b8d",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/f33757843fbc4f7b839d1bf846956b8d?x-expires=1974358800&x-signature=18GgUpIbPJDh0LqdglN9FXigcD0%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/f33757843fbc4f7b839d1bf846956b8d?x-expires=1974358800&x-signature=sSmeaW7q8bqX%2Bcbmh%2FBknDm5Sn4%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/f33757843fbc4f7b839d1bf846956b8d?x-expires=1974358800&x-signature=wWnpmea8GgrWR6%2FOwFG42cwctMo%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "hanshui.png",
    "display_name": "[鼾睡]",
    "hide": 1,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/f33757843fbc4f7b839d1bf846956b8d",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/f33757843fbc4f7b839d1bf846956b8d?x-expires=1974358800&x-signature=18GgUpIbPJDh0LqdglN9FXigcD0%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/f33757843fbc4f7b839d1bf846956b8d?x-expires=1974358800&x-signature=sSmeaW7q8bqX%2Bcbmh%2FBknDm5Sn4%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/f33757843fbc4f7b839d1bf846956b8d?x-expires=1974358800&x-signature=wWnpmea8GgrWR6%2FOwFG42cwctMo%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "haixiu.png",
    "display_name": "[害羞]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/4ffa8764af0747209b60c75bc9f874d5",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/4ffa8764af0747209b60c75bc9f874d5?x-expires=1974358800&x-signature=2VGV1EnvKM5jYWvd8QJdFuaLGL8%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/4ffa8764af0747209b60c75bc9f874d5?x-expires=1974358800&x-signature=bFjl%2B0SjzJaERqVmGbrudcFUVpc%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/4ffa8764af0747209b60c75bc9f874d5?x-expires=1974358800&x-signature=OpMKLJu3jKq9deJtIzHmXiB1plE%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "keai.png",
    "display_name": "[调皮]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/26b6203d04d24b3a891b1adca61ab7c8",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/26b6203d04d24b3a891b1adca61ab7c8?x-expires=1974358800&x-signature=jBlAC9ynbSM%2FSQbPdDkFcZyIIYk%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/26b6203d04d24b3a891b1adca61ab7c8?x-expires=1974358800&x-signature=XikZrLw269wBzgwFgUTgVSu0kl4%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/26b6203d04d24b3a891b1adca61ab7c8?x-expires=1974358800&x-signature=%2FE3MqwTTAvqxicCxIGujeuxWksI%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "keai.png",
    "display_name": "[可爱]",
    "hide": 1,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/26b6203d04d24b3a891b1adca61ab7c8",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/26b6203d04d24b3a891b1adca61ab7c8?x-expires=1974358800&x-signature=jBlAC9ynbSM%2FSQbPdDkFcZyIIYk%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/26b6203d04d24b3a891b1adca61ab7c8?x-expires=1974358800&x-signature=XikZrLw269wBzgwFgUTgVSu0kl4%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/26b6203d04d24b3a891b1adca61ab7c8?x-expires=1974358800&x-signature=%2FE3MqwTTAvqxicCxIGujeuxWksI%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "yun.png",
    "display_name": "[晕]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/0a36090e64f74fee84fe40e531d66f99",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/0a36090e64f74fee84fe40e531d66f99?x-expires=1974358800&x-signature=b9PIXAmx4r%2B7MW61SFkvQSVhI7k%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/0a36090e64f74fee84fe40e531d66f99?x-expires=1974358800&x-signature=DguaE5xmD8AXPr8c01971oNpYmU%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/0a36090e64f74fee84fe40e531d66f99?x-expires=1974358800&x-signature=WEiCKF1b0kbmFXyZrKvlH1NuDc4%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "shuai.png",
    "display_name": "[衰]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/cbd66aa8898e44f2948717479c32b1d2",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/cbd66aa8898e44f2948717479c32b1d2?x-expires=1974358800&x-signature=Vz%2BLS96tYF92YUMd%2BnUAewOsxPE%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/cbd66aa8898e44f2948717479c32b1d2?x-expires=1974358800&x-signature=%2BTlNfG4XHL0pMNx%2FjDMJ2s0v2h0%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/cbd66aa8898e44f2948717479c32b1d2?x-expires=1974358800&x-signature=vNDLaxHdDdi9TGtOv8hz6Ctjbv8%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "bizui.png",
    "display_name": "[闭嘴]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/e2137e619d12402f9a0c8025196d0f0c",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/e2137e619d12402f9a0c8025196d0f0c?x-expires=1974358800&x-signature=Hu8z7Vg8tT1zfF6hoQCy5jCNm%2FY%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/e2137e619d12402f9a0c8025196d0f0c?x-expires=1974358800&x-signature=uNfNxE0xcmvM5gLgMSANN%2BQ5Z4Y%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/e2137e619d12402f9a0c8025196d0f0c?x-expires=1974358800&x-signature=pAl1gOW3QAuYelT6%2FD3sPbxMPh4%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "jizhi.png",
    "display_name": "[机智]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/9909281d65394d649f5e6ebf8c49032c",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/9909281d65394d649f5e6ebf8c49032c?x-expires=1974358800&x-signature=UBXq4yYBOsTfX8qJD9x3xRUtUvE%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/9909281d65394d649f5e6ebf8c49032c?x-expires=1974358800&x-signature=Ya95QEulXlm8TeFAsJJt7ld%2FIy4%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/9909281d65394d649f5e6ebf8c49032c?x-expires=1974358800&x-signature=JgGsGNN8n%2BTAwetpAM%2BoPGbsnZs%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "zan.png",
    "display_name": "[赞]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/7cf5c75cb18f4108a97bf705e22030b6",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/7cf5c75cb18f4108a97bf705e22030b6?x-expires=1974358800&x-signature=vMophkGuNPmMlo2436zx%2B3we61k%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/7cf5c75cb18f4108a97bf705e22030b6?x-expires=1974358800&x-signature=8X2HdiuDhXGoAyhNibElIN4m3QQ%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/7cf5c75cb18f4108a97bf705e22030b6?x-expires=1974358800&x-signature=YwPkz0TosGm7MRnasCcFceSkG1o%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "guzhang.png",
    "display_name": "[鼓掌]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/e208e85a95a24302ae537b0db0ef240f",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/e208e85a95a24302ae537b0db0ef240f?x-expires=1974358800&x-signature=IMowffR1haJCvfqgs2SS7oSvI7I%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/e208e85a95a24302ae537b0db0ef240f?x-expires=1974358800&x-signature=wONNcBp1WbavN6tAWBzyfxYKQMw%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/e208e85a95a24302ae537b0db0ef240f?x-expires=1974358800&x-signature=56RssfxGG478PpPdzf1SLtCMJ%2Bw%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "qidao.png",
    "display_name": "[感谢]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/48343d02445945cdbf749c174cad360c",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/48343d02445945cdbf749c174cad360c?x-expires=1974358800&x-signature=5YC292F5ap31wDbMUym%2BnpgxJfg%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/48343d02445945cdbf749c174cad360c?x-expires=1974358800&x-signature=uuhxwax%2BGZVKk8x%2FAT%2BmnARiL5s%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/48343d02445945cdbf749c174cad360c?x-expires=1974358800&x-signature=Wb%2BZAqgqN2fauH2IeR4eH5lpgpM%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "qidao.png",
    "display_name": "[祈祷]",
    "hide": 1,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/48343d02445945cdbf749c174cad360c",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/48343d02445945cdbf749c174cad360c?x-expires=1974358800&x-signature=5YC292F5ap31wDbMUym%2BnpgxJfg%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/48343d02445945cdbf749c174cad360c?x-expires=1974358800&x-signature=uuhxwax%2BGZVKk8x%2FAT%2BmnARiL5s%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/48343d02445945cdbf749c174cad360c?x-expires=1974358800&x-signature=Wb%2BZAqgqN2fauH2IeR4eH5lpgpM%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "laikanwo.png",
    "display_name": "[来看我]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/313aae3678f94f3aaabc569e735576c2",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/313aae3678f94f3aaabc569e735576c2?x-expires=1974358800&x-signature=u09KXm5AtfITZ%2F09r4ExR63lQ08%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/313aae3678f94f3aaabc569e735576c2?x-expires=1974358800&x-signature=fyAfM5jhOgum2es3PXzrQODapys%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/313aae3678f94f3aaabc569e735576c2?x-expires=1974358800&x-signature=J%2BzXEjhxErZ90HTODk9Jmz1JAzk%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "lingguangyishan.png",
    "display_name": "[灵机一动]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/a5c8d51d16314b8bb69e34747fa66c6d",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/a5c8d51d16314b8bb69e34747fa66c6d?x-expires=1974358800&x-signature=bKnNq5WlN%2BTMo9WkxmEw2csnb5Q%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/a5c8d51d16314b8bb69e34747fa66c6d?x-expires=1974358800&x-signature=mXCOlAGF9OpK2LW9HN7S72UVS70%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/a5c8d51d16314b8bb69e34747fa66c6d?x-expires=1974358800&x-signature=lbeVfx81jc8yzntMXN6vtMmYtuk%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "lingguangyishan.png",
    "display_name": "[灵光一闪]",
    "hide": 1,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/a5c8d51d16314b8bb69e34747fa66c6d",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/a5c8d51d16314b8bb69e34747fa66c6d?x-expires=1974358800&x-signature=bKnNq5WlN%2BTMo9WkxmEw2csnb5Q%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/a5c8d51d16314b8bb69e34747fa66c6d?x-expires=1974358800&x-signature=mXCOlAGF9OpK2LW9HN7S72UVS70%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/a5c8d51d16314b8bb69e34747fa66c6d?x-expires=1974358800&x-signature=lbeVfx81jc8yzntMXN6vtMmYtuk%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "ye.png",
    "display_name": "[耶]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/c929a73d281047fb9200c28c3b7c70df",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/c929a73d281047fb9200c28c3b7c70df?x-expires=1974358800&x-signature=QN7mjbfYfq7ARafWzn2w82fA7Y4%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/c929a73d281047fb9200c28c3b7c70df?x-expires=1974358800&x-signature=E3AJGoecVmi%2BO4MD0ZG2AFNblKg%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/c929a73d281047fb9200c28c3b7c70df?x-expires=1974358800&x-signature=9iE6EgFHl7u5E5AXb3B%2FzRCT%2F84%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "dalian.png",
    "display_name": "[打脸]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/c9dda0af2db642e4b7b76e1a948595b7",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/c9dda0af2db642e4b7b76e1a948595b7?x-expires=1974358800&x-signature=9DZ50578%2BI0rbe%2F2A%2BcJwgovh38%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/c9dda0af2db642e4b7b76e1a948595b7?x-expires=1974358800&x-signature=LmhTVBYt7L2%2B%2Fqg0XJpKWzl0umc%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/c9dda0af2db642e4b7b76e1a948595b7?x-expires=1974358800&x-signature=rVHTSc3hLIHg0qWaPemev%2BDYsgM%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "daxiao.png",
    "display_name": "[大笑]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/9aec23c4c7034aae89c13db08f077b5d",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/9aec23c4c7034aae89c13db08f077b5d?x-expires=1974358800&x-signature=7S5crDaKxUjfn5YAmFU9Ooeo2Gs%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/9aec23c4c7034aae89c13db08f077b5d?x-expires=1974358800&x-signature=KjeNyTLaspu44V5dnbqhiRhl0Jg%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/9aec23c4c7034aae89c13db08f077b5d?x-expires=1974358800&x-signature=4SLwWjdYwHh3DgoUMwFCw7pthDQ%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "haqian.png",
    "display_name": "[哈欠]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/6e5a9f1587d44db3b4486d421736f462",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/6e5a9f1587d44db3b4486d421736f462?x-expires=1974358800&x-signature=8lMw5GSFuJgDK8Zj%2FS4w%2B7vNZcA%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/6e5a9f1587d44db3b4486d421736f462?x-expires=1974358800&x-signature=TyO8JOWHDc%2FgghO2%2FtVYUy0g4MI%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/6e5a9f1587d44db3b4486d421736f462?x-expires=1974358800&x-signature=RZ5HLkYKYrYqRpHfDlBb%2FnaMfW8%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "zhenliang.png",
    "display_name": "[震惊]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/9d3fd112900f476884aaf2ffa6d83db6",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/9d3fd112900f476884aaf2ffa6d83db6?x-expires=1974358800&x-signature=SHsfOTkCKkkJHsgXhI%2BjIsoP2Dc%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/9d3fd112900f476884aaf2ffa6d83db6?x-expires=1974358800&x-signature=epqLPRBYhrpT93hGUlW7XFL4Fg0%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/9d3fd112900f476884aaf2ffa6d83db6?x-expires=1974358800&x-signature=iqVz7P1OOSFREGFpgQs97Xm0KoU%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "songxin.png",
    "display_name": "[送心]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/813ee9e028fb4d0e89877e418e1ee323",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/813ee9e028fb4d0e89877e418e1ee323?x-expires=1974358800&x-signature=RSS1wz%2F9QgePb2Wuc98SfI53RXg%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/813ee9e028fb4d0e89877e418e1ee323?x-expires=1974358800&x-signature=cYc4B5BDq1qDIHij8wxhMKSetYk%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/813ee9e028fb4d0e89877e418e1ee323?x-expires=1974358800&x-signature=f4JOVBJqXUUMNkumYL9sCqGiIA4%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "kun.png",
    "display_name": "[困]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/0a03dae3ef4d4287aed4e098e2d25493",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/0a03dae3ef4d4287aed4e098e2d25493?x-expires=1974358800&x-signature=F9HhFh1kTdQndvLtI78eKfZ2oFQ%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/0a03dae3ef4d4287aed4e098e2d25493?x-expires=1974358800&x-signature=WtoKK6TW2rvUVvmbHri3jEti3lM%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/0a03dae3ef4d4287aed4e098e2d25493?x-expires=1974358800&x-signature=HbfXt9hGQw81gcMPhSqOcwsbmlQ%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "what.png",
    "display_name": "[疑问]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/e48d9d91134c482fbe0ed91700a16fd6",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/e48d9d91134c482fbe0ed91700a16fd6?x-expires=1974358800&x-signature=DPcvHiXm7%2FE0szu57V9jPc5yql0%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/e48d9d91134c482fbe0ed91700a16fd6?x-expires=1974358800&x-signature=UCXwoWIDGfF5csT%2BzewQAN%2Fknzc%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/e48d9d91134c482fbe0ed91700a16fd6?x-expires=1974358800&x-signature=cMsdy3hglyh5bqxrZFgWLmXch74%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "what.png",
    "display_name": "[what]",
    "hide": 1,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/e48d9d91134c482fbe0ed91700a16fd6",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/e48d9d91134c482fbe0ed91700a16fd6?x-expires=1974358800&x-signature=DPcvHiXm7%2FE0szu57V9jPc5yql0%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/e48d9d91134c482fbe0ed91700a16fd6?x-expires=1974358800&x-signature=UCXwoWIDGfF5csT%2BzewQAN%2Fknzc%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/e48d9d91134c482fbe0ed91700a16fd6?x-expires=1974358800&x-signature=cMsdy3hglyh5bqxrZFgWLmXch74%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "qibuchengsheng.png",
    "display_name": "[泣不成声]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/9091e41bbd7f4a4d9eb613a459f24203",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/9091e41bbd7f4a4d9eb613a459f24203?x-expires=1974358800&x-signature=dQRfIjzWyPOpd7%2FiefoeBtSJRyU%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/9091e41bbd7f4a4d9eb613a459f24203?x-expires=1974358800&x-signature=893spIdNlFzkKhnfBV8bI7L2shA%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/9091e41bbd7f4a4d9eb613a459f24203?x-expires=1974358800&x-signature=AYhii1XtW3ucfflxJ%2BIf51oR8sU%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "xiaoguzhang.png",
    "display_name": "[小鼓掌]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/04f536918fad4e38a7c7365a2c3957e5",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/04f536918fad4e38a7c7365a2c3957e5?x-expires=1974358800&x-signature=PXzoX%2BqFrofubq9Ry3I2xu%2FnMCw%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/04f536918fad4e38a7c7365a2c3957e5?x-expires=1974358800&x-signature=ZAiw11RI66UtXQXBAgX6vtYJs5U%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/04f536918fad4e38a7c7365a2c3957e5?x-expires=1974358800&x-signature=UCLSrZ0%2Fh%2BW%2FH3Tc37QcbN%2FJY%2Bc%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "dajinya.png",
    "display_name": "[大金牙]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/14780a881aa04ea78390c9920ff7d490",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/14780a881aa04ea78390c9920ff7d490?x-expires=1974358800&x-signature=mene0qVNtUJ5Sh09MoMByWppwt0%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/14780a881aa04ea78390c9920ff7d490?x-expires=1974358800&x-signature=Sx9YrYJnd1Ds5F5aF2BooTPKszE%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/14780a881aa04ea78390c9920ff7d490?x-expires=1974358800&x-signature=RJ7Ml1q%2FxaEVMQey6HS0OzRw1iI%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "touxiao.png",
    "display_name": "[偷笑]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/3d6c8c53488147cdbddd7b7559f17085",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/3d6c8c53488147cdbddd7b7559f17085?x-expires=1974358800&x-signature=0m9zWJM%2FmFhsr3oxRrWqmWhqA3g%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/3d6c8c53488147cdbddd7b7559f17085?x-expires=1974358800&x-signature=B%2FjC37HUALcRjfb%2F2rjREVDuZ3s%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/3d6c8c53488147cdbddd7b7559f17085?x-expires=1974358800&x-signature=MV0ESQJs3rbZiPg54D01q%2FH2elo%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "shihua.png",
    "display_name": "[石化]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/9b4b40f45204492c872e22ffaf129488",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/9b4b40f45204492c872e22ffaf129488?x-expires=1974358800&x-signature=ZH1M%2FGt3DO5bjYxAAQZPFN6Ipww%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/9b4b40f45204492c872e22ffaf129488?x-expires=1974358800&x-signature=%2F9iD0JvZHAA9BpebQNfXXcp2Ml8%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/9b4b40f45204492c872e22ffaf129488?x-expires=1974358800&x-signature=BbeDVSsNYoMPXA1NFP8cCTtNBxY%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "sikao.png",
    "display_name": "[思考]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/c6a75348bf99490f985383b81aa8ad67",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/c6a75348bf99490f985383b81aa8ad67?x-expires=1974358800&x-signature=te0Fwl%2BxsfzrFN%2BEp1Wciwj6Ak0%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/c6a75348bf99490f985383b81aa8ad67?x-expires=1974358800&x-signature=yT4u826Azzp5SUmhmM8I7E7DfJ8%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/c6a75348bf99490f985383b81aa8ad67?x-expires=1974358800&x-signature=V40drsEd2o4i%2FTfMUjcLhyPv2Bg%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "tuxie.png",
    "display_name": "[吐血]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/5028b616e7024a5594d8da60fa37bc1a",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/5028b616e7024a5594d8da60fa37bc1a?x-expires=1974358800&x-signature=WSQleCPjsvkhbhYcVWlLKo4gMEk%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/5028b616e7024a5594d8da60fa37bc1a?x-expires=1974358800&x-signature=kJ49a%2B%2BibixIa1cxF1OBGr0T1ng%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/5028b616e7024a5594d8da60fa37bc1a?x-expires=1974358800&x-signature=ag9NYvfhwbYcKNaNaoaefbW4EI4%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "kelian.png",
    "display_name": "[可怜]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/6a60bc110a6c462b9bb8c1acf3541da9",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/6a60bc110a6c462b9bb8c1acf3541da9?x-expires=1974358800&x-signature=pmKP1Ph3xPwY%2BptIreX1asHCM8g%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/6a60bc110a6c462b9bb8c1acf3541da9?x-expires=1974358800&x-signature=uT%2FOb6D8dHneNm6e20ImjFCbz2M%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/6a60bc110a6c462b9bb8c1acf3541da9?x-expires=1974358800&x-signature=cI4Q3A7yw6u%2BYpDPMO5KFLWBxWo%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "xu.png",
    "display_name": "[嘘]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/057ce5c1afd14183803065343ac35abe",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/057ce5c1afd14183803065343ac35abe?x-expires=1974358800&x-signature=Ytbppzlka8NS9Cn50hMSa02EOoY%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/057ce5c1afd14183803065343ac35abe?x-expires=1974358800&x-signature=UNcLROit0vssjfPV9p8AXhSaWO0%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/057ce5c1afd14183803065343ac35abe?x-expires=1974358800&x-signature=Dept4yi7I47Vp1Qx7Q2LY04gOBc%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "piezui.png",
    "display_name": "[撇嘴]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/b18bd2225a214a0a97d72c4ecc75f2c4",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/b18bd2225a214a0a97d72c4ecc75f2c4?x-expires=1974358800&x-signature=zsRtBf1rgUKXz%2FNvmX33O%2F%2FH9f0%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/b18bd2225a214a0a97d72c4ecc75f2c4?x-expires=1974358800&x-signature=LH9tACSkv8J7ANmjHqaNlpNO3iE%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/b18bd2225a214a0a97d72c4ecc75f2c4?x-expires=1974358800&x-signature=SAGwicYxFn1YmEn1KmfyGrqhlDQ%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "heixian.png",
    "display_name": "[尴尬]",
    "hide": 1,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/3b8ebc4412784f55a4f23984715c918b",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/3b8ebc4412784f55a4f23984715c918b?x-expires=1974358800&x-signature=T3Z1coMFUGmAcXiU3w76YgloIMM%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/3b8ebc4412784f55a4f23984715c918b?x-expires=1974358800&x-signature=mg410dL%2F8LrdIYPWw3Xgy34LNx4%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/3b8ebc4412784f55a4f23984715c918b?x-expires=1974358800&x-signature=SY2o1V5MWYuNooVJlPa8Tm2RyaE%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "heixian.png",
    "display_name": "[黑线]",
    "hide": 1,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/3b8ebc4412784f55a4f23984715c918b",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/3b8ebc4412784f55a4f23984715c918b?x-expires=1974358800&x-signature=T3Z1coMFUGmAcXiU3w76YgloIMM%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/3b8ebc4412784f55a4f23984715c918b?x-expires=1974358800&x-signature=mg410dL%2F8LrdIYPWw3Xgy34LNx4%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/3b8ebc4412784f55a4f23984715c918b?x-expires=1974358800&x-signature=SY2o1V5MWYuNooVJlPa8Tm2RyaE%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "xiaoku.png",
    "display_name": "[笑哭]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/51b52a85053a407db828e01a3abc9fa4",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/51b52a85053a407db828e01a3abc9fa4?x-expires=1974358800&x-signature=G2NQcFfp2YyYmmJQN%2FmhLzRBmQM%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/51b52a85053a407db828e01a3abc9fa4?x-expires=1974358800&x-signature=nCH8fW4WYeCvDROJSd9RaY5RJrI%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/51b52a85053a407db828e01a3abc9fa4?x-expires=1974358800&x-signature=FKeo2pvW%2Bhmiyy3ZaI8tIgftuDI%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "wumai.png",
    "display_name": "[生病]",
    "hide": 1,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/539bece82d9846808eb3855e27fdffd6",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/539bece82d9846808eb3855e27fdffd6?x-expires=1974358800&x-signature=TjhNV018zFD8ZfcyS4NwVtk7tVw%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/539bece82d9846808eb3855e27fdffd6?x-expires=1974358800&x-signature=ZZvkTmtLvAHE5pzIv%2FW%2BUcouJL8%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/539bece82d9846808eb3855e27fdffd6?x-expires=1974358800&x-signature=NN%2Bgj8bUNb3KFgPBO4rbwYZAlFE%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "wumai.png",
    "display_name": "[雾霾]",
    "hide": 1,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/539bece82d9846808eb3855e27fdffd6",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/539bece82d9846808eb3855e27fdffd6?x-expires=1974358800&x-signature=TjhNV018zFD8ZfcyS4NwVtk7tVw%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/539bece82d9846808eb3855e27fdffd6?x-expires=1974358800&x-signature=ZZvkTmtLvAHE5pzIv%2FW%2BUcouJL8%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/539bece82d9846808eb3855e27fdffd6?x-expires=1974358800&x-signature=NN%2Bgj8bUNb3KFgPBO4rbwYZAlFE%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "jianxiao.png",
    "display_name": "[奸笑]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/39b5963eef5341a981ac83c2e9496711",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/39b5963eef5341a981ac83c2e9496711?x-expires=1974358800&x-signature=wHf7YGJeKd6suppH8%2FtuKpm8kPg%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/39b5963eef5341a981ac83c2e9496711?x-expires=1974358800&x-signature=XrcQsa8b%2B35HuAJ3iWqJO78zj3I%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/39b5963eef5341a981ac83c2e9496711?x-expires=1974358800&x-signature=2Lr86MpLHGv9cvD%2BmhKNbC14RIE%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "deyi.png",
    "display_name": "[得意]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/f8964cc6372f4bb9ac4a437f1f173fb3",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/f8964cc6372f4bb9ac4a437f1f173fb3?x-expires=1974358800&x-signature=tbm%2FovIqYhmVlwTR%2B2i%2BNea7V6o%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/f8964cc6372f4bb9ac4a437f1f173fb3?x-expires=1974358800&x-signature=3OGoMcsa6KVE60cgSMMjQPFdg5Q%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/f8964cc6372f4bb9ac4a437f1f173fb3?x-expires=1974358800&x-signature=jfJO3sKxXAlL5ncsps6gJuLnfpk%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "hanxiao.png",
    "display_name": "[憨笑]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/e8cb80fdc4bb4c46b6421087fe2d0669",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/e8cb80fdc4bb4c46b6421087fe2d0669?x-expires=1974358800&x-signature=RbABEQM5W9ATXOJcmrpAAxr0f8U%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/e8cb80fdc4bb4c46b6421087fe2d0669?x-expires=1974358800&x-signature=pM9gMe%2BtHp%2B3mYDXEOr7A%2FxWF8A%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/e8cb80fdc4bb4c46b6421087fe2d0669?x-expires=1974358800&x-signature=V4JlgYhjPy%2B33VjR8BkFHJEGuRI%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "huaixiao.png",
    "display_name": "[坏笑]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/21036bfb76bb43d592b3bc119e5835e5",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/21036bfb76bb43d592b3bc119e5835e5?x-expires=1974358800&x-signature=JKblSrsR66QYhc4wXBbc5nX144Q%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/21036bfb76bb43d592b3bc119e5835e5?x-expires=1974358800&x-signature=MM3ieogrzB%2FElddeHPEv4fKtO8w%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/21036bfb76bb43d592b3bc119e5835e5?x-expires=1974358800&x-signature=nqIwGp5qFHijVDxQky3CsfTCto4%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "zhuakuang.png",
    "display_name": "[抓狂]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/cae0647eba954b719d3cd4cc287e7103",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/cae0647eba954b719d3cd4cc287e7103?x-expires=1974358800&x-signature=7MTry9wuehVruFmxIpKKcR4aANU%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/cae0647eba954b719d3cd4cc287e7103?x-expires=1974358800&x-signature=j0CCaVEEZqXx34yazLaR8QnJKiM%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/cae0647eba954b719d3cd4cc287e7103?x-expires=1974358800&x-signature=hgIDx2CR2NYUWvWCxX9yv7uW6jk%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "leiben.png",
    "display_name": "[泪奔]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/4ad886baeb8a496a87be86d4dafaf752",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/4ad886baeb8a496a87be86d4dafaf752?x-expires=1974358800&x-signature=ifR1CVgBIXx%2BJ8N%2Fd6LXiY8v3ww%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/4ad886baeb8a496a87be86d4dafaf752?x-expires=1974358800&x-signature=bA%2B%2Fib%2BIK8nUSjTFqFdSOxpJEyc%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/4ad886baeb8a496a87be86d4dafaf752?x-expires=1974358800&x-signature=TbVEKQllWyvXxyuhBmEzoJ7RU0I%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "qian.png",
    "display_name": "[钱]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/dd31ced47a8146b3a0da71a311f11045",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/dd31ced47a8146b3a0da71a311f11045?x-expires=1974358800&x-signature=Z4a%2B1yyf8bU8ne%2BabKbkVuLYYiw%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/dd31ced47a8146b3a0da71a311f11045?x-expires=1974358800&x-signature=mYNZ84B2ffXvgZs3mOd9b7alXIQ%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/dd31ced47a8146b3a0da71a311f11045?x-expires=1974358800&x-signature=PK7WtxneEO%2BeVCVuhBXojFL4JYM%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "wen.png",
    "display_name": "[亲亲]",
    "hide": 1,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/b9656bf2c9e94e03b3450c844f530724",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/b9656bf2c9e94e03b3450c844f530724?x-expires=1974358800&x-signature=4HoewmsodK7NdcSv%2BzOaOC%2Fm3F4%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/b9656bf2c9e94e03b3450c844f530724?x-expires=1974358800&x-signature=h4nDrK7o1VHeCTrtVMBS4xIv%2FOY%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/b9656bf2c9e94e03b3450c844f530724?x-expires=1974358800&x-signature=qD4VjxOhrM9s0fTVDrnY4txE5g4%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "wen.png",
    "display_name": "[吻]",
    "hide": 1,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/b9656bf2c9e94e03b3450c844f530724",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/b9656bf2c9e94e03b3450c844f530724?x-expires=1974358800&x-signature=4HoewmsodK7NdcSv%2BzOaOC%2Fm3F4%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/b9656bf2c9e94e03b3450c844f530724?x-expires=1974358800&x-signature=h4nDrK7o1VHeCTrtVMBS4xIv%2FOY%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/b9656bf2c9e94e03b3450c844f530724?x-expires=1974358800&x-signature=qD4VjxOhrM9s0fTVDrnY4txE5g4%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "kongju.png",
    "display_name": "[恐惧]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/711fd4710bc8482d972dd1c3bb324529",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/711fd4710bc8482d972dd1c3bb324529?x-expires=1974358800&x-signature=oJcyV5KmzahbwI0CqMpDakcoCCA%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/711fd4710bc8482d972dd1c3bb324529?x-expires=1974358800&x-signature=Xh1nOhoWXQUJp6p9t2SJY9J646k%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/711fd4710bc8482d972dd1c3bb324529?x-expires=1974358800&x-signature=sK%2B2PbdxbPRqpHBuWtOaOHW9ZIU%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "xiao.png",
    "display_name": "[愉快]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/88da3544e4224adc857fa12deed7a059",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/88da3544e4224adc857fa12deed7a059?x-expires=1974358800&x-signature=aJZ4BkPFyF8q0M%2B2QVLsEjAkvsM%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/88da3544e4224adc857fa12deed7a059?x-expires=1974358800&x-signature=djwjE5L1e4%2FUgYBuMXDXE4WqM8k%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/88da3544e4224adc857fa12deed7a059?x-expires=1974358800&x-signature=kRMD2DI1YHUqu4dkSDHqWoqZdc0%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "xiao.png",
    "display_name": "[笑]",
    "hide": 1,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/88da3544e4224adc857fa12deed7a059",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/88da3544e4224adc857fa12deed7a059?x-expires=1974358800&x-signature=aJZ4BkPFyF8q0M%2B2QVLsEjAkvsM%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/88da3544e4224adc857fa12deed7a059?x-expires=1974358800&x-signature=djwjE5L1e4%2FUgYBuMXDXE4WqM8k%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/88da3544e4224adc857fa12deed7a059?x-expires=1974358800&x-signature=kRMD2DI1YHUqu4dkSDHqWoqZdc0%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "kuaikule.png",
    "display_name": "[快哭了]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/5ba52d4240d747c3a2be0a3a2971a27f",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/5ba52d4240d747c3a2be0a3a2971a27f?x-expires=1974358800&x-signature=zwynbz1DTZ1cYV72JPtPdzDHDIw%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/5ba52d4240d747c3a2be0a3a2971a27f?x-expires=1974358800&x-signature=35S%2FJ%2F03MQ3ndZkW%2F07Qcisd5Ok%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/5ba52d4240d747c3a2be0a3a2971a27f?x-expires=1974358800&x-signature=%2Ba5yOUG6dp%2Buxqvz3S%2FyWxF49Ek%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "fanbaiyan.png",
    "display_name": "[翻白眼]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/d12abcc93e62465196d412d588f9eb14",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/d12abcc93e62465196d412d588f9eb14?x-expires=1974358800&x-signature=LlMIMVN81fS33EAWiZf%2FAnkYKys%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/d12abcc93e62465196d412d588f9eb14?x-expires=1974358800&x-signature=8D0JbrB6KadCRroSHd4brk3%2FSh8%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/d12abcc93e62465196d412d588f9eb14?x-expires=1974358800&x-signature=1c2l%2FsQw3NiWYW9K8fytGHYV3dY%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "fanbaiyan.png",
    "display_name": "[傲慢]",
    "hide": 1,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/d12abcc93e62465196d412d588f9eb14",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/d12abcc93e62465196d412d588f9eb14?x-expires=1974358800&x-signature=LlMIMVN81fS33EAWiZf%2FAnkYKys%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/d12abcc93e62465196d412d588f9eb14?x-expires=1974358800&x-signature=8D0JbrB6KadCRroSHd4brk3%2FSh8%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/d12abcc93e62465196d412d588f9eb14?x-expires=1974358800&x-signature=1c2l%2FsQw3NiWYW9K8fytGHYV3dY%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "hufen.png",
    "display_name": "[互粉]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/20fcf819fb1e4992bf394533a8d0d3cd",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/20fcf819fb1e4992bf394533a8d0d3cd?x-expires=1974358800&x-signature=7eTBuSMjMfxYeCWOrqSYa7mgCto%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/20fcf819fb1e4992bf394533a8d0d3cd?x-expires=1974358800&x-signature=JiCwKst8lxXpc%2BJg8OvnwkYSfHo%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/20fcf819fb1e4992bf394533a8d0d3cd?x-expires=1974358800&x-signature=NHHTcso7eMXKXOBFKiGT4YEJxpk%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "woxiangjingjing.png",
    "display_name": "[我想静静]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/3fb34faa90c0473f93e55070fee5161b",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/3fb34faa90c0473f93e55070fee5161b?x-expires=1974358800&x-signature=pVMuCnipV9pTyW8Haql4Jbebbos%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/3fb34faa90c0473f93e55070fee5161b?x-expires=1974358800&x-signature=OTue7YPAvwA8KwqgGnXJzi79tD4%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/3fb34faa90c0473f93e55070fee5161b?x-expires=1974358800&x-signature=lfnEMvgO%2F81ktv%2FACg098icOoug%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "weiqu.png",
    "display_name": "[委屈]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/c2cdc903cb0b43969a2812589faf2ee4",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/c2cdc903cb0b43969a2812589faf2ee4?x-expires=1974358800&x-signature=A1oKenjjs94G6cBX2wL8Wi0uYKY%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/c2cdc903cb0b43969a2812589faf2ee4?x-expires=1974358800&x-signature=vsMcYoAP1wxSDd%2BKL0Up%2B6EfkTE%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/c2cdc903cb0b43969a2812589faf2ee4?x-expires=1974358800&x-signature=iIHt%2FPh6koQe71LaNJbCsbY0yYs%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "tianping.png",
    "display_name": "[舔屏]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/0e8544c70c33474e8dbc9fa16bd54735",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/0e8544c70c33474e8dbc9fa16bd54735?x-expires=1974358800&x-signature=OMlW2SzLvgyU3kA%2FoG9x5%2BwXoas%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/0e8544c70c33474e8dbc9fa16bd54735?x-expires=1974358800&x-signature=QlIwwso4ZLEz3FI4SqtYSpxMGpo%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/0e8544c70c33474e8dbc9fa16bd54735?x-expires=1974358800&x-signature=WYsyDqaA72r58ooZphYTsOYRBnA%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "bishi.png",
    "display_name": "[鄙视]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/fd969a2ae53d4c588d2e316a1d498d07",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/fd969a2ae53d4c588d2e316a1d498d07?x-expires=1974358800&x-signature=dWuWvJAbJA0rQaSOZVc1Rkm%2BrIk%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/fd969a2ae53d4c588d2e316a1d498d07?x-expires=1974358800&x-signature=U9SR72EgX%2BvqIfOK11dNcn5VhKg%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/fd969a2ae53d4c588d2e316a1d498d07?x-expires=1974358800&x-signature=yuKRGMSa8jAcZ8Lx1vHravSt%2FRM%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "feiwen.png",
    "display_name": "[飞吻]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/d032b68fcddd47b690ca3ea695ffc1f3",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/d032b68fcddd47b690ca3ea695ffc1f3?x-expires=1974358800&x-signature=9Nr%2FT8uwg3l%2BnF0BOVLcSmLNfK8%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/d032b68fcddd47b690ca3ea695ffc1f3?x-expires=1974358800&x-signature=sD%2FETd3gCmDK9voNt1C7uKvj9w8%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/d032b68fcddd47b690ca3ea695ffc1f3?x-expires=1974358800&x-signature=W9PLatiScq68B%2BGCmlfPev3IaOM%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "zaijian.png",
    "display_name": "[再见]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/48ed961024f245f38913e94a4443c816",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/48ed961024f245f38913e94a4443c816?x-expires=1974358800&x-signature=5mAg69x%2BuCC48ranDmAKM7seyKU%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/48ed961024f245f38913e94a4443c816?x-expires=1974358800&x-signature=BzGZdvTL%2BGPxB6zoYHGHVDKWlN0%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/48ed961024f245f38913e94a4443c816?x-expires=1974358800&x-signature=i4i%2Bks1qJiJYVxEfCfvKnTku0dA%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "ziweibiezou.png",
    "display_name": "[紫薇别走]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/ea556c396fd44e869a19f5697d3e2776",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/ea556c396fd44e869a19f5697d3e2776?x-expires=1974358800&x-signature=lnv3olJd6Ga8oR1S%2B6dn%2FWHvBu8%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/ea556c396fd44e869a19f5697d3e2776?x-expires=1974358800&x-signature=NYzAvk76OcTCJdSvdqfzWjHV8jE%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/ea556c396fd44e869a19f5697d3e2776?x-expires=1974358800&x-signature=%2BqTNo4LOxcNhEsI3W64cqceE5Ok%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "tingge.png",
    "display_name": "[听歌]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/ed59fa28572b46a59acf4e94d5b78b0b",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/ed59fa28572b46a59acf4e94d5b78b0b?x-expires=1974358800&x-signature=OZjCliEHJaGYEXz29AnpBR2jrzw%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/ed59fa28572b46a59acf4e94d5b78b0b?x-expires=1974358800&x-signature=mC5r%2BkEvxIpHr%2Be8%2FCwOywIlfpI%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/ed59fa28572b46a59acf4e94d5b78b0b?x-expires=1974358800&x-signature=Km5L54w%2Fmzj6VpcEj0bFhctTSME%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "qiubaobao.png",
    "display_name": "[拥抱]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/3536d28066e04109952779ced5f2033d",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/3536d28066e04109952779ced5f2033d?x-expires=1974358800&x-signature=QqGGJ4bbHJP8%2Fa0KVfcDicv1RsY%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/3536d28066e04109952779ced5f2033d?x-expires=1974358800&x-signature=Vqg%2BhdtskpWhc%2BBxTnCbTofAJBw%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/3536d28066e04109952779ced5f2033d?x-expires=1974358800&x-signature=H56JEj3VCu6F4n6hF7Omf4JPL%2FI%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "qiubaobao.png",
    "display_name": "[求抱抱]",
    "hide": 1,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/3536d28066e04109952779ced5f2033d",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/3536d28066e04109952779ced5f2033d?x-expires=1974358800&x-signature=QqGGJ4bbHJP8%2Fa0KVfcDicv1RsY%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/3536d28066e04109952779ced5f2033d?x-expires=1974358800&x-signature=Vqg%2BhdtskpWhc%2BBxTnCbTofAJBw%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/3536d28066e04109952779ced5f2033d?x-expires=1974358800&x-signature=H56JEj3VCu6F4n6hF7Omf4JPL%2FI%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "zhoudongyudeningshi.png",
    "display_name": "[绝望的凝视]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/d52344b3ffb349889ea42941b340a3ef",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/d52344b3ffb349889ea42941b340a3ef?x-expires=1974358800&x-signature=DiFnTxTZ5RiT%2BNVcw1g9baxuX4s%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/d52344b3ffb349889ea42941b340a3ef?x-expires=1974358800&x-signature=upOhx8Mq2L19rgvIcmeqlqEN1pg%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/d52344b3ffb349889ea42941b340a3ef?x-expires=1974358800&x-signature=hSG901AwVxCJXBrllUDKeiB4N8I%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "masichundeweixiao.png",
    "display_name": "[不失礼貌的微笑]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/928212c27c0f4e16b5a3a08b01cbe31d",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/928212c27c0f4e16b5a3a08b01cbe31d?x-expires=1974358800&x-signature=J2Sfeq22Wbm8fo8txdOKkHHzpcY%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/928212c27c0f4e16b5a3a08b01cbe31d?x-expires=1974358800&x-signature=dp%2B6fEU8jRIBPElV4qKtPYDScDQ%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/928212c27c0f4e16b5a3a08b01cbe31d?x-expires=1974358800&x-signature=ZHK8JPgKqx%2F6vwID6RHrV6mtOa8%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "bukan.png",
    "display_name": "[不看]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/7e1023e408cb4dae9173549c411436a7",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/7e1023e408cb4dae9173549c411436a7?x-expires=1974358800&x-signature=fpZnXvqyiataG9%2FIMXf1%2FamNWWs%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/7e1023e408cb4dae9173549c411436a7?x-expires=1974358800&x-signature=lm4AL211zaogWnye9umoE%2BtAYkw%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/7e1023e408cb4dae9173549c411436a7?x-expires=1974358800&x-signature=cDIKmNjD1dC2OABQy4HWDdQzhxA%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "liekai.png",
    "display_name": "[裂开]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/993c9a74a7454464aa85d2d8f24f118a",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/993c9a74a7454464aa85d2d8f24f118a?x-expires=1974358800&x-signature=f%2BzKPvawrA2t6zpnW7Hx7Yuka6k%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/993c9a74a7454464aa85d2d8f24f118a?x-expires=1974358800&x-signature=7nibUVze4oQM9gTIT6MzOSl9zqw%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/993c9a74a7454464aa85d2d8f24f118a?x-expires=1974358800&x-signature=VutAVkFYdp49mW1%2F3s114cv7Qws%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "ganfanren.png",
    "display_name": "[干饭人]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/9867ae11e7e044a9919f9cef5bd64282",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/9867ae11e7e044a9919f9cef5bd64282?x-expires=1974358800&x-signature=Fk2eCsRGXEjz%2Bsszukv3vnhzsm0%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/9867ae11e7e044a9919f9cef5bd64282?x-expires=1974358800&x-signature=anf%2FRtjb9masnALG8yMLZKbYrBE%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/9867ae11e7e044a9919f9cef5bd64282?x-expires=1974358800&x-signature=%2F9Xv1Q4yogF%2FuFg%2B0%2F176CqsTT0%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "tushe.png",
    "display_name": "[吐舌]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/1082dec2edec44ad9cb8b61f20809419",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/1082dec2edec44ad9cb8b61f20809419?x-expires=1974358800&x-signature=xuv2CvfQsQKyXk%2FtmmtiKJRa5ec%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/1082dec2edec44ad9cb8b61f20809419?x-expires=1974358800&x-signature=3Bsuw3d46yUMlkw1WTVEmJaYC%2F0%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/1082dec2edec44ad9cb8b61f20809419?x-expires=1974358800&x-signature=S0zdkNdALhn%2F3ky%2B6%2F3OkzXlvQo%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "daiwugu.png",
    "display_name": "[呆无辜]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/12399b7ebc794b7c90c7ab9e008f11e3",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/12399b7ebc794b7c90c7ab9e008f11e3?x-expires=1974358800&x-signature=IS3V60PTPPBKJAzi%2Fe22sMEH6iA%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/12399b7ebc794b7c90c7ab9e008f11e3?x-expires=1974358800&x-signature=KX5vhV2YzS8yOp7PYi%2F9eEMejtM%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/12399b7ebc794b7c90c7ab9e008f11e3?x-expires=1974358800&x-signature=xJJjjiirR05uOPnbmZyYLjU%2Bga8%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "kan.png",
    "display_name": "[看]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/a1d72022ec604e578583bf2dd4216d9c",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/a1d72022ec604e578583bf2dd4216d9c?x-expires=1974358800&x-signature=eYx7cygpLQuaV8rCi%2FqHh%2FiLCFA%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/a1d72022ec604e578583bf2dd4216d9c?x-expires=1974358800&x-signature=RT9cGCoLJU4km%2FXTdPjKQJScKxU%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/a1d72022ec604e578583bf2dd4216d9c?x-expires=1974358800&x-signature=WGC00CjSyr2mqwjXst0xeOOAhWI%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "baiyan.png",
    "display_name": "[白眼]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/ecc05aaf214d499691b5c1d05b26191c",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/ecc05aaf214d499691b5c1d05b26191c?x-expires=1974358800&x-signature=jjRgzJfyKNzwNdKF1CZztrrJOBc%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/ecc05aaf214d499691b5c1d05b26191c?x-expires=1974358800&x-signature=iS9v3G0BzpWcocPrQQ3glicGLUE%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/ecc05aaf214d499691b5c1d05b26191c?x-expires=1974358800&x-signature=xmPDgMbT5oISHo5vSkJ%2Be1iu8gA%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "xiongji.png",
    "display_name": "[熊吉]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/8f58b75d84324621b30b2a53942de384",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/8f58b75d84324621b30b2a53942de384?x-expires=1974358800&x-signature=64IR1En6m0lDfH2XXyC9HDTtIpk%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/8f58b75d84324621b30b2a53942de384?x-expires=1974358800&x-signature=atPgTqmxvx6jNzm8B3uIa1egBTA%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/8f58b75d84324621b30b2a53942de384?x-expires=1974358800&x-signature=845PWEztpaqbiQ%2FNSUaY38ZbyXI%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "zhutou.png",
    "display_name": "[猪头]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/b7f6fabe0b914dd8b53a88eade735360",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/b7f6fabe0b914dd8b53a88eade735360?x-expires=1974358800&x-signature=k2%2FDOW3rR6wPZSq80hwx4lORP4E%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/b7f6fabe0b914dd8b53a88eade735360?x-expires=1974358800&x-signature=pcNcrOqTlNFQE7dcqcCAjWhVVLg%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/b7f6fabe0b914dd8b53a88eade735360?x-expires=1974358800&x-signature=mzNWM3A74S6fhtsiW3nu18cJNP8%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "lengmo.png",
    "display_name": "[冷漠]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/75c221312e994a34821ed011df40f6a5",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/75c221312e994a34821ed011df40f6a5?x-expires=1974358800&x-signature=3n8tBeZYBN56f3PBugjsoNnKO9M%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/75c221312e994a34821ed011df40f6a5?x-expires=1974358800&x-signature=dUv6%2Bl0RP0ftd%2BbsLo5FrmkBw%2FI%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/75c221312e994a34821ed011df40f6a5?x-expires=1974358800&x-signature=1oKGOYGmA%2FIAPaMcwmKi%2FLErLlc%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "weixiaodaishu.png",
    "display_name": "[微笑袋鼠]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/b023324a9f1740a69abddd70a8636001",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/b023324a9f1740a69abddd70a8636001?x-expires=1974358800&x-signature=80yFl%2BGzcZtO84dQiHa6Kwtuows%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/b023324a9f1740a69abddd70a8636001?x-expires=1974358800&x-signature=k0xAFk%2FjXACJsP%2FIoxYuB3wMC94%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/b023324a9f1740a69abddd70a8636001?x-expires=1974358800&x-signature=D8KkgB%2F8liL%2BfMp8eig2CjEOqKk%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "ningshi.png",
    "display_name": "[凝视]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/45e64517b41548acac2020ab91f0839a",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/45e64517b41548acac2020ab91f0839a?x-expires=1974358800&x-signature=eibhpZ727eAluuaBaNiK%2BQl2xPQ%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/45e64517b41548acac2020ab91f0839a?x-expires=1974358800&x-signature=Hi4KSVPIWOXgUblNL0Ip%2FePmCR8%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/45e64517b41548acac2020ab91f0839a?x-expires=1974358800&x-signature=5bumq5VBHjYPC2tOVvDwpj4DxUo%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "anzhongguancha.png",
    "display_name": "[暗中观察]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/fb9c5374e97744b99a5784437102e179",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/fb9c5374e97744b99a5784437102e179?x-expires=1974358800&x-signature=yki221mENvBvGZa8xI53hY21MI8%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/fb9c5374e97744b99a5784437102e179?x-expires=1974358800&x-signature=NuvYAAKQhjfBMxKa%2Ffa6ab32lhQ%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/fb9c5374e97744b99a5784437102e179?x-expires=1974358800&x-signature=FE4DrEn74Unfe%2B6Lrrm%2FXBOV%2FRo%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "erha.png",
    "display_name": "[二哈]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/827a922e371c4c53b82f58b30f97448c",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/827a922e371c4c53b82f58b30f97448c?x-expires=1974358800&x-signature=xmPGLyWCOGdVEXbh8P580IPLbyg%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/827a922e371c4c53b82f58b30f97448c?x-expires=1974358800&x-signature=MrlIGMbARyDcJDT%2B634k448EoDo%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/827a922e371c4c53b82f58b30f97448c?x-expires=1974358800&x-signature=NgK28XytYMI%2FyxOLwCu6ehUmatk%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "caigou.png",
    "display_name": "[菜狗]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/d799895847aa4b43a9fe6d40427b8395",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/d799895847aa4b43a9fe6d40427b8395?x-expires=1974358800&x-signature=4kodvE67I1QkERWaO8xDvgFd7xo%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/d799895847aa4b43a9fe6d40427b8395?x-expires=1974358800&x-signature=Dhil2SgfvikYZRR%2BJWmHJrj7Wfk%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/d799895847aa4b43a9fe6d40427b8395?x-expires=1974358800&x-signature=0vwy0C4a4n8Tvt6vSdxJsmH6Osw%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "kulou.png",
    "display_name": "[骷髅]",
    "hide": 1,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/2e56e2cbc3dd49168755d94d8443c197",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/2e56e2cbc3dd49168755d94d8443c197?x-expires=1974358800&x-signature=6gsygmYmUE1PeZrMD6Uq%2FfdF1Zo%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/2e56e2cbc3dd49168755d94d8443c197?x-expires=1974358800&x-signature=oDO6ZF86ZfFM2xHY5NPg73DdEmo%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/2e56e2cbc3dd49168755d94d8443c197?x-expires=1974358800&x-signature=%2FYiUCtAylG43ERwccBJ%2BQww4rbA%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "heilian.png",
    "display_name": "[黑脸]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/d61933b9dc264422ab092b4b703d3c76",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/d61933b9dc264422ab092b4b703d3c76?x-expires=1974358800&x-signature=qeR%2FgvwLf6PwiVxE7ejyV2ynt70%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/d61933b9dc264422ab092b4b703d3c76?x-expires=1974358800&x-signature=T8G%2FE9vI6BQ%2BJFwk8IOeQcxlTDc%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/d61933b9dc264422ab092b4b703d3c76?x-expires=1974358800&x-signature=8DYeg4aDM5num6PPJDqew%2BsdxbI%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "chiguaqunzhong.png",
    "display_name": "[吃瓜群众]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/da0ed1dae2894b20b62818b01d75e55e",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/da0ed1dae2894b20b62818b01d75e55e?x-expires=1974358800&x-signature=L1RhQafRLinZIdgcS2Hp%2BjQScPg%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/da0ed1dae2894b20b62818b01d75e55e?x-expires=1974358800&x-signature=%2FusQ%2FVmPINoQ5MG2vrjttixxgVw%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/da0ed1dae2894b20b62818b01d75e55e?x-expires=1974358800&x-signature=AUgB0Em0K%2BAsDZu9ENjxSdXbp6U%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "lvmaozi.png",
    "display_name": "[绿帽子]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/25e1da493d1f43ffb1264cd6f53ee846",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/25e1da493d1f43ffb1264cd6f53ee846?x-expires=1974358800&x-signature=GoXl6hqEz5pc9CSjEZW0CIivrIE%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/25e1da493d1f43ffb1264cd6f53ee846?x-expires=1974358800&x-signature=SIGGXrMP6ZEZV6yaO3imyYgrohI%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/25e1da493d1f43ffb1264cd6f53ee846?x-expires=1974358800&x-signature=%2FNOc1owtai8UjgQq2WgQucVqksU%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "han.png",
    "display_name": "[流汗]",
    "hide": 1,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/14120716789e4116a2d8b35137e423e4",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/14120716789e4116a2d8b35137e423e4?x-expires=1974358800&x-signature=d5tVYZpmJEI3aROTid1x8GgHaUg%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/14120716789e4116a2d8b35137e423e4?x-expires=1974358800&x-signature=OE1j3BwuLdxgeOjtYQCNcjkM4l0%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/14120716789e4116a2d8b35137e423e4?x-expires=1974358800&x-signature=A1Jl6H9V7%2FnggE%2FTPUps%2FA1Pg9k%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "han.png",
    "display_name": "[汗]",
    "hide": 1,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/14120716789e4116a2d8b35137e423e4",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/14120716789e4116a2d8b35137e423e4?x-expires=1974358800&x-signature=d5tVYZpmJEI3aROTid1x8GgHaUg%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/14120716789e4116a2d8b35137e423e4?x-expires=1974358800&x-signature=OE1j3BwuLdxgeOjtYQCNcjkM4l0%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/14120716789e4116a2d8b35137e423e4?x-expires=1974358800&x-signature=A1Jl6H9V7%2FnggE%2FTPUps%2FA1Pg9k%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "motou.png",
    "display_name": "[摸头]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/4170f15e44b34a8e84111dcc536b9cd6",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/4170f15e44b34a8e84111dcc536b9cd6?x-expires=1974358800&x-signature=JFYs2l0nIlyxAP%2FoqNCUqd%2BgPac%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/4170f15e44b34a8e84111dcc536b9cd6?x-expires=1974358800&x-signature=PVW937lqKZjCuIVztyccXdgEpjw%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/4170f15e44b34a8e84111dcc536b9cd6?x-expires=1974358800&x-signature=DLx6fuIFwO3PiWczN%2FjZqfXlWZw%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "zhoumei.png",
    "display_name": "[皱眉]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/abd7492ee1b045c8b859567d468ddc57",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/abd7492ee1b045c8b859567d468ddc57?x-expires=1974358800&x-signature=OkJwGsHKWiw4P9IBAqPGhTLqFvk%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/abd7492ee1b045c8b859567d468ddc57?x-expires=1974358800&x-signature=AOGryC3%2FTnRJzpdS6imZGI0HtdA%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/abd7492ee1b045c8b859567d468ddc57?x-expires=1974358800&x-signature=fQPqRVKz87oWB1GF%2Fn5s%2FaSsDHo%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "cahan.png",
    "display_name": "[擦汗]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/3f14735caabc4be195710d466533c834",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/3f14735caabc4be195710d466533c834?x-expires=1974358800&x-signature=NnLM0M9xCfyiqPoP%2ByJ5hPoJ6Ls%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/3f14735caabc4be195710d466533c834?x-expires=1974358800&x-signature=YUzFB3MBfQwms7ebvqiqvkx2fPc%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/3f14735caabc4be195710d466533c834?x-expires=1974358800&x-signature=Ir%2FrPSRHftPx5i8WyK0CUJSXvSo%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "honglian.png",
    "display_name": "[红脸]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/0c6be2e991c24be2b860ebf09cd98b19",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/0c6be2e991c24be2b860ebf09cd98b19?x-expires=1974358800&x-signature=Qa1eneRgN%2BSFfghLVv0zCTU4awI%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/0c6be2e991c24be2b860ebf09cd98b19?x-expires=1974358800&x-signature=iIyGdgzH6QhTbC3rTkrUKdzv%2Fv4%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/0c6be2e991c24be2b860ebf09cd98b19?x-expires=1974358800&x-signature=TMHNFRa2gs5sYc0hJEo9D6nb6EM%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "gaxiao.png",
    "display_name": "[尬笑]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/7694c94b0aac406fba031c7878059827",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/7694c94b0aac406fba031c7878059827?x-expires=1974358800&x-signature=fgu%2BVshSoSeGAY%2F71%2BPW5%2F0Pg6c%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/7694c94b0aac406fba031c7878059827?x-expires=1974358800&x-signature=w1RIPjAsevP4YBaTR2kazSSiTZM%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/7694c94b0aac406fba031c7878059827?x-expires=1974358800&x-signature=48XasiNBfxbHqtTYvKFjRI%2BDiCc%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "zuoguilian.png",
    "display_name": "[做鬼脸]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/4a3cccf5237042e88974697ace2d9199",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/4a3cccf5237042e88974697ace2d9199?x-expires=1974358800&x-signature=F8t7FKww32jjqrygqvdQioeMYMU%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/4a3cccf5237042e88974697ace2d9199?x-expires=1974358800&x-signature=Cpa0oUGJSiGCGzJhsuHSjyoTLWA%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/4a3cccf5237042e88974697ace2d9199?x-expires=1974358800&x-signature=BRaHY%2BB3mYP5bZPyGx1rqoZ2Hoc%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "qiang.png",
    "display_name": "[强]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/e5f34bbcfb964758a18531cfa58e4859",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/e5f34bbcfb964758a18531cfa58e4859?x-expires=1974358800&x-signature=IdpITOQ17GfXopf6k6igGWccxMs%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/e5f34bbcfb964758a18531cfa58e4859?x-expires=1974358800&x-signature=U2ug9C%2BRhstW3ikkEiTEEWqpSO8%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/e5f34bbcfb964758a18531cfa58e4859?x-expires=1974358800&x-signature=I8x6xBSc07mi8rYENBjM%2FRAXPBM%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "ruhua.png",
    "display_name": "[如花]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/7d1f8504e4a547bb91473802ee90a253",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/7d1f8504e4a547bb91473802ee90a253?x-expires=1974358800&x-signature=Bn1tOU%2BVJsiRwnMKD6Xyq1FCrco%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/7d1f8504e4a547bb91473802ee90a253?x-expires=1974358800&x-signature=JBNLEvlClvw7t%2FuI9y5hUSArFLg%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/7d1f8504e4a547bb91473802ee90a253?x-expires=1974358800&x-signature=k%2FwORQiMDplfb4CWqdstWa9eGOw%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "tu.png",
    "display_name": "[吐]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/2d0fbb3970994f239a3a8ada8fb0e89e",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/2d0fbb3970994f239a3a8ada8fb0e89e?x-expires=1974358800&x-signature=p%2Fh23rOYPmTBFA9DfyClVMoIz1w%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/2d0fbb3970994f239a3a8ada8fb0e89e?x-expires=1974358800&x-signature=crrqRIdBN54lxY4F1jyOCxCXipI%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/2d0fbb3970994f239a3a8ada8fb0e89e?x-expires=1974358800&x-signature=UIQL5karEHYbwrDDP64aqLZnWMw%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "liangxi.png",
    "display_name": "[惊喜]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/49870971bdaa44358251a619a9f70188",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/49870971bdaa44358251a619a9f70188?x-expires=1974358800&x-signature=A0M3HgZLInUPZJkacCrBI%2F5%2Bjo8%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/49870971bdaa44358251a619a9f70188?x-expires=1974358800&x-signature=xNAcT%2FQuYo9ISvDTpYde%2BGNAB2g%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/49870971bdaa44358251a619a9f70188?x-expires=1974358800&x-signature=SavAq467uLbciBQr%2FVQgyGTUveQ%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "qiaoda.png",
    "display_name": "[敲打]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/b64cde93d5b04c1fb31b196515dd25f6",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/b64cde93d5b04c1fb31b196515dd25f6?x-expires=1974358800&x-signature=94NNU8fZqo5%2FraCZEaFKKHKEz4w%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/b64cde93d5b04c1fb31b196515dd25f6?x-expires=1974358800&x-signature=DH7Anu9IAlYoi4rgM%2BZz9dsG564%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/b64cde93d5b04c1fb31b196515dd25f6?x-expires=1974358800&x-signature=UPld78n3D%2BBj3UGhQi7FSj%2Fi9K4%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "fendou.png",
    "display_name": "[奋斗]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/ba064f24e74c41e7b97441343095b551",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/ba064f24e74c41e7b97441343095b551?x-expires=1974358800&x-signature=KdciXR0SD6kbscv%2FSG5gfeeZEZc%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/ba064f24e74c41e7b97441343095b551?x-expires=1974358800&x-signature=tsYbIpTQvK1lgfSmc61mCHwfZ1s%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/ba064f24e74c41e7b97441343095b551?x-expires=1974358800&x-signature=7ed7BPukPUajU4uTswI7DKIwUck%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "tucaihong.png",
    "display_name": "[吐彩虹]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/74a7b8a6a48f447abd17cde29089aae4",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/74a7b8a6a48f447abd17cde29089aae4?x-expires=1974358800&x-signature=w90n5QUgEb2%2BPg9XCGnjVr94jbg%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/74a7b8a6a48f447abd17cde29089aae4?x-expires=1974358800&x-signature=jpyWArzuKlwgY%2BqT%2BT%2FJ%2BYtoMQQ%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/74a7b8a6a48f447abd17cde29089aae4?x-expires=1974358800&x-signature=xfXmyaYpzi6jHr3oQSr8Uk0pXqY%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "daku.png",
    "display_name": "[大哭]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/f158ee0a96ed42ebacdbb50a38393eac",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/f158ee0a96ed42ebacdbb50a38393eac?x-expires=1974358800&x-signature=IyDwXgo33hRorp7W3YJA7ftkc9A%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/f158ee0a96ed42ebacdbb50a38393eac?x-expires=1974358800&x-signature=ONzcigLJjVMFkzAlgkX6%2FdlXPeI%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/f158ee0a96ed42ebacdbb50a38393eac?x-expires=1974358800&x-signature=HrdENAIHS8wMwIlHV9TJouYmQN4%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "heiha.png",
    "display_name": "[嘿哈]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/7effd15261c44fe3acbb780aaae7d29e",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/7effd15261c44fe3acbb780aaae7d29e?x-expires=1974358800&x-signature=dCcCc8cnXAxK1Z0oEaaAFbIfo0s%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/7effd15261c44fe3acbb780aaae7d29e?x-expires=1974358800&x-signature=csD3vU0qxvVCagLHYdwVWkyzZHY%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/7effd15261c44fe3acbb780aaae7d29e?x-expires=1974358800&x-signature=niaXukSg2kYtd5Emm7NtoISguVA%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "jiahaoyou.png",
    "display_name": "[加好友]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/d81d449ac9464f76a08ad20e5afe8265",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/d81d449ac9464f76a08ad20e5afe8265?x-expires=1974358800&x-signature=477WlIUrcB0IKg8T641uIIxZ%2FSU%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/d81d449ac9464f76a08ad20e5afe8265?x-expires=1974358800&x-signature=PaCc6Ip2pHlGQK08BXTCLx69AQs%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/d81d449ac9464f76a08ad20e5afe8265?x-expires=1974358800&x-signature=5skL1xCUwN252OPuSz%2FdV31eFFg%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "jingkong.png",
    "display_name": "[惊恐]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/143eb85549774f90a0985c9a39ea586a",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/143eb85549774f90a0985c9a39ea586a?x-expires=1974358800&x-signature=AZxJkoiSaMTXKxLDRgPr%2B0LxxzU%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/143eb85549774f90a0985c9a39ea586a?x-expires=1974358800&x-signature=aNjbyCwX%2BtAyIJC7tIn4eZ6CK%2FY%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/143eb85549774f90a0985c9a39ea586a?x-expires=1974358800&x-signature=1SjQfXE4AMrs6aBUVfAnG8nudcA%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "jingya.png",
    "display_name": "[惊讶]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/2d7d707c90a3443cb1fed6d2039cc3db",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/2d7d707c90a3443cb1fed6d2039cc3db?x-expires=1974358800&x-signature=s725flgy%2FJ%2BrLegZk70vYBPSuqE%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/2d7d707c90a3443cb1fed6d2039cc3db?x-expires=1974358800&x-signature=3xhw3zq0eoXg3CDe0vZTBa2EzYI%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/2d7d707c90a3443cb1fed6d2039cc3db?x-expires=1974358800&x-signature=NZ5%2FJFzPkphqZcytiPG3Ph3D3Zw%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "jiong.png",
    "display_name": "[囧]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/38059ece9cc148b48f9084741bdb2fef",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/38059ece9cc148b48f9084741bdb2fef?x-expires=1974358800&x-signature=jrhM4bxyPJsi01lXHDCVw%2FzgsoU%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/38059ece9cc148b48f9084741bdb2fef?x-expires=1974358800&x-signature=9YchxbCS47g3sxZkDNJ52dGBXnM%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/38059ece9cc148b48f9084741bdb2fef?x-expires=1974358800&x-signature=82wHAMb0jLaWpqR3awsrZZNpxpo%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "nanguo.png",
    "display_name": "[难过]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/d4101a00edc74b0f958a9c8522896757",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/d4101a00edc74b0f958a9c8522896757?x-expires=1974358800&x-signature=XAofVDgPlKKcVQN0ZitNtGfo1s4%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/d4101a00edc74b0f958a9c8522896757?x-expires=1974358800&x-signature=r8seYhEk54r7qna0Ah2ltiY2jfo%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/d4101a00edc74b0f958a9c8522896757?x-expires=1974358800&x-signature=j4qnxG%2F0OwKFMu9sNC2HuAYtm6c%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "xieyan.png",
    "display_name": "[斜眼]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/8bf2131182a64be7b509173e5b0f4ea8",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/8bf2131182a64be7b509173e5b0f4ea8?x-expires=1974358800&x-signature=zun1DX34jkC7cwqO%2BPoDFX5s100%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/8bf2131182a64be7b509173e5b0f4ea8?x-expires=1974358800&x-signature=00Mqkob5K2AM44kkegT1koqpTAI%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/8bf2131182a64be7b509173e5b0f4ea8?x-expires=1974358800&x-signature=XMcwFyZlFKuLLgirkuhG2tWshFo%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "yinxian.png",
    "display_name": "[阴险]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/ece2ceab3cd04fbbb78dfcaf0e445aa9",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/ece2ceab3cd04fbbb78dfcaf0e445aa9?x-expires=1974358800&x-signature=hfOFaiJUrNRA34zmxE518Aza0Es%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/ece2ceab3cd04fbbb78dfcaf0e445aa9?x-expires=1974358800&x-signature=oifrlJeq49wV4ahJNtnpCo1Z4i8%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/ece2ceab3cd04fbbb78dfcaf0e445aa9?x-expires=1974358800&x-signature=yXHWywV52p%2FQyuErg1eQxTRlrI8%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "zuohengheng.png",
    "display_name": "[左哼哼]",
    "hide": 1,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/20ef3689f54b4da6af48c45086a375cb",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/20ef3689f54b4da6af48c45086a375cb?x-expires=1974358800&x-signature=TPPNl4SCuIroFCqJ3TNHqFeEZ64%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/20ef3689f54b4da6af48c45086a375cb?x-expires=1974358800&x-signature=76I1wfbjFEqwp%2BmabmERhUhf36E%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/20ef3689f54b4da6af48c45086a375cb?x-expires=1974358800&x-signature=8P51l0aa2H%2FQcM98ntC4S7%2BtiI8%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "youhengheng.png",
    "display_name": "[右哼哼]",
    "hide": 1,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/6c6284cdbc01433e9c96ab1822fb4228",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/6c6284cdbc01433e9c96ab1822fb4228?x-expires=1974358800&x-signature=RyxWmkvsTKIQhYqCYW%2FTB10A3cM%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/6c6284cdbc01433e9c96ab1822fb4228?x-expires=1974358800&x-signature=ZU9pnyn697U2w3srThJSh6QWPN8%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/6c6284cdbc01433e9c96ab1822fb4228?x-expires=1974358800&x-signature=sjbh3exhi9jr1XdW3sqyCMqOI6Y%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "youxian.png",
    "display_name": "[悠闲]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/ded935a2239a4c9cb41f3e78af6d01ee",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/ded935a2239a4c9cb41f3e78af6d01ee?x-expires=1974358800&x-signature=2nphdfK7dseDCFYYTuLuzfpmky4%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/ded935a2239a4c9cb41f3e78af6d01ee?x-expires=1974358800&x-signature=nYgxfxAjMhDDdtse8gkga6Yf%2BOQ%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/ded935a2239a4c9cb41f3e78af6d01ee?x-expires=1974358800&x-signature=bk1tXQNNqeZKzA0reSBiETXyUeA%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "zhouma.png",
    "display_name": "[咒骂]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/f582ecd398364c53beb51917e38a6e16",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/f582ecd398364c53beb51917e38a6e16?x-expires=1974358800&x-signature=oAEGAQyxkrjvpWmidv%2Bw91nc%2BMY%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/f582ecd398364c53beb51917e38a6e16?x-expires=1974358800&x-signature=VA7HqIbwRpYHzaeZHT2TXYeqhlg%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/f582ecd398364c53beb51917e38a6e16?x-expires=1974358800&x-signature=1HIbi08LB68RKB03Zl5kIrTzze0%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "bixin.png",
    "display_name": "[比心]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/de2c77ea756c4ce1aa4fc1a42018e67c",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/de2c77ea756c4ce1aa4fc1a42018e67c?x-expires=1974358800&x-signature=zClL13NM8syPpvSMx5438GCfGo8%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/de2c77ea756c4ce1aa4fc1a42018e67c?x-expires=1974358800&x-signature=6%2Bsa%2FjB8gKR27Svs2UY%2FBMfjMWY%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/de2c77ea756c4ce1aa4fc1a42018e67c?x-expires=1974358800&x-signature=lcZ7mgQ%2FBYzMSqQRK86pAm1txsI%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "jiayou.png",
    "display_name": "[强壮]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/88857d980b764c858d3145f8df7c6242",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/88857d980b764c858d3145f8df7c6242?x-expires=1974358800&x-signature=PgHTxF7RhFcLdEghtbEjctyLYkU%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/88857d980b764c858d3145f8df7c6242?x-expires=1974358800&x-signature=aPlLn7zRDzMbHiZU%2FDAkEtYxllk%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/88857d980b764c858d3145f8df7c6242?x-expires=1974358800&x-signature=JupMtcniS%2FTTIKCEhEBtWgXzT1o%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "jiayou.png",
    "display_name": "[加油]",
    "hide": 1,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/88857d980b764c858d3145f8df7c6242",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/88857d980b764c858d3145f8df7c6242?x-expires=1974358800&x-signature=PgHTxF7RhFcLdEghtbEjctyLYkU%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/88857d980b764c858d3145f8df7c6242?x-expires=1974358800&x-signature=aPlLn7zRDzMbHiZU%2FDAkEtYxllk%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/88857d980b764c858d3145f8df7c6242?x-expires=1974358800&x-signature=JupMtcniS%2FTTIKCEhEBtWgXzT1o%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "pengquan.png",
    "display_name": "[碰拳]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/ceb15bde869f49e6ae04278ac6b44f06",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/ceb15bde869f49e6ae04278ac6b44f06?x-expires=1974358800&x-signature=HcPB%2B1qHRCX7p8rYhw6sqRe1QQM%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/ceb15bde869f49e6ae04278ac6b44f06?x-expires=1974358800&x-signature=hQ%2BQLAQzqAQrd3pBcrfu0tKHwts%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/ceb15bde869f49e6ae04278ac6b44f06?x-expires=1974358800&x-signature=md%2BU094wa8EvPsIIu%2BLg5nqGcH4%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "ok.png",
    "display_name": "[OK]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/33f66f1c5f9d49b0a7c47a40731f3bef",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/33f66f1c5f9d49b0a7c47a40731f3bef?x-expires=1974358800&x-signature=pgV%2BeMEqBW%2FxTZtz8ExTwcbchXc%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/33f66f1c5f9d49b0a7c47a40731f3bef?x-expires=1974358800&x-signature=Intlxbaf6ITVeZO2J7bwmNTOJHQ%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/33f66f1c5f9d49b0a7c47a40731f3bef?x-expires=1974358800&x-signature=PkzEJ8UcNAtZ1GXHQuVCzk8yEBk%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "ok.png",
    "display_name": "[ok]",
    "hide": 1,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/33f66f1c5f9d49b0a7c47a40731f3bef",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/33f66f1c5f9d49b0a7c47a40731f3bef?x-expires=1974358800&x-signature=pgV%2BeMEqBW%2FxTZtz8ExTwcbchXc%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/33f66f1c5f9d49b0a7c47a40731f3bef?x-expires=1974358800&x-signature=Intlxbaf6ITVeZO2J7bwmNTOJHQ%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/33f66f1c5f9d49b0a7c47a40731f3bef?x-expires=1974358800&x-signature=PkzEJ8UcNAtZ1GXHQuVCzk8yEBk%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "jizhang.png",
    "display_name": "[击掌]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/d5799a7de3ab44da84a84c09d586a3f9",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/d5799a7de3ab44da84a84c09d586a3f9?x-expires=1974358800&x-signature=dyrVq%2BObat5dRuq1KbX4WA5dSqU%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/d5799a7de3ab44da84a84c09d586a3f9?x-expires=1974358800&x-signature=PcZWqHF5zkl1CV6SaC0F92Ga7Vk%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/d5799a7de3ab44da84a84c09d586a3f9?x-expires=1974358800&x-signature=Iv6WtDNm%2BNTnlChMePilsORoys0%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "zuoshang.png",
    "display_name": "[左上]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/4cdd2bf7d57a473d92e55bffce2b3ace",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/4cdd2bf7d57a473d92e55bffce2b3ace?x-expires=1974358800&x-signature=0n4GOnrq9Wb7M1hnuv12pcO64E0%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/4cdd2bf7d57a473d92e55bffce2b3ace?x-expires=1974358800&x-signature=YL0TuaTnuUO%2B6Bag%2BsImHL4kMuY%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/4cdd2bf7d57a473d92e55bffce2b3ace?x-expires=1974358800&x-signature=cKLsfWTcSf8Rq98PnOq3jxyU%2BR8%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "woshou.png",
    "display_name": "[握手]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/f878645e94224bdab3dba7c29b95cfef",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/f878645e94224bdab3dba7c29b95cfef?x-expires=1974358800&x-signature=3VdAh1jMdiBG%2Fp1kGGs34RoDIL0%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/f878645e94224bdab3dba7c29b95cfef?x-expires=1974358800&x-signature=5f0kITYpJW3GfYReJzEaDEm3skg%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/f878645e94224bdab3dba7c29b95cfef?x-expires=1974358800&x-signature=pqW4aQecVAxiNEHb9CGTGuh%2BgJs%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "baoquan.png",
    "display_name": "[抱拳]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/6fcf371a61854ebcb92f61e8cd418308",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/6fcf371a61854ebcb92f61e8cd418308?x-expires=1974358800&x-signature=%2Fk47IYzF2ekMFS%2BP%2F1JyClX38Ic%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/6fcf371a61854ebcb92f61e8cd418308?x-expires=1974358800&x-signature=WkmIDguOnOL7o2puqBNlHNBxIyE%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/6fcf371a61854ebcb92f61e8cd418308?x-expires=1974358800&x-signature=fVsygytkSKLtYf4OaHlQ%2BbxPZ6M%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "gouyin.png",
    "display_name": "[勾引]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/537812e5a1ca4f138245d01ef357a2cb",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/537812e5a1ca4f138245d01ef357a2cb?x-expires=1974358800&x-signature=zeQwmUJZi6P1KMqElddrMbDdmtQ%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/537812e5a1ca4f138245d01ef357a2cb?x-expires=1974358800&x-signature=pcU3YzLNOX7LKqyrh6gbUIqSC4I%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/537812e5a1ca4f138245d01ef357a2cb?x-expires=1974358800&x-signature=Uirvb9MA9LPRH%2FWAufBAssT0TAw%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "quantou.png",
    "display_name": "[拳头]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/794222aabfb34b01a24ebfb36a75c865",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/794222aabfb34b01a24ebfb36a75c865?x-expires=1974358800&x-signature=3bdHUc97xce%2FO704m6TY%2FvRl3vM%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/794222aabfb34b01a24ebfb36a75c865?x-expires=1974358800&x-signature=5FofsLfE%2BIbopp0DHTcNJXlj4z8%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/794222aabfb34b01a24ebfb36a75c865?x-expires=1974358800&x-signature=y6vaHVwppUTSMDhKXSTziLNx3mE%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "ruo.png",
    "display_name": "[弱]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/4d63a76416984ddbb9d9d6e69526ad0b",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/4d63a76416984ddbb9d9d6e69526ad0b?x-expires=1974358800&x-signature=ukVPp1EmIru6NTWek9NGVrwqW20%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/4d63a76416984ddbb9d9d6e69526ad0b?x-expires=1974358800&x-signature=tWtcb07jk%2FcURdeiRLX4bTRY4eo%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/4d63a76416984ddbb9d9d6e69526ad0b?x-expires=1974358800&x-signature=j3kpHh93U8jR68Bnd4jkGLJBJkc%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "shengli.png",
    "display_name": "[胜利]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/d9cf22f9a77347e5bb71510a1c81463c",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/d9cf22f9a77347e5bb71510a1c81463c?x-expires=1974358800&x-signature=P4ksTWXmqRg6HzXryDb4lPrPvc8%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/d9cf22f9a77347e5bb71510a1c81463c?x-expires=1974358800&x-signature=6RF1%2FE5Os08jXR7oD%2FaHnmBTCW8%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/d9cf22f9a77347e5bb71510a1c81463c?x-expires=1974358800&x-signature=x0aK0O5%2BMWyQ2gM1OAD3nZw9RPQ%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "youbian.png",
    "display_name": "[右边]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/90dc359454df494c954ae3f52985bcb5",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/90dc359454df494c954ae3f52985bcb5?x-expires=1974358800&x-signature=C%2BCh0GUrR1gnm66ZKQjfZJxn42k%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/90dc359454df494c954ae3f52985bcb5?x-expires=1974358800&x-signature=5jcTqO8hg7eFM4T%2Fc%2Fea8q2JKek%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/90dc359454df494c954ae3f52985bcb5?x-expires=1974358800&x-signature=bxdgnuCxCNBbTJikxFL9C5pW%2B9s%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "zuobian.png",
    "display_name": "[左边]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/1d6048a2f3d4433b845b29b28196ce95",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/1d6048a2f3d4433b845b29b28196ce95?x-expires=1974358800&x-signature=WTLQ3JoUgB%2Fx4st%2FW9kZKBzV0fk%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/1d6048a2f3d4433b845b29b28196ce95?x-expires=1974358800&x-signature=VVrDuGhte6H6UbaDgh7Dw7iUFLo%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/1d6048a2f3d4433b845b29b28196ce95?x-expires=1974358800&x-signature=RcvNLQJX4smYBRuvIvqcN2POM%2FY%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "kiss.png",
    "display_name": "[嘴唇]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/94ad7a2deb0843528a43967d84d4c287",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/94ad7a2deb0843528a43967d84d4c287?x-expires=1974358800&x-signature=wMV%2FdykixUwiFkjLQT3QshZZMbg%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/94ad7a2deb0843528a43967d84d4c287?x-expires=1974358800&x-signature=oNZ8rOMg1wFKV1M5pfuMmhH%2BNLs%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/94ad7a2deb0843528a43967d84d4c287?x-expires=1974358800&x-signature=veeIyyIIHWHnPPa01OdyQVFqnj4%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "kiss.png",
    "display_name": "[kiss]",
    "hide": 1,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/94ad7a2deb0843528a43967d84d4c287",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/94ad7a2deb0843528a43967d84d4c287?x-expires=1974358800&x-signature=wMV%2FdykixUwiFkjLQT3QshZZMbg%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/94ad7a2deb0843528a43967d84d4c287?x-expires=1974358800&x-signature=oNZ8rOMg1wFKV1M5pfuMmhH%2BNLs%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/94ad7a2deb0843528a43967d84d4c287?x-expires=1974358800&x-signature=veeIyyIIHWHnPPa01OdyQVFqnj4%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "xin.png",
    "display_name": "[爱心]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/cb3d395fc3bd430ea89d8706c5573d40",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/cb3d395fc3bd430ea89d8706c5573d40?x-expires=1974358800&x-signature=oRAfimDhaKV%2Bk0n%2B%2BsElVGzbLtQ%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/cb3d395fc3bd430ea89d8706c5573d40?x-expires=1974358800&x-signature=Car72F7DKSHs%2FsEYg4Kd4ICo%2FHc%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/cb3d395fc3bd430ea89d8706c5573d40?x-expires=1974358800&x-signature=9lORp5f5uH2krsribA6TzpKzc8Q%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "shangxin.png",
    "display_name": "[心碎]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/db9c54badfef440e9382df0853cf836c",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/db9c54badfef440e9382df0853cf836c?x-expires=1974358800&x-signature=VF64m%2B%2Bsz9jiAUVsi%2FVqCh3BjJE%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/db9c54badfef440e9382df0853cf836c?x-expires=1974358800&x-signature=ugFavSF3%2FlIJylEW2YeiiD5IV9c%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/db9c54badfef440e9382df0853cf836c?x-expires=1974358800&x-signature=PUUGeW8bgwOm8ycDFxqxZYVOI3o%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "meigui.png",
    "display_name": "[玫瑰]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/3ed256a052894a61b8ee3765d7150fcb",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/3ed256a052894a61b8ee3765d7150fcb?x-expires=1974358800&x-signature=NsgfojBciDPGHwjstrDLv1tDEoU%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/3ed256a052894a61b8ee3765d7150fcb?x-expires=1974358800&x-signature=yHCT%2BCaOrfL4BKrCtYcB1cRk0MY%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/3ed256a052894a61b8ee3765d7150fcb?x-expires=1974358800&x-signature=pzO%2FU1MZwvOFi%2BEmWuF%2BVS9v1gY%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "diaoxie.png",
    "display_name": "[凋谢]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/4fbccea05d61430e9cfafce554aacfbe",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/4fbccea05d61430e9cfafce554aacfbe?x-expires=1974358800&x-signature=O8rMVeL%2FDaef0kygQMy5SSpmIWM%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/4fbccea05d61430e9cfafce554aacfbe?x-expires=1974358800&x-signature=zNnAAVEn46J6z3CueRHAtS6sz2k%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/4fbccea05d61430e9cfafce554aacfbe?x-expires=1974358800&x-signature=mQ4yRGawkXzpuNfV4OfS1PoLKmE%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "pijiu.png",
    "display_name": "[啤酒]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/377a756273d74310acc017be0664d821",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/377a756273d74310acc017be0664d821?x-expires=1974358800&x-signature=o66F652mxZOEZS%2B8MmJPZ6OmP3U%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/377a756273d74310acc017be0664d821?x-expires=1974358800&x-signature=aKPAXlZGDIlVMwHytObC8kM60Uw%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/377a756273d74310acc017be0664d821?x-expires=1974358800&x-signature=hacsGmwcb8T7OY0%2FLU%2B5qHAj%2BoE%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "kafei.png",
    "display_name": "[咖啡]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/1ca8e1f39df74c80885d658ef67f3c5a",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/1ca8e1f39df74c80885d658ef67f3c5a?x-expires=1974358800&x-signature=J6kJpLUAH%2B6sChBPbSPmoKFvhTg%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/1ca8e1f39df74c80885d658ef67f3c5a?x-expires=1974358800&x-signature=0TvJERRherl2GgkcXkHyjuKYMR0%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/1ca8e1f39df74c80885d658ef67f3c5a?x-expires=1974358800&x-signature=%2Bs3Ut2z06H64rL33cXqQ5SxGWIY%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "dangao.png",
    "display_name": "[蛋糕]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/9acebd62cdc44941aeac8a3503ebb6c4",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/9acebd62cdc44941aeac8a3503ebb6c4?x-expires=1974358800&x-signature=mg7lA9KHO53L8kDOEm4m9xgXqms%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/9acebd62cdc44941aeac8a3503ebb6c4?x-expires=1974358800&x-signature=xl9Htt8S6Dz1WL7DHSlweYYoGbw%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/9acebd62cdc44941aeac8a3503ebb6c4?x-expires=1974358800&x-signature=3UVJ6tF%2FobK3%2FQLlNmgRuLOtABo%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "liwu.png",
    "display_name": "[礼物]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/01a34fbd080a41678875d92303151336",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/01a34fbd080a41678875d92303151336?x-expires=1974358800&x-signature=Hk94PaLV2XdTg28EVLK%2B4HiCImE%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/01a34fbd080a41678875d92303151336?x-expires=1974358800&x-signature=Pr%2FdPvgQ18A9%2BkkamAY87JahEtk%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/01a34fbd080a41678875d92303151336?x-expires=1974358800&x-signature=Wr5N6dvgzEjIf8wbLZA0%2Bu4IxSo%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "sahua.png",
    "display_name": "[撒花]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/0f481b14cb254132b94142b04de3ca8a",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/0f481b14cb254132b94142b04de3ca8a?x-expires=1974358800&x-signature=%2FvMmHe8Bb01xYTYfVjq7MhHIq2s%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/0f481b14cb254132b94142b04de3ca8a?x-expires=1974358800&x-signature=pHEUda0FBkR9ddK9Q99e6RAWTqs%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/0f481b14cb254132b94142b04de3ca8a?x-expires=1974358800&x-signature=ExYbam2sQNolC2W%2F7UEtXftrVHs%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "V5.png",
    "display_name": "[V5]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/67335cffe2d449cda8c53802ac3e7918",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/67335cffe2d449cda8c53802ac3e7918?x-expires=1974358800&x-signature=gCFIive9sMOqWS5CCV7Wy5xPkIM%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/67335cffe2d449cda8c53802ac3e7918?x-expires=1974358800&x-signature=cCidio7nXX2vcDMJoMPsDWdnLnM%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/67335cffe2d449cda8c53802ac3e7918?x-expires=1974358800&x-signature=xUBvdTM65LrbrOHnyPpKpjC%2Fs0c%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "jue.png",
    "display_name": "[绝]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/67cbcdd341ed4b12a644bccaa2509dc7",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/67cbcdd341ed4b12a644bccaa2509dc7?x-expires=1974358800&x-signature=ovwwkuoQWhYmzwrD72NHYasmyac%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/67cbcdd341ed4b12a644bccaa2509dc7?x-expires=1974358800&x-signature=6L8Svay2PPWOVDjQhSA8XPrlckQ%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/67cbcdd341ed4b12a644bccaa2509dc7?x-expires=1974358800&x-signature=WOvjm7bLsVTUvqX8YqOfS4MS8L0%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "666.png",
    "display_name": "[666]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/382cee67ff9d4b438b4a78b327508943",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/382cee67ff9d4b438b4a78b327508943?x-expires=1974358800&x-signature=t6gU0RFW1JxcthGW%2B7Q9OaY7PF8%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/382cee67ff9d4b438b4a78b327508943?x-expires=1974358800&x-signature=ngUprZEh5VNFHBGCT1apQRVZccU%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/382cee67ff9d4b438b4a78b327508943?x-expires=1974358800&x-signature=eqyktmyzDKB2IjKcjvUYJAo9HyQ%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "geili.png",
    "display_name": "[给力]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/cefb9503252245458a44645656cb0d1d",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/cefb9503252245458a44645656cb0d1d?x-expires=1974358800&x-signature=4A8%2B8I0XfnO4E8x7lCvPkNU%2FqQM%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/cefb9503252245458a44645656cb0d1d?x-expires=1974358800&x-signature=EuAnie92bIxNppkWIGvK3MPQQzY%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/cefb9503252245458a44645656cb0d1d?x-expires=1974358800&x-signature=D3foVqFGrBMHrP0WymABpuc0T4s%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "hongbao.png",
    "display_name": "[红包]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/8011acf85e4047e4b0aab61ff792c121",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/8011acf85e4047e4b0aab61ff792c121?x-expires=1974358800&x-signature=OMjyLuYxQHRPxBaX%2FCnwM3IEKO8%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/8011acf85e4047e4b0aab61ff792c121?x-expires=1974358800&x-signature=fBAMWsGEpfLX5JFGd1%2FI6qNOFkQ%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/8011acf85e4047e4b0aab61ff792c121?x-expires=1974358800&x-signature=mz6L3ec%2BQAl4axnvdxXwlHnIdK4%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "shi.png",
    "display_name": "[屎]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/f1ae02bb68eb4816aec245c27b4808d5",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/f1ae02bb68eb4816aec245c27b4808d5?x-expires=1974358800&x-signature=gpbKu5nHXFyxFXfZkUutv94xUCE%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/f1ae02bb68eb4816aec245c27b4808d5?x-expires=1974358800&x-signature=rYmTezL8JPwmbbaDH%2BPILiXU92I%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/f1ae02bb68eb4816aec245c27b4808d5?x-expires=1974358800&x-signature=HxMT83Sm%2BFM3RvJMpttqT%2F0mZoQ%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "fa.png",
    "display_name": "[发]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/4c94f2c5f1ce4b15b3b41a3d83412f3c",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/4c94f2c5f1ce4b15b3b41a3d83412f3c?x-expires=1974358800&x-signature=UtqOHT5LdvDv1VsAZYUtzVmbnG0%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/4c94f2c5f1ce4b15b3b41a3d83412f3c?x-expires=1974358800&x-signature=NJR98LA8%2FHGtWu3wdvYZj%2BqdkRM%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/4c94f2c5f1ce4b15b3b41a3d83412f3c?x-expires=1974358800&x-signature=o6mYE8B2mSNU%2FluNPvHK7HFoYKA%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "wotainanle.png",
    "display_name": "[我太难了]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/af6417d03e1c454dab1c89fcc7f1a13e",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/af6417d03e1c454dab1c89fcc7f1a13e?x-expires=1974358800&x-signature=8GnQ8CPwXeMD3584ied4GRcjBxw%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/af6417d03e1c454dab1c89fcc7f1a13e?x-expires=1974358800&x-signature=b3iiN0zGdGqUu4dxTmePLl5Gs6Q%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/af6417d03e1c454dab1c89fcc7f1a13e?x-expires=1974358800&x-signature=HXBlTW%2FIjIeZcE3cnmn03yBs9Vs%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "18jin.png",
    "display_name": "[18禁]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/909f66957e364e11be8f8b1c430cfacc",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/909f66957e364e11be8f8b1c430cfacc?x-expires=1974358800&x-signature=RPZuXZYJj1xJNvdZb%2F3A2jHv4Fk%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/909f66957e364e11be8f8b1c430cfacc?x-expires=1974358800&x-signature=q1Au7Jjn2kzlsUcsPXgFTqkYv4Y%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/909f66957e364e11be8f8b1c430cfacc?x-expires=1974358800&x-signature=61HFaICkU4YoLrMswhDQRCbrI%2FE%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "zhadan.png",
    "display_name": "[炸弹]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/232a360e86044f9b8f137f47f8ec2e30",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/232a360e86044f9b8f137f47f8ec2e30?x-expires=1974358800&x-signature=wW%2Fy9obVPQgMvJhmYrD8tmuIpB0%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/232a360e86044f9b8f137f47f8ec2e30?x-expires=1974358800&x-signature=VJCbUlw%2F%2B%2BH3qwQpkV1B6PWP3ZA%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/232a360e86044f9b8f137f47f8ec2e30?x-expires=1974358800&x-signature=4dd0%2BdGXIMgv0xRLRhOpgZC%2B3GQ%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "quwufen.png",
    "display_name": "[去污粉]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/624c8b331d884841ab091db12903efca",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/624c8b331d884841ab091db12903efca?x-expires=1974358800&x-signature=huYZPennc%2B049Sum4TEXecF6XV0%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/624c8b331d884841ab091db12903efca?x-expires=1974358800&x-signature=9iD57IcUJG%2FoKkqmW8mXtP46yGM%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/624c8b331d884841ab091db12903efca?x-expires=1974358800&x-signature=z%2BAjYszTnj8RvA07SgrENcOxNKA%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "xigua.png",
    "display_name": "[西瓜]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/ee08d8cd500643958eded3080c006fd3",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/ee08d8cd500643958eded3080c006fd3?x-expires=1974358800&x-signature=oHf5qHrLh%2FrZRHIqNnanTW0LD7A%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/ee08d8cd500643958eded3080c006fd3?x-expires=1974358800&x-signature=5MHOPVegA3Zm6jqQy%2Fi4lIdTk%2FY%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/ee08d8cd500643958eded3080c006fd3?x-expires=1974358800&x-signature=1iCNYp5jBPntb30anTRGEMjK0uM%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "dao.png",
    "display_name": "[菜刀]",
    "hide": 1,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/86f2bf3d8d3043a3ac40d6b1784b2e34",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/86f2bf3d8d3043a3ac40d6b1784b2e34?x-expires=1974358800&x-signature=Ad1gqZ4Wdo6bgCoegyib4NSYybY%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/86f2bf3d8d3043a3ac40d6b1784b2e34?x-expires=1974358800&x-signature=Lq4VRyYe4dEFoJyxjUNHMEBzWFw%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/86f2bf3d8d3043a3ac40d6b1784b2e34?x-expires=1974358800&x-signature=B5kPU4ta1dSHuNUMe1cwnmp5EkI%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "dao.png",
    "display_name": "[刀]",
    "hide": 1,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/86f2bf3d8d3043a3ac40d6b1784b2e34",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/86f2bf3d8d3043a3ac40d6b1784b2e34?x-expires=1974358800&x-signature=Ad1gqZ4Wdo6bgCoegyib4NSYybY%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/86f2bf3d8d3043a3ac40d6b1784b2e34?x-expires=1974358800&x-signature=Lq4VRyYe4dEFoJyxjUNHMEBzWFw%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/86f2bf3d8d3043a3ac40d6b1784b2e34?x-expires=1974358800&x-signature=B5kPU4ta1dSHuNUMe1cwnmp5EkI%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "xin.png",
    "display_name": "[心]",
    "hide": 1,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/cb3d395fc3bd430ea89d8706c5573d40",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/cb3d395fc3bd430ea89d8706c5573d40?x-expires=1974358800&x-signature=oRAfimDhaKV%2Bk0n%2B%2BsElVGzbLtQ%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/cb3d395fc3bd430ea89d8706c5573d40?x-expires=1974358800&x-signature=Car72F7DKSHs%2FsEYg4Kd4ICo%2FHc%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/cb3d395fc3bd430ea89d8706c5573d40?x-expires=1974358800&x-signature=9lORp5f5uH2krsribA6TzpKzc8Q%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "shangxin.png",
    "display_name": "[伤心]",
    "hide": 1,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/db9c54badfef440e9382df0853cf836c",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/db9c54badfef440e9382df0853cf836c?x-expires=1974358800&x-signature=VF64m%2B%2Bsz9jiAUVsi%2FVqCh3BjJE%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/db9c54badfef440e9382df0853cf836c?x-expires=1974358800&x-signature=ugFavSF3%2FlIJylEW2YeiiD5IV9c%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/db9c54badfef440e9382df0853cf836c?x-expires=1974358800&x-signature=PUUGeW8bgwOm8ycDFxqxZYVOI3o%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "shi.png",
    "display_name": "[便便]",
    "hide": 1,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/f1ae02bb68eb4816aec245c27b4808d5",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/f1ae02bb68eb4816aec245c27b4808d5?x-expires=1974358800&x-signature=gpbKu5nHXFyxFXfZkUutv94xUCE%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/f1ae02bb68eb4816aec245c27b4808d5?x-expires=1974358800&x-signature=rYmTezL8JPwmbbaDH%2BPILiXU92I%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/f1ae02bb68eb4816aec245c27b4808d5?x-expires=1974358800&x-signature=HxMT83Sm%2BFM3RvJMpttqT%2F0mZoQ%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "jiajitui.png",
    "display_name": "[加鸡腿]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/1f06d9a525b24f27844463e7a9bc350c",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/1f06d9a525b24f27844463e7a9bc350c?x-expires=1974358800&x-signature=JPB1ZGnU0RhdqNhQPqrWHU3yBM8%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/1f06d9a525b24f27844463e7a9bc350c?x-expires=1974358800&x-signature=iPlW0XbAxNsTx2Z%2B7YsUu0GXfDE%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/1f06d9a525b24f27844463e7a9bc350c?x-expires=1974358800&x-signature=jGIS26BaettkEtt5v9g%2FOfCHJKs%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "wosuanle.png",
    "display_name": "[我酸了]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/02e463152ad64400b90eab83bf687382",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/02e463152ad64400b90eab83bf687382?x-expires=1974358800&x-signature=Msy8WoNDeniforh5MtcuQ7b%2B%2Ba8%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/02e463152ad64400b90eab83bf687382?x-expires=1974358800&x-signature=vLomkZt2VdPISFosyaSU7uVIBWw%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/02e463152ad64400b90eab83bf687382?x-expires=1974358800&x-signature=hGa1fFFzByDmx212z8xkQlm45fM%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "wozhua.png",
    "display_name": "[握爪]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/2df33eea9459409e95e3d379f8fb3fd2",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/2df33eea9459409e95e3d379f8fb3fd2?x-expires=1974358800&x-signature=yA3hE%2FVaXTU39uMDwWwa7s6J7O0%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/2df33eea9459409e95e3d379f8fb3fd2?x-expires=1974358800&x-signature=6Ko6TXcV%2BCfN4ltGtnoCyD76OBQ%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/2df33eea9459409e95e3d379f8fb3fd2?x-expires=1974358800&x-signature=217M3lDOyTbfyaP8%2FDYIGhiIVlU%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "taiyang.png",
    "display_name": "[太阳]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/5cf8deb02740409db456567c0b100a7c",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/5cf8deb02740409db456567c0b100a7c?x-expires=1974358800&x-signature=zEnRKjxgTsKJSZY6NNsHA8tyKXc%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/5cf8deb02740409db456567c0b100a7c?x-expires=1974358800&x-signature=LE3aLE0bZupRT6FEhzTJGRV%2B8Jk%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/5cf8deb02740409db456567c0b100a7c?x-expires=1974358800&x-signature=8cU1LGi1NdCKdKG25xxTIo3Z4xI%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "yueliang.png",
    "display_name": "[月亮]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/d40758147185446aa4bf044bdc418ccf",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/d40758147185446aa4bf044bdc418ccf?x-expires=1974358800&x-signature=6Sz2rnWQaPWQ2HzCTk4ghPOCNho%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/d40758147185446aa4bf044bdc418ccf?x-expires=1974358800&x-signature=lYEBPcAk3ld34iXOfMC%2BqdxOc%2FY%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/d40758147185446aa4bf044bdc418ccf?x-expires=1974358800&x-signature=NLAZc1W7KC7JTxi33zVTbawVGQU%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "geiguile.png",
    "display_name": "[给跪了]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/d3817036fe084a0ba4461f91c06da126",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/d3817036fe084a0ba4461f91c06da126?x-expires=1974358800&x-signature=0b0IOEG4ayHz3MYqehTyBRH3%2FSU%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/d3817036fe084a0ba4461f91c06da126?x-expires=1974358800&x-signature=Ck1A35USeCJ0Omq3Q1UGeT30DZI%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/d3817036fe084a0ba4461f91c06da126?x-expires=1974358800&x-signature=AEidxCYuaPnlXuuDcPNyBh%2BwfaM%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "jiaolv.png",
    "display_name": "[蕉绿]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/34809d673a954033ab98499d30e6b4c9",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/34809d673a954033ab98499d30e6b4c9?x-expires=1974358800&x-signature=tRFuTyaEleHxZaNlowrUHTCyRGU%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/34809d673a954033ab98499d30e6b4c9?x-expires=1974358800&x-signature=cVMLW1SdSq%2FqK4%2FXcvrPiRaR6qQ%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/34809d673a954033ab98499d30e6b4c9?x-expires=1974358800&x-signature=5TSYRTF7ARrFY%2B%2B47bvVEP3nBOE%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "zhaxin.png",
    "display_name": "[扎心]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/a1d5323d258142d1b84c651d85670346",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/a1d5323d258142d1b84c651d85670346?x-expires=1974358800&x-signature=didBDeN4Xi4DlZDcS27VoXZkHRE%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/a1d5323d258142d1b84c651d85670346?x-expires=1974358800&x-signature=rYPF0mkfjj4S1rpyqL%2BwyrNfcQM%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/a1d5323d258142d1b84c651d85670346?x-expires=1974358800&x-signature=sG4voghlxWDWOtykgTBdczuIiW4%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "hugua.png",
    "display_name": "[胡瓜]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/cf013a583ce24dd09520e9f54fa61144",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/cf013a583ce24dd09520e9f54fa61144?x-expires=1974358800&x-signature=lsDH3e%2Bq%2Bi4gb%2FYGIg%2BnsO8vrlo%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/cf013a583ce24dd09520e9f54fa61144?x-expires=1974358800&x-signature=Wqd%2FWBBtcqB%2F5ebWh3pHSNNj1VA%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/cf013a583ce24dd09520e9f54fa61144?x-expires=1974358800&x-signature=sYRQuNsLd1M30IAdxbrh%2B9UsXiU%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "yyds.png",
    "display_name": "[yyds]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/6ab372988191438b8313968b82fa5fb6",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/6ab372988191438b8313968b82fa5fb6?x-expires=1974358800&x-signature=S6nL4ck1Oh4AQV06nrJqGnXNfoQ%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/6ab372988191438b8313968b82fa5fb6?x-expires=1974358800&x-signature=ZCNp0r5x5Zqwh%2Bvs5aay4l%2BIOjQ%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/6ab372988191438b8313968b82fa5fb6?x-expires=1974358800&x-signature=m4oPriH9LSBxHz0j0VLwhhld6jk%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "emo.png",
    "display_name": "[emo]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/0cb6123fca8d4a609fb05bc0d5c91801",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/0cb6123fca8d4a609fb05bc0d5c91801?x-expires=1974358800&x-signature=ypsqORDob7QbZLdWN5DN19ZGE5Q%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/0cb6123fca8d4a609fb05bc0d5c91801?x-expires=1974358800&x-signature=0qhvfxF%2B3LtRBOgAZXJsOFzGVXk%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/0cb6123fca8d4a609fb05bc0d5c91801?x-expires=1974358800&x-signature=HWtanmMdIXs%2BlwFhzDj2Nj4r8nA%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "dacall.png",
    "display_name": "[打call]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/39823d72edbf484aa3126773bad7c0ba",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/39823d72edbf484aa3126773bad7c0ba?x-expires=1974358800&x-signature=8u9yVb7lK2kXu%2FBJWq1kPIHzLUA%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/39823d72edbf484aa3126773bad7c0ba?x-expires=1974358800&x-signature=E%2BAcULt4nxYQp71NQVe%2FNCL0h78%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/39823d72edbf484aa3126773bad7c0ba?x-expires=1974358800&x-signature=MqRSz0KEulGW0ePoHripdLvp5GU%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "shuanq.png",
    "display_name": "[栓Q]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/1f0e745af7b14d7b883a8e5f354863ef",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/1f0e745af7b14d7b883a8e5f354863ef?x-expires=1974358800&x-signature=qR0eFJpyycIaD8AVw4KAxXYu%2FO4%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/1f0e745af7b14d7b883a8e5f354863ef?x-expires=1974358800&x-signature=q9lCPeoA81Hn8WhB204Zvz3lWu8%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/1f0e745af7b14d7b883a8e5f354863ef?x-expires=1974358800&x-signature=Vx48IeHR%2F2JXFZLW9lMfD0y24h4%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "wuyu.png",
    "display_name": "[无语]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/d4b3b21fb1674f13a1441f967258043e",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/d4b3b21fb1674f13a1441f967258043e?x-expires=1974358800&x-signature=mmVVNSa8gl4ILzH9KBlESl6E%2FpI%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/d4b3b21fb1674f13a1441f967258043e?x-expires=1974358800&x-signature=7Hep3oze05fWG8vPV2G5QHgo7pc%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/d4b3b21fb1674f13a1441f967258043e?x-expires=1974358800&x-signature=CQQeIcG33QQ%2FbOqN%2FCG8puYk3Rs%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "xueren.png",
    "display_name": "[雪人]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/fddd43d67b594268a02d29919e02b557",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/fddd43d67b594268a02d29919e02b557?x-expires=1974358800&x-signature=2UlsBLmxUwNj8cUbqQeax5CzdV8%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/fddd43d67b594268a02d29919e02b557?x-expires=1974358800&x-signature=%2FHM3EN%2F1CQJZiIRvIOvV2La8wNQ%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/fddd43d67b594268a02d29919e02b557?x-expires=1974358800&x-signature=uwxd81SC5r3XNUTamqs0RKppIiY%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "xuehua.png",
    "display_name": "[雪花]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/069dc227b2b745f7a17ad3c80da6e47d",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/069dc227b2b745f7a17ad3c80da6e47d?x-expires=1974358800&x-signature=ijg2B%2FqfgY7kEBYilJlkDN8vl7M%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/069dc227b2b745f7a17ad3c80da6e47d?x-expires=1974358800&x-signature=UZ24E7ULqcBkOb2CVhBzYtKrs8s%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/069dc227b2b745f7a17ad3c80da6e47d?x-expires=1974358800&x-signature=k5udhtbucgxM9pljncS6%2Frw%2BJ3A%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "shengdanshu.png",
    "display_name": "[圣诞树]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/fa82f66cde504091b82039ab8c790403",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/fa82f66cde504091b82039ab8c790403?x-expires=1974358800&x-signature=61blfs1Y%2F5ui58YbUg6jNtIXAVs%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/fa82f66cde504091b82039ab8c790403?x-expires=1974358800&x-signature=cNtw35RLN%2F2cyt1bEfy8MbfbwwY%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/fa82f66cde504091b82039ab8c790403?x-expires=1974358800&x-signature=N6UKGVNqGLUMYfW3%2BofQHXsGoSQ%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "pinganguo.png",
    "display_name": "[平安果]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/dee980b21d7b435495881e9ea13701cc",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/dee980b21d7b435495881e9ea13701cc?x-expires=1974358800&x-signature=ZMYEkLGPJDHLJP66RQR32oywPQU%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/dee980b21d7b435495881e9ea13701cc?x-expires=1974358800&x-signature=v0QH%2FVYAEB4AkWnVQfTqDEBl8Eg%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/dee980b21d7b435495881e9ea13701cc?x-expires=1974358800&x-signature=XhIO1zFSoYU1QGKRsJQkq8BVV2M%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "shengdanmao.png",
    "display_name": "[圣诞帽]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/35191825b27b49eda8071600fa716584",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/35191825b27b49eda8071600fa716584?x-expires=1974358800&x-signature=j1r1edcJiMsrtCJIoCv9BW%2BQYCU%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/35191825b27b49eda8071600fa716584?x-expires=1974358800&x-signature=HyChPUqLhUQ5i5hda4ye5V9Y%2FVw%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/35191825b27b49eda8071600fa716584?x-expires=1974358800&x-signature=UOc1FxtFE8Vtq98r6hPKw6oov%2BM%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "qiqiu.png",
    "display_name": "[气球]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/9417d24dc5ef4448a31d1265464c770d",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/9417d24dc5ef4448a31d1265464c770d?x-expires=1974358800&x-signature=AuNz88PCp0OQlOlvxPtqSKsGzN0%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/9417d24dc5ef4448a31d1265464c770d?x-expires=1974358800&x-signature=sZd0EwoVoGKsIB1CcosUGd6gdPQ%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/9417d24dc5ef4448a31d1265464c770d?x-expires=1974358800&x-signature=JA%2FaD9jHW01YscR2nCmbomCc4VY%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "ganbei.png",
    "display_name": "[干杯]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/b20416869c93422a8dd6d14625bcbc3d",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/b20416869c93422a8dd6d14625bcbc3d?x-expires=1974358800&x-signature=ohGc7mZlG5C%2Fo20cIBHW%2B2qlmrE%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/b20416869c93422a8dd6d14625bcbc3d?x-expires=1974358800&x-signature=O%2FyeCIloAoUFQ%2BhaMVAoBHBGFwc%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/b20416869c93422a8dd6d14625bcbc3d?x-expires=1974358800&x-signature=JURlPxXooUSAAD6JVdZp%2FaBaCEQ%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "yanhua.png",
    "display_name": "[烟花]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/4a44c7f50bd047ffb004440ed94fb627",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/4a44c7f50bd047ffb004440ed94fb627?x-expires=1974358800&x-signature=yzhVcmcau3%2BfGB2cdwtFJGD4fHM%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/4a44c7f50bd047ffb004440ed94fb627?x-expires=1974358800&x-signature=XYmethhw2RJpSV9xP7NLwAo9vGw%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/4a44c7f50bd047ffb004440ed94fb627?x-expires=1974358800&x-signature=brMxguuQ%2BTSqRVxW5I%2BVK01H4YA%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "fu.png",
    "display_name": "[福]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/b6266d9ab119497c90370b3301b576b5",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/b6266d9ab119497c90370b3301b576b5?x-expires=1974358800&x-signature=VtUHij3q2J8ricmqe57X6J8BcB4%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/b6266d9ab119497c90370b3301b576b5?x-expires=1974358800&x-signature=FWA6i37aQdbXB3m1uDCToAALsG8%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/b6266d9ab119497c90370b3301b576b5?x-expires=1974358800&x-signature=UOrurJeHUX737srppTctyRryJ3E%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "candy.png",
    "display_name": "[candy]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/1b28167e8d8543148d36448e2f78b5c7",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/1b28167e8d8543148d36448e2f78b5c7?x-expires=1974358800&x-signature=X%2BV%2FNvPYA6bCzibWxJ2%2BnocbOXI%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/1b28167e8d8543148d36448e2f78b5c7?x-expires=1974358800&x-signature=HOgbBXYBAozXIWUdAhQvEqmk%2Bz0%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/1b28167e8d8543148d36448e2f78b5c7?x-expires=1974358800&x-signature=TWI8uj1%2Bzi6ojPqtW3ARwyHjeg0%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "tanghulu.png",
    "display_name": "[糖葫芦]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/5be2a42b76a54d2f820415186ca8a53f",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/5be2a42b76a54d2f820415186ca8a53f?x-expires=1974358800&x-signature=vnqiaMgNNcZVsN%2Faf1sCYHd9vY4%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/5be2a42b76a54d2f820415186ca8a53f?x-expires=1974358800&x-signature=m3ayxy%2FTvrIQ6Ow9fXE8bSNXK%2BQ%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/5be2a42b76a54d2f820415186ca8a53f?x-expires=1974358800&x-signature=g9u%2BAFwf3tNsGjIwA%2BPe4lVGbt4%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "hutou.png",
    "display_name": "[虎头]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/51b127ce6db84e4ab9c32b8be7e6693e",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/51b127ce6db84e4ab9c32b8be7e6693e?x-expires=1974358800&x-signature=eKuclE7ObNsIOfwRtnVSgLcfJDo%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/51b127ce6db84e4ab9c32b8be7e6693e?x-expires=1974358800&x-signature=IPOZnk%2FXcO7s9pmZWgK9m9Q0MKs%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/51b127ce6db84e4ab9c32b8be7e6693e?x-expires=1974358800&x-signature=91sppZ2PppqEL%2BIdX5fmLxUtwCg%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "jiaozi.png",
    "display_name": "[饺子]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/6398e6e84fc0474dbe5186f6b2dca9d5",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/6398e6e84fc0474dbe5186f6b2dca9d5?x-expires=1974358800&x-signature=pjPUoa7E7hyc3mnNjlf5WXNOBKA%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/6398e6e84fc0474dbe5186f6b2dca9d5?x-expires=1974358800&x-signature=C8JrS827wKo9ikOyDTyuvv8p5%2F8%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/6398e6e84fc0474dbe5186f6b2dca9d5?x-expires=1974358800&x-signature=vocWpMqlkWtHI%2Bc9IVk1asK9rN8%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "bianpao.png",
    "display_name": "[鞭炮]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/203e34194907476882b3b79480319a1c",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/203e34194907476882b3b79480319a1c?x-expires=1974358800&x-signature=XwBWAaO4sGuzTF0tITHVXL0JaJ8%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/203e34194907476882b3b79480319a1c?x-expires=1974358800&x-signature=fjQzoW3yq%2Frj5Yybr%2F89YJLh7pI%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/203e34194907476882b3b79480319a1c?x-expires=1974358800&x-signature=9TzGkxVpQggd3GaVvIwN9yg4ZGc%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "yuanbao.png",
    "display_name": "[元宝]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/e87e835aee534a3eac278f3a3e91a799",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/e87e835aee534a3eac278f3a3e91a799?x-expires=1974358800&x-signature=cQKAHur0q30HxUq33W5Aj27opag%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/e87e835aee534a3eac278f3a3e91a799?x-expires=1974358800&x-signature=p8tkekzB7p%2Feane5tvRqWms%2FjTc%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/e87e835aee534a3eac278f3a3e91a799?x-expires=1974358800&x-signature=7utA807m0NWFHyYrzqiYrtCfSEw%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "denglong.png",
    "display_name": "[灯笼]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/5fe1118c3af84a0a93fe5f9f4af98d06",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/5fe1118c3af84a0a93fe5f9f4af98d06?x-expires=1974358800&x-signature=Q%2Fu%2FcxxxNXJCEEcxfGMw8BtKQSY%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/5fe1118c3af84a0a93fe5f9f4af98d06?x-expires=1974358800&x-signature=bbpmGqD9s3l%2B9b53Apl%2BfvduHd8%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/5fe1118c3af84a0a93fe5f9f4af98d06?x-expires=1974358800&x-signature=6xy%2Fw8BtAoGeYj7L7ykdDfVK45o%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "jinli.png",
    "display_name": "[锦鲤]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/6c6eb29de934482cabd2172c9e304eba",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/6c6eb29de934482cabd2172c9e304eba?x-expires=1974358800&x-signature=jxa9Zt9cF9dm%2F8IB%2F4UxiHQhC00%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/6c6eb29de934482cabd2172c9e304eba?x-expires=1974358800&x-signature=xIJXxJPiycD5%2FMOkh6gvcxFvPY0%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/6c6eb29de934482cabd2172c9e304eba?x-expires=1974358800&x-signature=l8laWQHfi0jZY%2FiPvN1V64v3rnU%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "qiaokeli.png",
    "display_name": "[巧克力]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/269a4612f3704ff99f0bb9d8c95c6611",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/269a4612f3704ff99f0bb9d8c95c6611?x-expires=1974358800&x-signature=Aqx6ygMv2T%2FteFd9IHythSotKDk%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/269a4612f3704ff99f0bb9d8c95c6611?x-expires=1974358800&x-signature=3HirwsmBgKWeJc8l5WA8wD0Mxd8%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/269a4612f3704ff99f0bb9d8c95c6611?x-expires=1974358800&x-signature=Eqj%2BGsncbeX0kzvJxgEFmnqmQ%2BE%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "tangyuan.png",
    "display_name": "[汤圆]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/fb6cd81414cd4fb69586081c75abfc3a",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/fb6cd81414cd4fb69586081c75abfc3a?x-expires=1974358800&x-signature=8mxLcUYqs7FU3hROIR92zV0WsZ4%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/fb6cd81414cd4fb69586081c75abfc3a?x-expires=1974358800&x-signature=4UqBzGTolFT9kFB0ZjEqa42ZwWg%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/fb6cd81414cd4fb69586081c75abfc3a?x-expires=1974358800&x-signature=ErM2hAlvSl5vxfanL2%2BBnTkQW%2Bw%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "qingshu.png",
    "display_name": "[情书]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/d27bad0daec74a4db186cdd6f8b76957",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/d27bad0daec74a4db186cdd6f8b76957?x-expires=1974358800&x-signature=h4fl8zZDVZgjiw6EgDmG9U80abc%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/d27bad0daec74a4db186cdd6f8b76957?x-expires=1974358800&x-signature=rwej2CrkKtEKRUe74D45kRj%2Bdt0%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/d27bad0daec74a4db186cdd6f8b76957?x-expires=1974358800&x-signature=2%2FxSZbsoWCEc0v1frBCL9r26NP4%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "iloveyou.png",
    "display_name": "[iloveyou]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/ef592117a4524e1b8c8cffd831ca8778",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/ef592117a4524e1b8c8cffd831ca8778?x-expires=1974358800&x-signature=L2xUzBwXKaBH6z1tq0hC0xTVzzM%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/ef592117a4524e1b8c8cffd831ca8778?x-expires=1974358800&x-signature=l4S%2Fs3OTf6d5wqyGT9643Nzzl3I%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/ef592117a4524e1b8c8cffd831ca8778?x-expires=1974358800&x-signature=IUdU95%2Fozm8woOVudikPy%2FXr4eM%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "jiezhi.png",
    "display_name": "[戒指]",
    "hide": 0,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/b24c567eeba040cfbb1386cb7e75f617",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/b24c567eeba040cfbb1386cb7e75f617?x-expires=1974358800&x-signature=YDkTh%2B%2FqOvEGJmjT9PFnHR%2BMtjU%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/b24c567eeba040cfbb1386cb7e75f617?x-expires=1974358800&x-signature=jxTkykQ9DYDD3PVUdwYVa7Nt%2BZk%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/b24c567eeba040cfbb1386cb7e75f617?x-expires=1974358800&x-signature=f4EQuIERcYG7OUIQJPhLn9H80sk%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "sahua.png",
    "display_name": "[派对]",
    "hide": 1,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/0f481b14cb254132b94142b04de3ca8a",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/0f481b14cb254132b94142b04de3ca8a?x-expires=1974358800&x-signature=%2FvMmHe8Bb01xYTYfVjq7MhHIq2s%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/0f481b14cb254132b94142b04de3ca8a?x-expires=1974358800&x-signature=pHEUda0FBkR9ddK9Q99e6RAWTqs%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/0f481b14cb254132b94142b04de3ca8a?x-expires=1974358800&x-signature=ExYbam2sQNolC2W%2F7UEtXftrVHs%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "guonianshu.png",
    "display_name": "[过年鼠]",
    "hide": 1,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/57c4feec2a84400aaea6c151480881ab",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/57c4feec2a84400aaea6c151480881ab?x-expires=1974358800&x-signature=M1jYFLJKASGCxU7jmUuYQYp41TQ%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/57c4feec2a84400aaea6c151480881ab?x-expires=1974358800&x-signature=gEDze5Gsu%2FWn09YlPSTapfJK%2BC0%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/57c4feec2a84400aaea6c151480881ab?x-expires=1974358800&x-signature=A0zR%2FQWEvAgHPBo8AqYD%2FAKZ6I4%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "xiaohuangya.png",
    "display_name": "[小黄鸭]",
    "hide": 1,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/8cffd861e51848d3923df35c01cc0f83",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/8cffd861e51848d3923df35c01cc0f83?x-expires=1974358800&x-signature=2xfv4A%2BwFSNFqg2oDxkiDKEptzY%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/8cffd861e51848d3923df35c01cc0f83?x-expires=1974358800&x-signature=Puylth1Iy0%2F8ownwa%2FWHzD0xzR4%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/8cffd861e51848d3923df35c01cc0f83?x-expires=1974358800&x-signature=e6El17zeFNDaeGn5dumajr7Dzz8%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "bangbangtang.png",
    "display_name": "[棒棒糖]",
    "hide": 1,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/a3c7d316db6d42a8805a3bfff56b2fe9",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/a3c7d316db6d42a8805a3bfff56b2fe9?x-expires=1974358800&x-signature=uDOxcr19W0SpmcMMqUy3OK8SqDI%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/a3c7d316db6d42a8805a3bfff56b2fe9?x-expires=1974358800&x-signature=Q1rBfhie47OIfOXaR3677ey%2Bgvc%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/a3c7d316db6d42a8805a3bfff56b2fe9?x-expires=1974358800&x-signature=4b8m6a655C5v7t%2F0bSNeMEfuPak%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "zhifeiji.png",
    "display_name": "[纸飞机]",
    "hide": 1,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/140db02486db48958670b22acde3dc20",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/140db02486db48958670b22acde3dc20?x-expires=1974358800&x-signature=VWcZxRZt9Hy%2Fz%2FyttTDTxJSyBYw%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/140db02486db48958670b22acde3dc20?x-expires=1974358800&x-signature=SJqyUb48yZWLLICTD7njl%2BuZAWM%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/140db02486db48958670b22acde3dc20?x-expires=1974358800&x-signature=dib43gruwFFLnIdmCLXLXhTXth0%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "bisheng.png",
    "display_name": "[必胜]",
    "hide": 1,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/a2ca21bf08584b17a339a15aeb7e95ce",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/a2ca21bf08584b17a339a15aeb7e95ce?x-expires=1974358800&x-signature=22nek5JE1N3dG4WCZyjW7uhBQqo%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/a2ca21bf08584b17a339a15aeb7e95ce?x-expires=1974358800&x-signature=B9ySE3SdWXfPeCsKP%2B19RCqAShU%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/a2ca21bf08584b17a339a15aeb7e95ce?x-expires=1974358800&x-signature=4Yc%2BzQ2%2BAiL%2F7UwYvbhqe0pyPMc%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "zongzi.png",
    "display_name": "[粽子]",
    "hide": 1,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/83773105269d4de3b29c96543d986461",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/83773105269d4de3b29c96543d986461?x-expires=1974358800&x-signature=9Dmpx0YBz62ZIF7Gd50748zGmVQ%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/83773105269d4de3b29c96543d986461?x-expires=1974358800&x-signature=Easz33oGw3QE8PBz%2FYkWCzyBAWg%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/83773105269d4de3b29c96543d986461?x-expires=1974358800&x-signature=Veym2%2FQ9ag%2FbNulaGB93VPQQ2cg%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "xiang.png",
    "display_name": "[象]",
    "hide": 1,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/f0acd5ba6df34bacbe4471d43d05ec71",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/f0acd5ba6df34bacbe4471d43d05ec71?x-expires=1974358800&x-signature=deFjw1JvKptoDFJKtHppi4u2N0E%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/f0acd5ba6df34bacbe4471d43d05ec71?x-expires=1974358800&x-signature=LMFYE0ou3cBhRpRv%2FQ8XB3ns944%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/f0acd5ba6df34bacbe4471d43d05ec71?x-expires=1974358800&x-signature=4l3Ldv9Ul9vK4%2BDIZcoI4uzSDKU%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "xiaohonghua.png",
    "display_name": "[小红花]",
    "hide": 1,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/38bf774e2e9642b3b1aac86c9293025e",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/38bf774e2e9642b3b1aac86c9293025e?x-expires=1974358800&x-signature=3fpafNdUeYP9ogEQBwuDaURs3Uo%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/38bf774e2e9642b3b1aac86c9293025e?x-expires=1974358800&x-signature=cLz3%2FoCbXsplLLdq1Wj43aUBs0g%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/38bf774e2e9642b3b1aac86c9293025e?x-expires=1974358800&x-signature=dsvoWKjp3wX2jjCrf42Qj3hzDDk%3D&from=876277922"
      ]
    }
  },
  {
    "origin_uri": "luosanpao.png",
    "display_name": "[罗三炮]",
    "hide": 1,
    "emoji_url": {
      "uri": "tos-cn-i-tsj2vxp0zn/f5bba13cccd74dc5b43440dca4f22836",
      "url_list": [
        "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/f5bba13cccd74dc5b43440dca4f22836?x-expires=1974358800&x-signature=VGHA%2B0kWKNF%2Bqi1xY100IqnAHjI%3D&from=876277922",
        "https://p6-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/f5bba13cccd74dc5b43440dca4f22836?x-expires=1974358800&x-signature=G5nV4AIEovcGFIcVqdcF0%2FCtNSo%3D&from=876277922",
        "https://p9-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/f5bba13cccd74dc5b43440dca4f22836?x-expires=1974358800&x-signature=e9igVENOnmg4mNwKAPKyPNNSZ6s%3D&from=876277922"
      ]
    }
  }
]
for i in em:
    Emojis.create(origin_uri=i['origin_uri'], display_name=i['display_name'])