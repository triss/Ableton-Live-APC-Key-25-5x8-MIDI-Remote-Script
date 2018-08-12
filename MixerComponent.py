# Embedded file name: /Users/versonator/Jenkins/live/output/mac_64_static/Release/python-bundle/MIDI Remote Scripts/APC_Key_25/MixerComponent.py
# Compiled at: 2018-04-23 20:27:04
from __future__ import absolute_import, print_function, unicode_literals
from _APC.MixerComponent import MixerComponent as MixerComponentBase
from _APC.MixerComponent import ChanStripComponent as ChanStripComponentBase
from _Framework.Util import nop

class ChanStripComponent(ChanStripComponentBase):

    def __init__(self, *a, **k):
        self.reset_button_on_exchange = nop
        super(ChanStripComponent, self).__init__(*a, **k)


class MixerComponent(MixerComponentBase):

    def on_num_sends_changed(self):
        if self.send_index is None and self.num_sends > 0:
            self.send_index = 0
        return

    def _create_strip(self):
        return ChanStripComponent()
