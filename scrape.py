
dic = {'herbis':'ハービス大阪',
       'hankyu':'梅田阪急ビル',
       'granfront':'グランフロント大阪ビル',
       'citytower':'シティタワー西梅田',
       'breezetower':'ブリーゼタワービル',
       'owners':'オーナーズタワー  ビル',
       'sky':'梅田スカイビル',
       'meiji':'明治安田生命大阪梅田ビル',
       'tyayamati':'茶屋町アプローズタワー',
       'northgate':'ノースゲートビルディング',
       'aioi':'あいおいニッセイ同和損保フェニックスタワー',
       'umedatower':'THE UMEDA TOWER ',
       'hilton':'ヒルトン大阪',
       'yodobashi':'ヨドバシ梅田タワー',
       'mode':'大阪モード学園'}

from icrawler.builtin import BingImageCrawler
for k,v in dic.items():
       crawler = BingImageCrawler(storage={"root_dir": k})
       crawler.crawl(keyword=v,max_num=100)
