''' python resample from 1-minute to lower frequencies
'''
def resample_to_lower_freq(self, instrument):
    first_time_frame = self.time_frames[0]
    for time_frame, time_frame_timedelta in zip(self.time_frames[1:], self.time_frame_timedeltas[1:]):
        self.ohlc[time_frame][instrument]['open'] = self.ohlc[first_time_frame][instrument]['open'].resample(
                    time_frame).first().ffill(limit=0).dropna()
        self.ohlc[time_frame][instrument]['close'] = self.ohlc[first_time_frame][instrument]['close'].resample(
                    time_frame).last().ffill(limit=0).dropna()
        self.ohlc[time_frame][instrument]['high'] = self.ohlc[first_time_frame][instrument]['high'].resample(
                    time_frame).max().ffill(limit=0).dropna()
        self.ohlc[time_frame][instrument]['low'] = self.ohlc[first_time_frame][instrument]['low'].resample(
                    time_frame).min().ffill(limit=0).dropna()
        self.ohlc[time_frame][instrument]['volume'] = self.ohlc[first_time_frame][instrument]['volume'].resample(
                    time_frame).sum().ffill(limit=0).dropna()
        self.ohlc[time_frame][instrument]['instrument'] = instrument
        self.ohlc[time_frame][instrument]['market'] = self.sec_names[instrument]
        self.ohlc[time_frame][instrument]['timestamp'] = self.ohlc[time_frame][instrument].index.values
        self.ohlc[time_frame][instrument]['period'] = self.time_frame_map[time_frame]
