from kivy.app import App
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import ObjectProperty, NumericProperty, Clock
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.widget import Widget

from audio_engine import AudioEngine
from sound_kit_service import SoundKitService
from track import TrackWidget

Builder.load_file("track.kv")
Builder.load_file("play_indicator.kv")

TRACKS_NB_STEPS = 16
MIN_BPM = 80
MAX_BPM = 160

class MainWidget(RelativeLayout):
    tracks_layout = ObjectProperty()
    play_indicator_widget = ObjectProperty()
    TRACK_STEPS_LEFT_ALIGN = NumericProperty(dp(100))
    step_index = 0
    bpm = NumericProperty(115)

    def __init__(self, **kwargs):
        super(MainWidget, self).__init__(**kwargs)
        self.sound_kit_service = SoundKitService()
        self.audio_engine = AudioEngine()

        # kick_sound = self.sound_kit_service.get_sound_at(0)
        # self.audio_engine.play_sound(kick_sound.samples)

        # self.audio_engine.create_track(kick_sound.samples, 120)

        # call create_mixer(...120, TRACKS_NB_STEPS)
        self.mixer = self.audio_engine.create_mixer(self.sound_kit_service.soundkit.get_all_samples(), self.bpm, TRACKS_NB_STEPS, self.on_mixer_current_step_changed, MIN_BPM)

    def on_parent(self, widget, parent):
        self.play_indicator_widget.set_nb_steps(TRACKS_NB_STEPS)
        # 2 - test your function here ()
        # self.play_indicator_widget.set_current_step_index(8)

        for i in range(0, self.sound_kit_service.get_nb_tracks()):
            sound = self.sound_kit_service.get_sound_at(i)
            self.tracks_layout.add_widget(TrackWidget(sound, self.audio_engine, TRACKS_NB_STEPS, self.mixer.tracks[i], self.TRACK_STEPS_LEFT_ALIGN))

    def on_mixer_current_step_changed(self, step_index):
        # print("on_mixer_current_step_changed: " + str(step_index))
        # executed in an audio thread
        self.step_index = step_index
        Clock.schedule_once(self.update_play_indicator_cbk, 0)

    def update_play_indicator_cbk(self, dt):
        # executed in the main UI thread
        if self.play_indicator_widget is not None:
            self.play_indicator_widget.set_current_step_index(self.step_index)

    def on_play_button_pressed(self):
        self.mixer.audio_play()

    def on_stop_button_pressed(self):
        self.mixer.audio_stop()

    def on_bpm(self, widget, value):
        print("BPM: " + str(value))
        # 80 - 160
        if value < MIN_BPM:
            self.bpm = MIN_BPM
            return
        if value > MAX_BPM:
            self.bpm = MAX_BPM
            return

        # pass to the audio engine
        self.mixer.set_bpm(self.bpm)

class MrBeatApp(App):
    pass


MrBeatApp().run()


