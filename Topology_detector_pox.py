from pox.core import core
import pox.openflow.libopenflow_01 as of

from pox.lib.revent import EventMixin
from pox.openflow.discovery import Discovery
from pox.openflow.discovery import LinkEvent

import datetime

log = core.getLogger()

class TopologyDetector(EventMixin):

    def __init__(self):
        self.listenTo(core.openflow)
        self.listenTo(core.openflow_discovery)

        self.switches = set()
        self.links = set()

    def _handle_ConnectionUp(self, event):
        dpid = event.dpid
        self.switches.add(dpid)
        self.log_change(f"Switch ADDED: {dpid}")

    def _handle_ConnectionDown(self, event):
        dpid = event.dpid
        if dpid in self.switches:
            self.switches.remove(dpid)
        self.log_change(f"Switch REMOVED: {dpid}")

    def _handle_LinkEvent(self, event):
        link = (event.link.dpid1, event.link.dpid2)

        if event.added:
            self.links.add(link)
            self.log_change(f"Link ADDED: {link}")

        elif event.removed:
            if link in self.links:
                self.links.remove(link)
            self.log_change(f"Link REMOVED: {link}")

    def log_change(self, message):
        timestamp = datetime.datetime.now()
        log_msg = f"{timestamp} - {message}"

        log.info(log_msg)

        with open("topology_log.txt", "a") as f:
            f.write(log_msg + "\n")


def launch():
    # Enable discovery module (VERY IMPORTANT)
    core.registerNew(TopologyDetector)
