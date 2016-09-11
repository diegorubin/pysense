from gi.repository import Notify, GdkPixbuf
from os.path import join

from sense.settings import ICONS_PATH

Notify.init("Sense")

def notify(title, body, image = None):
    notification = Notify.Notification.new(title, body)

    if not image is None:
        f = join(ICONS_PATH, image)
        pixbuf = GdkPixbuf.Pixbuf.new_from_file(f)
        notification.set_icon_from_pixbuf(image)
        notification.set_image_from_pixbuf(image)

    notification.show()

