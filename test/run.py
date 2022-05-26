from pt.client.qbittorrent import Qbittorrent
from pt.client.transmission import Transmission
from pt.searcher import Searcher
from rmt.media import Media
from rmt.metainfo import MetaInfo
from utils.sqls import get_system_messages

if __name__ == "__main__":
    '''
    with open('torrentnames.txt', 'r', encoding='utf-8') as f:
        names = f.readlines()
        for name in names:
            meta_info = MetaInfo(name)
            print(meta_info.get_name())
    with open('filenames.txt', 'r', encoding='utf-8') as f:
        names = f.readlines()
        for name in names:
            meta_info = MetaInfo(name)
            print(meta_info.get_name())
    print(MetaInfo('归来.4k修复版.2004.CC.1080p').__dict__)
    print(MetaInfo('2046.4k修复版.2004.CC.1080p').__dict__)
    print(MetaInfo('[秘密访客].Home.Sweet.Home.2021.BlueRay.1080p').__dict__)
    print(MetaInfo('The.355.2021.BluRay.1080p').__dict__)
    print(MetaInfo('[神奇女侠.1984].Wonder.Woman.1984.2020.3D.BluRay.1080p').__dict__)
    print(MetaInfo('亲爱的.2014.TW.1080p.国语.简繁中字').__dict__)
    print(MetaInfo('医是医，二是二 - S01E02 - 第 10 集.mp4').__dict__)
    print(MetaInfo('Interstellar.IMAX.1080p.HDR.10bit.BT2020.DTS.HD').__dict__)
    print(MetaInfo('玻璃樽(未删减版).Gorgeous.UNCUT.1999.BluRay.1080p.x265.10bit').__dict__)
    print(MetaInfo('Kingmaker.2022.KOREAN.1080p.WEBRip.AAC2.0.x264-Imagine').__dict__)
    print(MetaInfo('[第 1 季 Ep6]Sweet Home - 第 6 集.mkv').__dict__)
    print(MetaInfo('[LPSub]Paripi Koumei[01][HEVC AAC][1080p][CH].mkv').__dict__)
    print(MetaInfo('[LPSub]Paripi Koumei[01][HEVC AAC][1080p][CH].mkv', anime=True).__dict__)
    print(MetaInfo('S01E01.mkv').__dict__)
    print(MetaInfo('[Nekomoe kissaten][Paripi Koumei][01][1080p][CHS].mp4', anime=True).__dict__)
    print(MetaInfo('[Sakurato] Kenja no Deshi o Nanoru Kenja [12][HEVC-10bit 1080p AAC][CHS&CHT].mkv', anime=True).__dict__)
    print(MetaInfo('[NC-Raws] 東方少年 - 06 (Baha 1920x1080 AVC AAC MP4).mp4', anime=True).__dict__)
    print(MetaInfo('[Nekomoe kissaten&LoliHouse] Paripi Koumei - 01 [WebRip 1080p HEVC-10bit AAC ASSx2].mkv', anime=True).__dict__)    
    print(MetaInfo('[Sono Bisque Doll wa Koi wo Suru][12][BIG5][1080P][MP4]', anime=True).__dict__)
    print(MetaInfo('[云光字幕组]恐怖神棍节 S3 Karakai Jouzu no S3[02][简体中文]', anime=True).__dict__)
    print(is_anime('[Nekomoe kissaten&LoliHouse] Paripi Koumei - 01 [WebRip 1080p HEVC-10bit AAC ASSx2].mkv'))
    print(is_anime('[NC-Raws] 東方少年 - 06 (Baha 1920x1080 AVC AAC MP4).mp4'))
    print(is_anime('[Sakurato] Kenja no Deshi o Nanoru Kenja [12][HEVC-10bit 1080p AAC][CHS&CHT].mkv'))
    print(is_anime('[LPSub]Paripi Koumei[01][HEVC AAC][1080p][CH].mkv'))
    print(is_anime('医是医，二是二 - S01E02 - 第 10 集.mp4'))
    print(is_anime('[LPSub]Paripi Koumei[HEVC AAC][2160x1080][CH].mkv'))
    print(is_anime('[Sono Bisque Doll wa Koi wo Suru][01-12][BIG5][1080P][MP4]'))
    print(MetaInfo('[Sono Bisque Doll wa Koi Wo Suru][06][BIG5][1080p].mp4', anime=True).__dict__)
    print(MetaInfo('Kenja no Deshi o Nanoru Kenja[12][1080p][CHS&CHT].mkv', anime=True).__dict__)
    print(MetaInfo('[Sono Bisque Doll wa Koi wo Suru][01-12][BIG5][1080P][MP4]', anime=True).__dict__)
    print(MetaInfo('[Nekomoe kissaten][Paripi Koumei][01][1080p][CHS].mp4', anime=True).__dict__)
    print(MetaInfo('[NC-Raws] 東方少年 - 06 (Baha 1920x1080 AVC AAC MP4).mp4', anime=True).__dict__)
    print(MetaInfo('[LPSub][Paripi Koumei][01][1080p][CHS].mp4', anime=True).__dict__)
    print(MetaInfo('[三少爷的剑]CHC.Kingmaker.2022.KOREAN.1080p.WEBRip.AAC2.0.x264-Imagine').__dict__)
    print(MetaInfo('[orion origin]Sono Bisque Doll wa Koi wo Suru [12] [END] [x265] [1440p] [DB].mkv', anime=True).__dict__)
    print(is_anime('[U2-Rip] SLAM DUNK 第005話「根性なしの午後」(BDrip 1440x1080 H264 FLAC).mkv'))
    print(MetaInfo('[U2-Rip] SLAM DUNK 第005話「根性なしの午後」(BDrip 1440x1080 H264 FLAC).mkv').__dict__)
    print(MetaInfo('进击的巨人.第4季.Attack.on.Titan.S04E28.1080p.WEB-DL.H264.ACC-OurTV.mkv').__dict__)
    print(MetaInfo('The Knick 2014-2015 Complete 1080p Blu-ray x265 AC3￡cXcY@FRDS').__dict__)
    print(select_by_sql('SELECT * FROM RSS_TVS'))
    media_info = Media().get_media_info('Paripi Koumei S01E01 1080p B-Global WEB-DL H264 AAC-CHDWEB')
    print(Rss().is_torrent_match(media_info, [], get_rss_tvs()))
    print(MetaInfo('Jurassic.World.3D.2015.1080p.Half-SBS.BluRay.x264.DTS-WiKi.mkv').__dict__)
    print(MetaInfo('Percent.World.3D.2022.2160p.WEB-DL.H265.DDP5.1-LeagueWEB.mkv').__dict__)
    print(MetaInfo('刺客伍六七.第03季.Scissor.Seven.Ⅲ.2021.第06话.WEB-DL.1080P.AVC.DD+2.0＆AAC.GB-XHGM.mkv').__dict__)
    print(MetaInfo('神奇女侠.1984.Wonder.Woman.1984.2020.3D.BluRay.1080p').__dict__)
    print(MetaInfo('神奇女侠.Wonder.Woman.1984.2020.3D.BluRay.1080p').__dict__)
    print(MetaInfo('Wonder.Woman.1984.2020.3D.BluRay.1080p').__dict__)
    print(MetaInfo('神奇女侠.1984.2020.3D.BluRay.1080p').__dict__)
    print(MetaInfo('1984.2020.3D.BluRay.1080p').__dict__)
    print(MetaInfo('[U2-Rip] SLAM DUNK 第005話「根性なしの午後」(BDrip 1440x1080 H264 FLAC).mkv').__dict__)
    print(MetaInfo('西部世界 第2集.mkv').__dict__)
    print(MetaInfo('西部世界 02.mkv').__dict__)
    print(MetaInfo('1.mkv').__dict__)
    '''
    # print(MetaInfo('刺客伍六七.全3季.Scissor.Seven.Ⅲ.2021.WEB-DL.1080P.AVC.DD+2.0＆AAC.GB-XHGM.mkv').__dict__)
    # print(MetaInfo('刺客伍六七.E01-E05.全2季.Scissor.Seven.Ⅲ.2021.WEB-DL.1080P.AVC.DD+2.0＆AAC.GB-XHGM.mkv').__dict__)
    # FileTransfer().transfer_media(in_from=SyncType.MAN, in_path="C:\\Users\\jxxgh\\Documents\\TV\\Breaking.Bad.Season.3.Episode.10.Fly.REMUX-FraMeSToR.mkv")
    # Searcher().search_one_media("进击的巨人")
    # print(MetaInfo('Hokusai.to.meshi.sae.areba.S01E03.2017.1080p.KKTV.WEB-DL.x264.ACC-ADWeb').__dict__)
    # print(get_config_search_rule())
    # print(MetaInfo('556.mkv').__dict__)
    # insert_transfer_unknown("/volume1/PT/任何人 (2022)", "/电影")
    # insert_transfer_unknown("/volume1/PT/Etharkkum.Thunindhavan.2022.1080p.NF.WEB-DL.H264.DDP5.1-ADWeb5", "")
    # print(Jellyfin().get_no_exists_episodes(meta_info, 1, 10))
    # print(Jellyfin().get_movies("我和我的祖国", "2019"))
    # meta_info = Media().get_media_info("未来中国 2022")
    '''insert_rss_tv(meta_info, 30, 12)
    meta_info = Media().get_media_info("西部世界 2022 S01")
    insert_rss_tv(meta_info, 8, 2)
    meta_info = Media().get_media_info("我和我的祖国 2019")
    insert_rss_movie(meta_info)
    meta_info = Media().get_media_info("新蝙蝠侠 2022")
    insert_rss_movie(meta_info)'''
    # print(get_rss_tvs())
    # update_by_sql("DELETE FROM DOUBAN_MEDIAS")
    # DoubanSync().run_schedule()
    # RssSearch().run_schedule()
    # print(MetaInfo('Season 1').__dict__)
    # meta_info = Media().get_media_info("双城之战 2021")
    # print(Jellyfin().get_no_exists_episodes(meta_info, 1, 36))
    # meta_info = Media().get_media_info("灌篮高手.Slam.Dunk.EP017.1993.BluRay.x264.5Audio.1080p-52HD.mkv")
    # print(meta_info.__dict__)
    # movie = Plex().get_medias_count()
    # print(movie)
    # print(Media().get_media_info("Seasons 2016 BluRay 1080p 2Audio DTS HD MA-5.1 x264-beAst ").__dict__)
    # print(get_transfer_statistics())
    # print(len(Qbittorrent().get_completed_torrents()))
    # add_rss_substribe_from_string(rss_string="订阅 西部世界", in_from=SearchType.WX)
    # items = [{"file": "C:\\Users\\jxxgh\\Documents\\Movie\\任何人 (2022)\\任何人 (2022) - 1080P", "name": "In the Mood for Love"}]
    # Subtitle().download_subtitle(items)
    # print(Media().get_media_info("The Adam Project 2022 1080p DSNP WEB-DL DDP5.1 Atmos Multiple Audios X264 ASS-DIY@JAKET789").__dict__)
    # Searcher().search_one_media("亚当计划")
    # print(Media().get_media_info('Mud.2012.1080p.BluRay.DD5.1x264-SA89.mkv').__dict__)
    print(Media().get_media_info("[星空字幕组][间谍过家家 / SPY×FAMILY][03][简日双语][1080P][WEBrip][MP4]（急招翻译、校对、时轴）").__dict__)
