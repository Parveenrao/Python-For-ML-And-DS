# scream_detection.py
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
import sounddevice as sd
import numpy as np
import soundfile as sf
import os


class ScreamDetectionApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', spacing=10)

        # Microphone Icon
        microphone_icon = Image(source='microphone.png', size_hint=(None, None), size=(100, 100))
        self.layout.add_widget(microphone_icon)

        # Record Button
        self.record_button = Button(text='Record', size_hint=(None, None), size=(100, 50))
        self.record_button.bind(on_press=self.record_audio)
        self.layout.add_widget(self.record_button)

        # Status Label
        self.status_label = Label(text='', color=(1, 0, 0, 1))
        self.layout.add_widget(self.status_label)

        return self.layout

    def record_audio(self, instance):
        # Disable record button during recording
        self.record_button.disabled = True

        # Start recording
        duration = 5  # Recording duration in seconds
        sample_rate = 44100
        recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype=np.int16)
        sd.wait()

        # Save the recorded audio to a file
        output_file = "recorded_audio.wav"
        sf.write('output_file_path.pkl', recording, sample_rate)

        # Predict the label for the recorded audio
        predicted_label = predict_audio('predicted_label.pkl', model, label_encoder)

        # Show the result in a popup
        message = f"The predicted label for the recorded audio is: {predicted_label}"
        if predicted_label == 1:
            message += "\n\nNearby Officer is alerted"
        else:
            message += "\n\nNo alert required"

        self.show_popup(message)

        # Re-enable record button
        self.record_button.disabled = False

    def show_popup(self, message):
        popup = Popup(title='Scream Detection', content=Label(text=message), size_hint=(None, None), size=(400, 200))
        popup.open()


if __name__ == '__main__':
    ScreamDetectionApp().run()

