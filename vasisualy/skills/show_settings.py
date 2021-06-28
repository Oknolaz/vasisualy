from ..ui import settings
from PyQt5 import QtWidgets
from ..core import defaults
import json


class ShowSettingsWindow(QtWidgets.QWidget, settings.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        try:
            voice = defaults.get_value("voice")
            speed = defaults.get_value("speed")
            pitch = defaults.get_value("pitch")
            sentences = defaults.get_value("wiki_sentences")
            musicDir = defaults.get_value("music")
            theme = defaults.get_value("theme")
            to_lang = defaults.get_value("to_lang")
            from_lang = defaults.get_value("from_lang")
            weather_api = defaults.get_value("weather_api")
            weather_city = defaults.get_value("weather_city")
            self.voiceBox.setCurrentText(voice)
            self.speedSlider.setSliderPosition(speed)
            self.pitchSlider.setSliderPosition(pitch)
            self.wikiSpin.setValue(sentences)
            self.musicLoc.setText(musicDir)
            self.themeCombo.setCurrentText(theme)
            self.toLangCombo.setCurrentText(to_lang)
            self.fromLangCombo.setCurrentText(from_lang)
            self.weatherApi.setText(weather_api)
            self.weatherCity.setText(weather_city)
        except Exception:
            config = defaults.defaults
            self.voiceBox.setCurrentText(config["voice"])
            self.speedSlider.setSliderPosition(config["speed"])
            self.pitchSlider.setSliderPosition(config["pitch"])
            self.wikiSpin.setValue(config["wiki_sentences"])
            self.musicLoc.setText(config["music"])
            self.themeCombo.setCurrentText(config["theme"])
            self.toLangCombo.setCurrentText(config["to_lang"])
            self.fromLangCombo.setCurrentText(config["from_lang"])
            self.weatherApi.setText(config["weather_api"])
            self.weatherCity.setText(config["weather_city"])
        self.musicDir.clicked.connect(self.selectDir)
        self.buttonBox.accepted.connect(self.writeChanges)
        self.buttonBox.rejected.connect(self.hide)

    def writeChanges(self):
        config = {
            "voice": self.voiceBox.currentText(),
            "speed": self.speedSlider.sliderPosition(),
            "pitch": self.pitchSlider.sliderPosition(),
            "wiki_sentences": self.wikiSpin.value(),
            "music": self.musicLoc.text(),
            "theme": self.themeCombo.currentText(),
            "to_lang": self.toLangCombo.currentText(),
            "from_lang": self.fromLangCombo.currentText(),
            "weather_api": self.weatherApi.text(),
            "weather_city": self.weatherCity.text()
        }
        with open("vasisualy.json", "w") as f:
            json.dump(config, f)
        self.hide()

    def selectDir(self):
        dir = QtWidgets.QFileDialog.getExistingDirectory()
        self.musicLoc.setText(dir)
