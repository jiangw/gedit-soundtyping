from gi.repository import GObject, Gedit
import pygame
import time

class VoiceTypingWindowActivatable(GObject.Object, Gedit.WindowActivatable):
    __gtype_name__ = "VoiceTypingWindowActivatable"

    window = GObject.property(type=Gedit.Window)
    doc = 0

    def __init__(self):
        GObject.Object.__init__(self)
        pygame.init()

    def do_activate(self):
        print "VoiceTypingPlugin: Start listening keyboard input."
        l_id = self.window.connect("key_press_event", self.do_key_pressed)
        self.window.VoiceTypingPluginHandlerId = l_id
        pygame.mixer.music.load("/home/jiang/Share/gedit/plugins/typewriter-key-1.wav")

    def do_deactivate(self):
        print "VoiceTypingPlugin: Stop listening keyboard input."
        l_id = self.window.VoiceTypingPluginHandlerId
        self.window.disconnect(l_id)
        self.window.VoiceTypingPluginHandlerId = None

    def do_update_state(self):
        # Called whenever the window has been updated (active tab
        # changed, etc.)
        self.doc = self.window.get_active_document()
    
    def do_key_pressed(self, event, data):
        if self.doc != None:
            pygame.mixer.music.play()
            time.sleep(0.001)
