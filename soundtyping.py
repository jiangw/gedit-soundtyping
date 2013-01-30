from gi.repository import GObject, Gedit
import pygame
import time

class VoiceTypingWindowActivatable(GObject.Object, Gedit.WindowActivatable):
    __gtype_name__ = "VoiceTypingWindowActivatable"

    window = GObject.property(type=Gedit.Window)
    doc = 0
    snd_abc = 0
    snd_ABC = 0
    snd_123 = 0
    snd_others = 0

    def __init__(self):
        GObject.Object.__init__(self)
        pygame.mixer.init()

    def do_activate(self):
        print "VoiceTypingPlugin: Start listening keyboard input."
        l_id = self.window.connect("key_press_event", self.do_key_pressed)
        self.window.VoiceTypingPluginHandlerId = l_id
        self.snd_abc = pygame.mixer.Sound("/home/jiang/Share/gedit/plugins/SoundTyping/abc.wav")
        self.snd_ABC = pygame.mixer.Sound("/home/jiang/Share/gedit/plugins/SoundTyping/ABC.wav")
        self.snd_123 = pygame.mixer.Sound("/home/jiang/Share/gedit/plugins/SoundTyping/123.wav")
        self.snd_others = pygame.mixer.Sound("/home/jiang/Share/gedit/plugins/SoundTyping/others.wav")

    def do_deactivate(self):
        print "VoiceTypingPlugin: Stop listening keyboard input."
        l_id = self.window.VoiceTypingPluginHandlerId
        self.window.disconnect(l_id)
        self.window.VoiceTypingPluginHandlerId = None

    def do_update_state(self):
        # Called whenever the window has been updated (active tab
        # changed, etc.)
        self.doc = self.window.get_active_document()
    
    def do_key_pressed(self, window, event):
        if self.doc != None:
            if event.keyval >= 0x030 and event.keyval <= 0x039:
                self.snd_123.play()
                time.sleep(0.001)
            elif event.keyval >= 0x061 and event.keyval <= 0x07a:
                self.snd_abc.play()
                time.sleep(0.001)
            elif event.keyval >= 0x041 and event.keyval <= 0x05a:
                self.snd_ABC.play()
                time.sleep(0.001)
            else:
                self.snd_others.play()
                time.sleep(0.001)
