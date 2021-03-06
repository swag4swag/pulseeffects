# -*- coding: utf-8 -*-

import configparser


class SavePresets():

    def __init__(self):
        self.config = configparser.ConfigParser()

    def set_output_path(self, path):
        self.output_file = open(path, 'w')

    def save_limiter_presets(self, settings, section):
        enabled = settings.get_value('limiter-state')
        input_gain = settings.get_value('limiter-input-gain')
        limit = settings.get_value('limiter-limit')
        release_time = settings.get_value('limiter-release-time')

        self.config[section] = {'enabled': str(enabled),
                                'input gain': str(input_gain),
                                'limit': str(limit),
                                'release time': str(release_time)}

    def save_autovolume_presets(self, settings, section):
        enabled = settings.get_value('autovolume-state')
        window = settings.get_value('autovolume-window')
        target = settings.get_value('autovolume-target')
        tolerance = settings.get_value('autovolume-tolerance')
        threshold = settings.get_value('autovolume-threshold')

        self.config[section] = {'enabled': str(enabled),
                                'window': str(window),
                                'target': str(target),
                                'tolerance': str(tolerance),
                                'threshold': str(threshold)}

    def save_panorama_presets(self, settings, section):
        enabled = settings.get_value('panorama-state')
        position = settings.get_value('panorama-position')

        self.config[section] = {'enabled': str(enabled),
                                'position': str(position)}

    def save_compressor_presets(self, settings, section):
        enabled = settings.get_value('compressor-state')
        use_peak = settings.get_value('compressor-use-peak')
        attack = settings.get_value('compressor-attack')
        release = settings.get_value('compressor-release')
        threshold = settings.get_value('compressor-threshold')
        ratio = settings.get_value('compressor-ratio')
        knee = settings.get_value('compressor-knee')
        makeup = settings.get_value('compressor-makeup')

        self.config[section] = {'enabled': str(enabled),
                                'use_peak': str(use_peak),
                                'attack': str(attack),
                                'release': str(release),
                                'threshold': str(threshold),
                                'ratio': str(ratio),
                                'knee': str(knee),
                                'makeup': str(makeup)}

    def save_reverb_presets(self, settings, section):
        enabled = settings.get_value('reverb-state')
        room_size = settings.get_value('reverb-room-size')
        damping = settings.get_value('reverb-damping')
        width = settings.get_value('reverb-width')
        level = settings.get_value('reverb-level')

        self.config[section] = {'enabled': str(enabled),
                                'room size': str(room_size),
                                'damping': str(damping),
                                'width': str(width),
                                'level': str(level)}

    def save_highpass_presets(self, settings, section):
        enabled = settings.get_value('highpass-state')
        cutoff = settings.get_value('highpass-cutoff')
        poles = settings.get_value('highpass-poles')

        self.config[section] = {'enabled': str(enabled), 'cutoff': str(cutoff),
                                'poles': str(poles)}

    def save_lowpass_presets(self, settings, section):
        enabled = settings.get_value('lowpass-state')
        cutoff = settings.get_value('lowpass-cutoff')
        poles = settings.get_value('lowpass-poles')

        self.config[section] = {'enabled': str(enabled), 'cutoff': str(cutoff),
                                'poles': str(poles)}

    def save_equalizer_presets(self, settings, section):
        enabled = settings.get_value('equalizer-state')
        input_gain = settings.get_value('equalizer-input-gain')
        output_gain = settings.get_value('equalizer-output-gain')

        gain, frequencies, qualities, types = [], [], [], []

        for n in range(15):
            gain.append(
                settings.get_value('equalizer-band' + str(n) + '-gain'))

            frequencies.append(
                settings.get_value('equalizer-band' + str(n) + '-frequency'))

            qualities.append(
                settings.get_value('equalizer-band' + str(n) + '-quality'))

            types.append(
                settings.get_value('equalizer-band' + str(n) + '-type'))

        self.config[section] = {'enabled': str(enabled),
                                'input_gain': str(input_gain),
                                'output_gain': str(output_gain),
                                'band0': str(gain[0]),
                                'band1': str(gain[1]),
                                'band2': str(gain[2]),
                                'band3': str(gain[3]),
                                'band4': str(gain[4]),
                                'band5': str(gain[5]),
                                'band6': str(gain[6]),
                                'band7': str(gain[7]),
                                'band8': str(gain[8]),
                                'band9': str(gain[9]),
                                'band10': str(gain[10]),
                                'band11': str(gain[11]),
                                'band12': str(gain[12]),
                                'band13': str(gain[13]),
                                'band14': str(gain[14]),
                                'band0_freq': str(frequencies[0]),
                                'band1_freq': str(frequencies[1]),
                                'band2_freq': str(frequencies[2]),
                                'band3_freq': str(frequencies[3]),
                                'band4_freq': str(frequencies[4]),
                                'band5_freq': str(frequencies[5]),
                                'band6_freq': str(frequencies[6]),
                                'band7_freq': str(frequencies[7]),
                                'band8_freq': str(frequencies[8]),
                                'band9_freq': str(frequencies[9]),
                                'band10_freq': str(frequencies[10]),
                                'band11_freq': str(frequencies[11]),
                                'band12_freq': str(frequencies[12]),
                                'band13_freq': str(frequencies[13]),
                                'band14_freq': str(frequencies[14]),
                                'band0_qfactor': str(qualities[0]),
                                'band1_qfactor': str(qualities[1]),
                                'band2_qfactor': str(qualities[2]),
                                'band3_qfactor': str(qualities[3]),
                                'band4_qfactor': str(qualities[4]),
                                'band5_qfactor': str(qualities[5]),
                                'band6_qfactor': str(qualities[6]),
                                'band7_qfactor': str(qualities[7]),
                                'band8_qfactor': str(qualities[8]),
                                'band9_qfactor': str(qualities[9]),
                                'band10_qfactor': str(qualities[10]),
                                'band11_qfactor': str(qualities[11]),
                                'band12_qfactor': str(qualities[12]),
                                'band13_qfactor': str(qualities[13]),
                                'band14_qfactor': str(qualities[14]),
                                'band0_type': str(types[0]),
                                'band1_type': str(types[1]),
                                'band2_type': str(types[2]),
                                'band3_type': str(types[3]),
                                'band4_type': str(types[4]),
                                'band5_type': str(types[5]),
                                'band6_type': str(types[6]),
                                'band7_type': str(types[7]),
                                'band8_type': str(types[8]),
                                'band9_type': str(types[9]),
                                'band10_type': str(types[10]),
                                'band11_type': str(types[11]),
                                'band12_type': str(types[12]),
                                'band13_type': str(types[13]),
                                'band14_type': str(types[14])}

    def save_output_limiter_presets(self, settings, section):
        enabled = settings.get_value('output-limiter-state')
        input_gain = settings.get_value('output-limiter-input-gain')
        limit = settings.get_value('output-limiter-limit')
        release_time = settings.get_value('output-limiter-release-time')

        self.config[section] = {'enabled': str(enabled),
                                'input gain': str(input_gain),
                                'limit': str(limit),
                                'release time': str(release_time)}

    def save_sink_inputs_presets(self, settings):
        self.save_limiter_presets(settings, 'apps_limiter')
        self.save_autovolume_presets(settings, 'apps_autovolume')
        self.save_panorama_presets(settings, 'apps_panorama')
        self.save_compressor_presets(settings, 'apps_compressor')
        self.save_reverb_presets(settings, 'apps_reverb')
        self.save_highpass_presets(settings, 'apps_highpass')
        self.save_lowpass_presets(settings, 'apps_lowpass')
        self.save_equalizer_presets(settings, 'apps_equalizer')
        self.save_output_limiter_presets(settings, 'apps_output_limiter')

    def save_source_outputs_presets(self, settings):
        self.save_limiter_presets(settings, 'mic_limiter')
        self.save_autovolume_presets(settings, 'mic_autovolume')
        self.save_compressor_presets(settings, 'mic_compressor')
        self.save_reverb_presets(settings, 'mic_reverb')
        self.save_highpass_presets(settings, 'mic_highpass')
        self.save_lowpass_presets(settings, 'mic_lowpass')
        self.save_equalizer_presets(settings, 'mic_equalizer')

    def write_config(self):
        self.config.write(self.output_file)
        self.output_file.close()
