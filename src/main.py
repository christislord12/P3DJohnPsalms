from panda3d.core import *
loadPrcFileData("", "audio-library-name p3openal_audio")
loadPrcFileData('', 'win-size 540 800')
from direct.showbase.DirectObject import DirectObject
from direct.gui.OnscreenText import OnscreenText
from direct.showbase.ShowBase import ShowBase
from direct.gui.DirectGui import *
from direct.task import Task
class MediaPlayer(ShowBase):
    def __init__(self):
        self.fxmodevalue = 1
        ShowBase.__init__(self)
        wp = WindowProperties()
        wp.setSize(540,800)
        self.win.requestProperties(wp)
        self.tex = MovieTexture("name")
        success = self.tex.read("JohnPsalms3DRenderUnderwater.mp4")
        self.cm = CardMaker("Video Card")
        self.cm.setFrame(-1.920, 1.080, -1.920, 1.080) 
        self.slider = DirectScrollBar(range=(0,278), value=0, pageSize=5,scrollSize = 2,resizeThumb=False, command=self.showValue)
        self.slider.setZ(-1.35)
        self.slider.setScale(1.52)
        self.cm.setUvRange(self.tex)
        self.card = NodePath(self.cm.generate())
        self.card.reparentTo(render)
        self.card.setTexture(self.tex)
        self.card.setScale(1.080,1.920,1.920)
        self.card.setPos(0.45,8,1)
        base.setBackgroundColor(0,0,0,0)
        self.sound = loader.loadSfx("JohnPsalms3DRenderUnderwater.mp4")
        self.tex.synchronizeTo(self.sound)
        self.accept('p', self.playpause)
        self.accept('P', self.playpause)
        self.playpb = DirectButton(text=(">"),pos=(0.9,0,-1.38), scale=.20, command=self.playpause)
        self.fxmode = DirectButton(text=("FX"),pos=(-0.9,0,-1.38), scale=.12, command=self.changefxmode)
        taskMgr.add(self.update, 'Update')
        self.playpause()
    def stopsound(self):
        self.sound.stop()
        self.sound.setPlayRate(1.0)
    def showValue(self):  
        if self.sound.status() == AudioSound.PLAYING:
            self.sound.setTime(self.slider['value'])
        else:
            self.sound.setTime(self.slider['value'])
            self.sound.play()
            self.sound.setTime(self.slider['value'])
            self.sound.stop()
            self.sound.setTime(self.slider['value'])
    def changefxmode(self):
        t = self.sound.getTime()
        self.timestore = t
        self.sound.stop()
        self.sound.setTime(t)
        self.playpb['text'] = ">"
        if self.fxmodevalue == 1:
            self.tex = MovieTexture("name")
            success = self.tex.read("JohnPsalms.mp4")
            self.sound = loader.loadSfx("JohnPsalms.mp4")
            self.cm.setUvRange(self.tex)
            self.card.setTexture(self.tex)
            self.tex.synchronizeTo(self.sound)
            self.slider.setValue(0)
            self.fxmodevalue = 0
            self.playpause()
        else:
            self.tex = MovieTexture("name")
            success = self.tex.read("JohnPsalms3DRenderUnderwater.mp4")
            self.sound = loader.loadSfx("JohnPsalms3DRenderUnderwater.mp4")
            self.cm.setUvRange(self.tex)
            self.card.setTexture(self.tex)
            self.tex.synchronizeTo(self.sound)
            self.slider.setValue(0)
            self.fxmodevalue = 1
            self.playpause()
    def update(self,task):
        if self.sound.status() == AudioSound.PLAYING:
            self.slider.setValue(self.sound.getTime())
        return task.cont
    def playpause(self):
        if self.sound.status() == AudioSound.PLAYING:
            t = self.sound.getTime()
            self.sound.stop()
            self.sound.setTime(t)
            self.playpb['text'] = ">"
        else:
            self.sound.play()
            self.playpb['text'] = "="
player = MediaPlayer()
player.run()