from ..ui import settings
from PyQt5 import QtWidgets
import os
from ..core import defaults


class ShowSettingsWindow(QtWidgets.QWidget, settings.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        appDir = os.path.dirname(os.path.realpath(__file__))
        try:
            os.chdir(f"{appDir}/../..")
            config = open("vasisualy.conf", "r")
            for line in config:
                if "voice:" in line:
                    voice = line.replace("voice:", "")
                elif "speed:" in line:
                    speed = int(line.replace("speed:", ""))
                elif "pitch:" in line:
                    pitch = int(line.replace("pitch:", ""))
                elif "sentences:" in line:
                    sentences = int(line.replace("sentences:", ""))
                elif "music:" in line:
                    musicDir = line.replace("music:", "")

            self.voiceBox.setCurrentText(voice)
            self.speedSlider.setSliderPosition(speed)
            self.pitchSlider.setSliderPosition(pitch)
            self.wikiSpin.setValue(sentences)
            self.musicLoc.setText(musicDir)
        except Exception:
            config = defaults.defaults
            self.voiceBox.setCurrentText(config["voice"])
            self.speedSlider.setSliderPosition(config["speed"])
            self.pitchSlider.setSliderPosition(config["pitch"])
            self.wikiSpin.setValue(config["sentences"])
            self.musicLoc.setText(config["music"])
        self.musicDir.clicked.connect(self.selectDir)
        self.buttonBox.accepted.connect(self.writeChanges)

    def writeChanges(self):
        appDir = os.path.dirname(os.path.realpath(__file__))
        os.chdir(f"{appDir}/../..")
        config = open("vasisualy.conf", "w")
        config.write(f"voice:{self.voiceBox.currentText()}\n"
                     f"speed:{self.speedSlider.sliderPosition()}\n"
                     f"pitch:{self.pitchSlider.sliderPosition()}\n"
                     f"sentences:{self.wikiSpin.value()}\n"
                     f"music:{self.musicLoc.text()}")
        config.close()
        self.hide()

    def selectDir(self):
        dir = QtWidgets.QFileDialog.getExistingDirectory()
        self.musicLoc.setText(dir)