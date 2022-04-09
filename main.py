import os
import sys
import traceback

import requests
from mutagen.flac import FLAC, Picture
from mutagen.id3 import APIC, ID3
from mutagen.wave import WAVE
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from SearchNetease import SearchNetease
from ui_mainw import Ui_MainWindow


class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setup_thread()
        self.setup_con()
        self.cover_data_list = []

    def Questionbox(self, title: str, text: str):
        msgbox = QMessageBox(QMessageBox.Question, title, text, parent=self)
        msgbox.addButton("确定", QMessageBox.YesRole)
        msgbox.addButton("取消", QMessageBox.NoRole)
        replay = msgbox.exec()
        return replay

    def setup_thread(self):
        self.thread1 = QThread(self)
        self.cover_thread = GetNeteaseCoverData()
        self.cover_thread.moveToThread(self.thread1)
        # 线程数据传回信号
        self.cover_thread.netease_data_requested.connect(self.add_coverdata_item)

    def setup_con(self):
        self.viewfld_pushButton.clicked.connect(self.open_music_floder)
        self.music_listWidget.currentRowChanged.connect(self.change_music)
        self.music_listWidget.currentRowChanged.connect(
            self.cover_thread.get_music_name
        )  # 线程启动信号
        self.cover_listWidget.currentRowChanged.connect(self.change_cover_selected)
        self.save_pushButton.clicked.connect(self.save_tags)
        self.search_pushButton.clicked.connect(self.cover_thread.get_music_name)
        self.about_pushButton.clicked.connect(self.about_me)

    def open_music_floder(self):
        open_path = QFileDialog.getExistingDirectory(
            self, "打开音乐文件夹...", r"D:\Music\acgMusic"
        )
        if open_path != "":
            new_path = open_path
            norm_path = os.path.normpath(new_path)
            self.path_label.setText(norm_path)
            self.path_label.setToolTip(norm_path)
            self.setup_music_listwidget(new_path)

    def setup_music_listwidget(self, path):
        self.music_listWidget.clear()
        self.music_list = []
        scan_file = os.scandir(path)
        self.music_count = 0
        for i in scan_file:
            if i.is_file():
                ext = os.path.splitext(i.path)[1]
                if ext == ".mp3" or ext == ".flac" or ext == ".wav":
                    list_item = QListWidgetItem()
                    list_item.setText(i.name)
                    self.music_listWidget.addItem(list_item)
                    self.music_list.append(i)
                    self.music_count += 1
                else:
                    print(ext)
        self.count_label.setText(f"0/{self.music_count}")

    def change_music(self, current_row: int):
        if self.thread1.isRunning():
            self.thread1.terminate()
        self.cover_listWidget.clear()
        self.cover_data_list = []
        self.thread1.start()
        self.save_pushButton.setEnabled(False)
        self.count_label.setText(f"{current_row+1}/{self.music_count}")
        file: os.DirEntry = self.music_list[current_row]
        self.file_path_label.setText(file.path)
        ext = os.path.splitext(file.path)[1]
        if ext == ".mp3":
            self.id3_tag_read(file)
        elif ext == ".flac":
            self.flac_tag_read(file)
        elif ext == ".wav":
            self.wave_tag_read(file)

    def id3_tag_read(self, file: os.DirEntry):
        file_obj = ID3(file.path)
        # 获取歌曲名称
        music_name_list = file_obj.getall("TIT2")
        if len(music_name_list) > 0:
            music_name = music_name_list[0].text[0]
        else:
            music_name = "标签信息缺失！"
        self.music_lineEdit.setText(music_name)
        # 获取歌曲歌手
        singer_list = file_obj.getall("TPE1")
        if len(singer_list) > 0:
            music_singer = singer_list[0].text[0]
        else:
            music_singer = "标签信息缺失！"
        self.singer_lineEdit.setText(music_singer)
        # 获取歌曲专辑
        al_list = file_obj.getall("TALB")
        if len(al_list) > 0:
            music_al = al_list[0].text[0]
        else:
            music_al = "标签信息缺失！"
        self.al_lineEdit.setText(music_al)
        # 获取专辑封面
        cover_list = file_obj.getall("APIC")
        if len(cover_list) == 0:
            self.cover_label.setText("未能获取到专辑封面信息...")
            self.size_label.setText(r"N\A")
        else:
            cover_data = cover_list[0].data
            self.setup_cover(cover_data)

    def flac_tag_read(self, file: os.DirEntry):
        file_obj = FLAC(file.path)
        tags_dict = {"TITLE": "标签信息缺失！", "ALBUM": "标签信息缺失！", "ARTIST": "标签信息缺失！"}
        for tag_tuple in file_obj.tags:
            tag = tag_tuple[0].upper()
            for key in tags_dict.keys():
                if tag == key:
                    tags_dict[key] = tag_tuple[1]
        # 获取歌曲名称
        music_name = tags_dict["TITLE"]
        self.music_lineEdit.setText(music_name)
        # 获取歌曲专辑
        album_name = tags_dict["ALBUM"]
        self.al_lineEdit.setText(album_name)
        # 获取歌曲歌手
        singer_name = tags_dict["ARTIST"]
        self.singer_lineEdit.setText(singer_name)
        # 获取专辑封面
        if len(file_obj.pictures) > 0:
            cover_data = file_obj.pictures[0].data
            self.setup_cover(cover_data)
        else:
            self.cover_label.setText("未能获取到专辑封面信息...")
            self.size_label.setText(r"N\A")

    def wave_tag_read(self, file: os.DirEntry):
        file_obj = WAVE(file.path)
        # 获取歌曲名称
        music_name_list = file_obj.tags.getall("TIT2")
        if len(music_name_list) > 0:
            music_name = music_name_list[0].text[0]
        else:
            music_name = "标签信息缺失！"
        self.music_lineEdit.setText(music_name)
        # 获取歌曲歌手
        singer_list = file_obj.tags.getall("TPE1")
        if len(singer_list) > 0:
            music_singer = singer_list[0].text[0]
        else:
            music_singer = "标签信息缺失！"
        self.singer_lineEdit.setText(music_singer)
        # 获取歌曲专辑
        al_list = file_obj.tags.getall("TALB")
        if len(al_list) > 0:
            music_al = al_list[0].text[0]
        else:
            music_al = "标签信息缺失！"
        self.al_lineEdit.setText(music_al)
        # 获取专辑封面
        cover_list = file_obj.tags.getall("APIC")
        if len(cover_list) == 0:
            self.cover_label.setText("未能获取到专辑封面信息...")
            self.size_label.setText(r"N\A")
        else:
            cover_data = cover_list[0].data
            self.setup_cover(cover_data)

    def change_cover_selected(self, current_row: int):
        self.save_pushButton.setEnabled(True)
        cover_data = self.cover_data_list[current_row]
        self.setup_cover(cover_data)

    def setup_cover(self, data):
        self.cover_label.clear()
        cover_pixmap = QPixmap()
        cover_pixmap.loadFromData(data)
        self.cover_label.setPixmap(cover_pixmap)
        size = self.get_pixmap_size(cover_pixmap)
        self.size_label.setText(f"{size[0]}*{size[1]}")

    def add_coverdata_item(self, data_list: list):
        item = QListWidgetItem()
        music_name = data_list[0]
        music_singer = data_list[2]
        music_al = data_list[3]
        cover_data = data_list[5]
        cover = QPixmap()
        cover.loadFromData(cover_data)
        item.setIcon(cover)
        size = self.get_pixmap_size(cover)
        item.setText(
            f"{music_singer} - {music_name}\n专辑：{music_al}\n封面尺寸：{size[0]}*{size[1]}"
        )
        self.cover_listWidget.addItem(item)
        self.cover_data_list.append(cover_data)

    def save_tags(self):
        file_selcet_item = self.music_listWidget.selectedItems()[0]
        file_index = self.music_listWidget.row(file_selcet_item)
        file = self.music_list[file_index]
        cover_data_item = self.cover_listWidget.selectedItems()[0]
        cover_data_index = self.cover_listWidget.row(cover_data_item)
        cover_data = self.cover_data_list[cover_data_index]
        ext = os.path.splitext(file.path)[1]
        if ext == ".mp3":
            self.save_id3(file.path, cover_data)
        elif ext == ".flac":
            self.save_flac(file.path, cover_data)
        elif ext == ".wav":
            self.save_wave(file.path, cover_data)

    def save_id3(self, file_path, cover_data):
        id3_obj = ID3(file_path)
        cover_list = id3_obj.getall("APIC")
        if len(cover_list) > 0:
            replay = self.Questionbox("覆盖专辑封面", "该歌曲已存在专辑封面，是否覆盖？\n注意：这将会删除所有的图片！")
            if replay == 1:  # user cancel
                return
        id3_obj.delall("APIC")
        id3_obj.add(
            APIC(encoding=3, mime="image/jpeg", type=3, desc="Cover", data=cover_data)
        )
        try:
            id3_obj.save()
            QMessageBox(
                QMessageBox.Information, "成功！", "成功嵌入当前专辑封面！", QMessageBox.Ok, self
            ).exec()
        except:
            QMessageBox(
                QMessageBox.Critical,
                "失败！",
                traceback.format_exc(),
                QMessageBox.Ok,
                self,
            ).exec()

    def save_flac(self, file_path, cover_data):
        flac_obj = FLAC(file_path)
        if len(flac_obj.pictures) > 0:
            replay = self.Questionbox("覆盖专辑封面", "该歌曲已存在专辑封面，是否覆盖？\n注意：这将会删除所有的图片！")
            if replay == 1:  # user cancel
                return
        flac_obj.clear_pictures()
        cover = Picture()
        cover.type = 3
        cover.mime = "image/jpeg"
        cover.desc = "Cover"
        cover.data = cover_data
        flac_obj.add_picture(cover)
        try:
            flac_obj.save()
            QMessageBox(
                QMessageBox.Information, "成功！", "成功嵌入当前专辑封面！", QMessageBox.Ok, self
            ).exec()
        except:
            QMessageBox(
                QMessageBox.Critical,
                "失败！",
                traceback.format_exc(),
                QMessageBox.Ok,
                self,
            ).exec()

    def save_wave(self, file_path, cover_data):
        wave_obj = WAVE(file_path)
        cover_list = wave_obj.tags.getall("APIC")
        if len(cover_list) > 0:
            replay = self.Questionbox("覆盖专辑封面", "该歌曲已存在专辑封面，是否覆盖？\n注意：这将会删除所有的图片！")
            if replay == 1:  # user cancel
                return
        wave_obj.tags.delall("APIC")
        wave_obj.tags.add(
            APIC(encoding=3, mime="image/jpeg", type=3, desc="Cover", data=cover_data)
        )
        try:
            wave_obj.save()
            QMessageBox(
                QMessageBox.Information, "成功！", "成功嵌入当前专辑封面！", QMessageBox.Ok, self
            ).exec()
        except:
            QMessageBox(
                QMessageBox.Critical,
                "失败！",
                traceback.format_exc(),
                QMessageBox.Ok,
                self,
            ).exec()

    def get_pixmap_size(self, pixmap: QPixmap):
        size = pixmap.size()
        w = size.width()
        h = size.height()
        return w, h

    def about_me(self):
        QMessageBox.about(
            self,
            "关于...",
            "专辑封面管理器 Ver 0.3\n一款获取网易云音乐封面并一键嵌入音频文件的软件。\n支持格式：.mp3,.flac,.wav",
        )


class GetNeteaseCoverData(QObject):
    netease_data_requested = Signal(list)  # 传出信号

    def __init__(self):
        super().__init__()

    def get_music_name(self):
        music_name = main_window.music_lineEdit.text()
        if music_name == "标签信息缺失！":
            return
        ss = SearchNetease()
        result_list = ss.search_song(music_name)
        if len(result_list) == 0:
            main_window.cover_listWidget.addItem(
                QListWidgetItem(QPixmap(), "未能搜索到专辑封面，请检查网络、歌曲标签之后重试！")
            )
        for i in result_list:
            cover = requests.get(i[4], timeout=20)
            cover_data = cover.content
            i.append(cover_data)
            self.netease_data_requested.emit(i)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    app.exec()
